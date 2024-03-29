import os
import shutil
import urllib

# import subprocess
import importlib.util
from os.path import abspath, exists
from zipfile import ZipFile

# from configparser import ConfigParser


def import_mod_from_fp(module_name, filepath):
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_fw_settings = import_mod_from_fp("lib", os.path.dirname(__file__) + "/framework/settings.py")


def _delete_dir(directory):
    directory = abspath(directory)
    if exists(directory):
        shutil.rmtree(directory)


def _create_dir(directory):
    directory = abspath(directory)
    if not exists(directory):
        os.makedirs(directory)


def _copy_dir(source, target):
    if not exists(target):
        shutil.copytree(abspath(source), abspath(target))


def _create_dirs(dirs):
    for dir in dirs:
        _create_dir(dir)


# def _resolve_payload_path():
#     payload_name = "/payload"
#     possible_path = SITEPACKAGESPATH + "/" + EGG_NAME + ".egg-link"
#     if exists(possible_path):
#         egglink_file = open(possible_path, "r")
#         link_path = egglink_file.read().split("\n")[0]
#         possible_payload_path = link_path + "/" + PROJECT_NAME + payload_name
#     else:
#         possible_path = SITEPACKAGESPATH + "/" + PROJECT_NAME
#         possible_payload_path = possible_path + payload_name
#     return possible_payload_path


def _get_github_repo(url, target, filename, extract):
    # zipname = filename.replace(".zip", "-master")
    url = url + "/archive/master.zip"
    if not exists(target):
        with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall(path=extract)
