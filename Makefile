SHELL:=/bin/bash
UNAME:=$(shell uname)
export LOG_DIR:=logs
export LOG_DIR_ABS:=$(shell python -c 'import os; print(os.path.realpath("$(LOG_DIR)"))')
# install app
install: conda-install init

# ~~~~~ Setup Conda ~~~~~ #
# this sets the system PATH to ensure we are using in included 'conda' installation for all software
PATH:=$(CURDIR)/conda/bin:$(PATH)
unexport PYTHONPATH
unexport PYTHONHOME

# install versions of conda for Mac or Linux
ifeq ($(UNAME), Darwin)
CONDASH:=Miniconda3-4.5.4-MacOSX-x86_64.sh
endif

ifeq ($(UNAME), Linux)
CONDASH:=Miniconda3-4.5.4-Linux-x86_64.sh
endif

CONDAURL:=https://repo.continuum.io/miniconda/$(CONDASH)

# install conda
conda:
	@echo ">>> Setting up conda..."
	@wget "$(CONDAURL)" && \
	bash "$(CONDASH)" -b -p conda && \
	rm -f "$(CONDASH)"

# install the conda and python packages required
# NOTE: **MUST** install ncurses from conda-forge for RabbitMQ to work!!
conda-install: conda
	conda install -y -c anaconda \
	python=3.6 \
	django=2.1.5

# ~~~~~ SETUP DJANGO APP ~~~~~ #
export DJANGO_DB:=django.sqlite3
export DASHBOARD_DB:=dashboard.sqlite3
# create the app for development; only need to run this when first creating repo
# django-start:
# 	django-admin startproject webapp .
# 	python manage.py startapp rxadherence
