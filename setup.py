from pathlib import Path
from setuptools import setup
from setuptools import find_packages
import toml
import re
from os import path, mkdir
import shutil
from urllib import request
from zipfile import ZipFile


def normalize(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def _parse_pyproject():
    pyproject_path = "pyproject.toml"
    pp = Path(pyproject_path)
    return toml.load(pp.open())


def create_dirs(dirs):
    for dir in dirs:
        if not path.exists(dir):
            mkdir(dir)


def dl_bash_repos(repos, _tmp):
    for repo in repos:
        request.urlretrieve(repo["url"], repo["filename"])
        with ZipFile(repo["filename"], "r") as zip_ref:
            zip_ref.extractall(_tmp)


# VARS
pyproject = _parse_pyproject()
project_name = normalize(pyproject["project"]["name"])
src = pyproject["tool"]["bem"]["source-directory"]
dirs = [".tmp", ".tmp/download", ".tmp/logs"]
# BEM setup and framework import

create_dirs(dirs)

# repos = [
#     {
#         "url": "https://github.com/terminal-labs/bash-environment-shelf/archive/refs/heads/master.zip",
#         "filename": ".tmp/download/bash-environment-shelf.zip",
#     }
# ]
shelf_name = ".tmp/download/bash-environment-shelf.zip"


def install_codepacks(bem_shelf):
    print(bem_shelf)
    for codepack, url in bem_shelf.items():
        request.urlretrieve(url, shelf_name)
        with ZipFile(shelf_name, "r") as zip_ref:
            zip_ref.extractall(".tmp")
        if src:
            cpack_path = Path(src + "/" + project_name + "/" + "framework")
        else:
            cpack_path = Path(project_name + "/" + "framework")
        shutil.rmtree(cpack_path, ignore_errors=True)
        shutil.copytree(".tmp/bash-environment-shelf-master/codepacks/" + codepack, cpack_path)


install_codepacks(pyproject.get("tool", {}).get("bem", {}).get("codepack", {}))
# dl_bash_repos(repos, ".tmp")

# _path_to_framework = src + "/" + project_name + "/" + "framework"
# if path.exists(_path_to_framework):
#     shutil.rmtree(_path_to_framework)

# if not path.exists(_path_to_framework):
#     shutil.copytree(".tmp/bash-environment-shelf-master/codepacks/framework", _path_to_framework)


# setuptools setup
def parse_extras_require(pyproject):
    extra_requirements = pyproject["project"]["optional-dependencies"]
    recursive_re = re.compile(project_name + r"\[.*\]")
    extra_re = re.compile(r"(?<=\[).*(?=\])")

    def parse_extra(reqs):
        parsed_reqs = []
        for req in reqs:
            if recursive_re.fullmatch(req):
                extra_name = extra_re.search(req).group(0)
                parsed_reqs += [expanded_rq for expanded_rq in parse_extra(extra_requirements[extra_name])]
            else:
                parsed_reqs.append(req)
        return parsed_reqs

    for extra, reqs in extra_requirements.items():
        extra_requirements[extra] = parse_extra(reqs)
    return extra_requirements

setup_kwargs = {}
if not src:
    setup_kwargs["packages"] = [project_name]
else:
    setup_kwargs["packages"] = find_packages(where=src)
    setup_kwargs["package_dir"] = {"": src}

setup(
    name=project_name,
    version=pyproject["project"]["version"],
    description=pyproject["project"]["description"],
    url=pyproject["project"]["urls"]["repository"],
    author=[auth for auth in pyproject["project"]["authors"]],
    author_email=[auth for auth in pyproject["project"]["authors"]],
    license_files=pyproject["project"]["license"],
    # package_dir={"": src},
    # packages=found_packages,
    zip_safe=False,
    include_package_data=True,
    python_requires=pyproject["project"]["requires-python"],
    install_requires=pyproject["tool"]["bem"].get("pins") + pyproject["project"]["dependencies"],
    extras_require=parse_extras_require(pyproject),
    entry_points="""
        [console_scripts]
    """
    + f"{project_name}={project_name}.__main__:main",
    **setup_kwargs
)
