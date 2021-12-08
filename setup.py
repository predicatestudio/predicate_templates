from pathlib import Path
from setuptools import setup
from setuptools import find_packages
import toml
import re


def normalize(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def _parse_pyproject():
    pyproject_path = "pyproject.toml"
    pp = Path(pyproject_path)
    return toml.load(pp.open())


pyproject = _parse_pyproject()
project_name = normalize(pyproject["project"]["name"])
setup(
    name=project_name,
    version=pyproject["project"]["version"],
    description=pyproject["project"]["description"],
    url=pyproject["project"]["urls"]["repository"],
    author=[auth for auth in pyproject["project"]["authors"]],
    author_email=[auth for auth in pyproject["project"]["authors"]],
    license_files=pyproject["project"]["license"],
    package_dir={"": pyproject["tool"]["bem"]["source-directory"]},
    packages=find_packages(where=pyproject["tool"]["bem"]["source-directory"]),
    zip_safe=False,
    include_package_data=True,
    python_requires=pyproject["project"]["requires-python"],
    install_requires=pyproject["project"]["dependencies"],  # _fw_lib.smart_reqs(_local.extras, package_name),
    extras_require=pyproject["project"]["optional-dependencies"],
    entry_points="""
        [console_scripts]
    """
    + f"{project_name}={project_name}.__main__:main",
)
