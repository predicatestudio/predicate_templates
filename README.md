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

### .repo

### dependencies

### src

### Makefile

### setup.cfg

### setup.py

## Development Features working in BEM

```md
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
```