# https://www.mdpi.com/2076-2615/11/11/3089/htm

import os
import xml.etree.ElementTree as ET

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s
import src.utils as u


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "Automatic Monitoring of Pigs"
    dataset_path = "/mnt/d/datasetninja-raw/automatic-monitoring-pigs/supplementary_files"
    batch_size = 30
    ds_name = "ds"
    data_folder = "labeled_testing_datasets"
    images_ext = ".jpg"
    bboxes_ext = ".xml"

    def create_ann(image_path):
        labels = []

        image_name = get_file_name(image_path)
        image_time = image_name.split(" ")[1]
        image_hour = image_time.split("-")[0]
        image_hour_decimal = u.time_to_decimal_hour(image_time)

        CO2_data = u.calculate_y_graph(
            image_hour_decimal, u.m_values_CO2, u.b_values_CO2, u.x_ranges
        )
        tag_CO2 = sly.Tag(tag_CO2_meta, value=int(round(CO2_data, -1)))
        mix_data = u.calculate_y_graph(
            image_hour_decimal, u.m_values_mix, u.b_values_mix, u.x_ranges
        )
        tag_mix = sly.Tag(tag_mixture_of_gases_meta, value=round(mix_data))

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        bbox_path = image_path.split(".")[0] + bboxes_ext

        if file_exists(bbox_path):
            tree = ET.parse(bbox_path)
            root = tree.getroot()

            coords_xml = root.findall(".//object")
            for curr_object in coords_xml:
                label_tags = []
                pose = curr_object.find(".//name").text
                tag_meta = pose_to_tag[pose]
                tag = sly.Tag(tag_meta)
                label_tags.append(tag)
                score_data = pose_to_score[pose]
                score_value = score_data.get(image_hour)
                if score_value is not None:
                    treatment_meta = time_to_treatment[image_hour]
                    treatment = sly.Tag(treatment_meta)
                    score = sly.Tag(score_meta, value=score_value)
                    label_tags.extend([treatment, score])
                curr_coord = curr_object.find(".//bndbox")

                left = int(curr_coord[0].text)
                top = int(curr_coord[1].text)
                right = int(curr_coord[2].text)
                bottom = int(curr_coord[3].text)

                rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
                label = sly.Label(rect, obj_class, label_tags)
                labels.append(label)

        return sly.Annotation(
            img_size=(img_height, img_wight), labels=labels, img_tags=[tag_CO2, tag_mix]
        )

    obj_class = sly.ObjClass("pig", sly.Rectangle)

    tag_standing = sly.TagMeta("standing pig", sly.TagValueType.NONE)
    tag_ll = sly.TagMeta("lateral lying pig", sly.TagValueType.NONE)
    tag_sl = sly.TagMeta("sternal lying pig", sly.TagValueType.NONE)

    tag_CO2_meta = sly.TagMeta("CO2_ppm", sly.TagValueType.ANY_NUMBER)
    tag_mixture_of_gases_meta = sly.TagMeta("CO_NO_CH4_ppm", sly.TagValueType.ANY_NUMBER)

    # CO2_to_values = {
    #     "07": [900, 2150],
    #     "08": [2150, 1700],
    #     "13": [900, 2000],
    #     "14": [2000, 1500],
    #     "18": [1300, 1100],
    #     "19": [1100, 900],
    #     "09": [1700, 1600],
    #     "10": [1600, 1300],
    # }

    # mixture_to_values = {
    #     "07": [900, 1500],
    #     "08": [1500, 1100],
    #     "13": [900, 1400],
    #     "14": [1400, 1300],
    #     "18": [1100, 900],
    #     "19": [900, 800],
    #     "09": [1100, 1050],
    #     "10": [1050, 1000],
    # }

    tag_before = sly.TagMeta("before treatment", sly.TagValueType.NONE)
    tag_during = sly.TagMeta("during treatment", sly.TagValueType.NONE)
    tag_after = sly.TagMeta("after treatment", sly.TagValueType.NONE)
    score_meta = sly.TagMeta("score", sly.TagValueType.ANY_NUMBER)

    time_to_treatment = {
        "07": tag_during,
        "08": tag_after,
        "13": tag_during,
        "14": tag_after,
        "19": tag_before,
    }

    score_standing_to_values = {
        "07": 0.11,
        "08": 0.16,
        "13": 0.08,
        "14": 0.12,
        "19": 0.13,
    }

    score_ll_to_values = {
        "07": 2.7,
        "08": 2,
        "13": 3.5,
        "14": 3,
        "19": 3.3,
    }

    score_sl_to_values = {
        "07": 1.5,
        "08": 1.5,
        "13": 1.2,
        "14": 1.4,
        "19": 1.3,
    }

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class],
        tag_metas=[
            tag_standing,
            tag_ll,
            tag_sl,
            tag_CO2_meta,
            tag_mixture_of_gases_meta,
            tag_before,
            tag_during,
            tag_after,
            score_meta,
        ],
    )
    api.project.update_meta(project.id, meta.to_json())

    pose_to_tag = {
        "standing_pig": tag_standing,
        "ll_pig": tag_ll,
        "sl_pig": tag_sl,
    }

    pose_to_score = {
        "standing_pig": score_standing_to_values,
        "ll_pig": score_ll_to_values,
        "sl_pig": score_sl_to_values,
    }

    data_path = os.path.join(dataset_path, data_folder)

    images_names = [
        im_name for im_name in os.listdir(data_path) if get_file_ext(im_name) == images_ext
    ]

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [
            os.path.join(data_path, image_name) for image_name in images_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(images_names_batch))
    return project
