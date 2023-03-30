# imports
import setuptools

# read files from README.md
with open("README.md", "r", encoding="utf8") as f:
    long_description = f.read()

# project version
__version__ = "0.0.0"

REPO_NAME = "CAT_DOG_CLASSIFIER_CNN"
AUTHOR_USERNAME = "utkarshkant"
SRC_REPO = "CAT_DOG_CLASSIFIER_CNN"
AUTHOR_EMAIL = "utkarsh.kant@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USERNAME,
    author_email = AUTHOR_EMAIL,
    description = "A small Python package for CNN Classifier",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)