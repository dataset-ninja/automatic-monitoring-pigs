# https://www.mdpi.com/2076-2615/11/11/3089/htm

import os
import shutil
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
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


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "Automatic Monitoring of Pigs"
    dataset_path = "/mnt/d/datasetninja/automatic-monitoring-pigs/supplementary_files"
    batch_size = 30
    ds_name = "ds"
    data_folder = "labeled_testing_datasets"
    images_ext = ".jpg"
    bboxes_ext = ".xml"

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        bbox_path = image_path.split(".")[0] + bboxes_ext

        if file_exists(bbox_path):
            tree = ET.parse(bbox_path)
            root = tree.getroot()

            coords_xml = root.findall(".//object")
            for curr_object in coords_xml:
                pose = curr_object.find(".//name").text
                tag_meta = pose_to_tag[pose]
                tag = sly.Tag(tag_meta)
                curr_coord = curr_object.find(".//bndbox")

                left = int(curr_coord[0].text)
                top = int(curr_coord[1].text)
                right = int(curr_coord[2].text)
                bottom = int(curr_coord[3].text)

                rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
                label = sly.Label(rect, obj_class, [tag])
                labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class = sly.ObjClass("pig", sly.Rectangle)

    tag_standing = sly.TagMeta("standing pig", sly.TagValueType.NONE)
    tag_ll = sly.TagMeta("lateral lying pig", sly.TagValueType.NONE)
    tag_sl = sly.TagMeta("sternal lying pig", sly.TagValueType.NONE)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class], tag_metas=[tag_standing, tag_ll, tag_sl])
    api.project.update_meta(project.id, meta.to_json())

    pose_to_tag = {"standing_pig": tag_standing, "ll_pig": tag_ll, "sl_pig": tag_sl}

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
