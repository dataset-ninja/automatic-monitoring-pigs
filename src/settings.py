from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Automatic Monitoring of Pigs"
PROJECT_NAME_FULL: str = "Automatic Monitoring of Pigs` Physico-Temporal Activities at Different Greenhouse Gas Concentrations"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Livestock()]
CATEGORY: Category = Category.Livestock()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2021-10-29"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = None
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 3154242
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/automatic-monitoring-pigs"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://drive.google.com/file/d/1DmkR5AyysQkFbMEwjPjJnnNVyGvtsu9H/view"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
PAPER: Optional[Union[str, List[str]]] = "https://www.mdpi.com/2076-2615/11/11/3089/htm#"
BLOGPOST: Optional[Union[str, List[str]]] = None
CITATION_URL: Optional[str] = "https://www.mdpi.com/2076-2615/11/11/3089/htm#"
AUTHORS: Optional[List[str]] = [
    "Bhujel, Anil",
    "Arulmozhi, Elanchezhian",
    "Moon, Byeong-Eun",
    "Kim, Hyeon-Tae",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Gyeongsang National University, Korea",
    "Ministry of Communication and Information Technology, Nepal",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.gnu.ac.kr/eng/main.do",
    "https://mocit.gov.np/",
]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with value:str to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "__PRETEXT__": "Every image has information about ***CO2_ppm*** and ***CO_NO_CH4_N2O_ppm*** gas concentrations, while every object has information about it's posture: ***standing pig***, ***sternal lying pig***, ***lateral lying pig***; and it's treatment' ***score*** and state: ***before treatment***, ***during treatment***, ***after treatment***"
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")
    settings["homepage_url"] = HOMEPAGE_URL
    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
