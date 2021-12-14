# Using BEM for Conda
Bem is a packaging utility built for developers. It's useable accross a variety of environments, but its original use was in python conda environments. Key features are:
 - Simple CI/CD
 - Simple venv creation
 - Simple VM implementation

## Activation Process
Bem wraps pip and Conda. The best easiest ways to get started are in the Makefile:
make vagrant.conda # to spin up a vm
make conda # to install on a local conda environment

### Vagrant Conda
This workflow spins up a vm and creates a Conda environment with your package installed within the vm. The working directory is shared with the machine as well, in /vagrant.
This is an editable install, so changes to your local codebase should reflect to the vm.

### Conda
This creates a new install of your project in a fresh conda env. This is also an editable install.

## License

MIT (See LICENSE file).

## Commands

black --line-length 150 .

flake8 --max-line-length=150 .

radon cc .

## How to make a BEM Project: Python

To get started creating a new Python project with BEM, first fork this repository. You will then want to begin replacing bemplate configurations with your own.
To begin this process, we reccomend a text search to replace all instances--both within files and in file and folder names--of "bemplate" with your project name. Note that the only required changes are:
Makefile (APPNAME)
Manifest.in (relevant filepaths)
pyproject.toml (project.name)
Other instances of "bemplate" are likely reflexive imports or dependencies. Since these are likely to change regardless, we leave it to you to apply updates.
The following steps are expanded in less detail, but they are as follows:
update the pyproject.toml
update the license
update the makefile variables
update the environment dependencies in dependencies/
replace src/bemplate with src/{yourproject} and the relevant concepts, or begin developing from the bemplate skeleton.

### .repo
the .repo folder contains a list of files used for configuring BEM. The filenames are treated as environmental keywords, and the contents of the file are the corresponding values. Options for these will be documented in the official BEM documentation.

### dependencies
The dependencies folder contains a list of environment dependencies needed for your project. These should contain the name of the installing tool (e.g., apt-get, etc) followed by a list of commands to pass to the installer. Note that package dependences should not be placed here, as those are found in pyprojct.toml's /[project/].dependencies.

### src
The src/ directory holds your project. This should contain a folder with the name of your package, and relevant files should be placed within.

### Makefile
The makefile holds a selection of useful commands, namely the vagrant.conda, conda, nuke, and lint commands. Currently the only parts intended to be user servicable are the variables declared at the beggining. These will likely be moved to pyproject.toml in a coming version.

### setup.cfg
BEM projects don't make use of a setup.cfg file. relevant information that might have been stored here should now be located in pyproject.toml.

### setup.py
in BEM projects, setup.py is not intended to be user-servicable. If you do find yourself needing to edit this file, please open an issue in this repository. There may be a more standard approach, or we may need to add features.

### .tmp
The .tmp folder is generated (if not already present) by BEM and houses many of of it's tools. It also can be configured as detailed below to further empower BEM.

#### .tmp/repo
This folder is to contain local installs of python repos. If source files for a pip-installable package are placed here, they will be installed in an editable format. This install should overwrite default dependency installs in pyproject.toml, but conflicts may occur due to version pinning. 
This feature is in BETA and should not be conisidered stable.
This is a development feature and not intended for use in production environments.
Possible coming features include sub-folders relating to the desired install-tool. 

## Development Features working in BEM

```md
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
```