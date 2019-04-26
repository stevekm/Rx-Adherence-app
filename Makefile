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
	conda install -y -c anaconda -c conda-forge  \
	python=3.6 \
	django=2.1.5 \
	gunicorn=19.9.0 \
	nginx=1.15.5 \
	nodejs=10.13.0
	# && \
	# pip install \
	# djangorestframework==3.9.2 \
	# markdown==3.1 \
	# django-filter==2.1.0

# ~~~~~ SETUP DJANGO APP ~~~~~ #
# dir with db files for dev
export DB_DIR:=db
# filenames inside db dir
export DJANGO_DB:=django.sqlite3
export RXADHERENCE_DB:=rxadherence.sqlite3
export DRUGS_FILE:=drugs.csv
# create the app for development; only need to run this when first creating repo
# django-start:
# 	django-admin startproject webapp .
# 	python manage.py startapp rxadherence

init:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py migrate rxadherence
	python manage.py migrate rxadherence --database=rxadherence_db
	python manage.py createsuperuser
	python manage.py collectstatic

import:
	python rxadherence/importer.py --type drug --file "$(DB_DIR)/$(DRUGS_FILE)"
	python rxadherence/importer.py --type user --username "Bob"
	python rxadherence/importer.py --type user --username "Mary"
	python rxadherence/importer.py --type user --username "John"
	python rxadherence/importer.py --type user --username "Jane"
	python rxadherence/importer.py --type usage --username "Jane" --drug-id 1
	python rxadherence/importer.py --type usage --username "Jane" --drug-id 1
	python rxadherence/importer.py --type usage --username "Bob" --drug-id 1
	python rxadherence/importer.py --type usage --username "Bob" --drug-id 1
	python rxadherence/importer.py --type usage --username "John" --drug-id 2
	python rxadherence/importer.py --type usage --username "John" --drug-id 2
	python rxadherence/importer.py --type usage --username "Mary" --drug-id 3
	python rxadherence/importer.py --type usage --username "Mary" --drug-id 3
	python rxadherence/importer.py --type usage --username "Mary" --drug-id 3

USERNAME:=
import-user:
	if [ -n "$(USERNAME)" ]; then python rxadherence/importer.py --type user --username "$(USERNAME)"; fi

# need runserver running for this
# demo query of API
# [{"url":"http://localhost:8000/users/1/","username":"steve","email":"","is_staff":true}]
get-users:
	curl localhost:8000/users/
get-drugs:
	curl localhost:8000/drugs/

# run the Django dev server
runserver:
	python manage.py runserver

# start interactive shell
shell:
	python manage.py shell

# run arbitrary user-passed command
CMD:=
cmd:
	$(CMD)

# ~~~~~ RESET ~~~~~ #
# re-initialize just the databases
reinit: nuke
	python manage.py makemigrations
	python manage.py migrate
	python manage.py migrate rxadherence --database=rxadherence_db

# destroy app database
nuke:
	@echo ">>> Removing database items:"; \
	rm -rfv rxadherence/migrations/__pycache__ && \
	rm -fv rxadherence/migrations/0*.py && \
	rm -fv "$$(python -c 'import os; print(os.path.join("$(DB_DIR)", "$(RXADHERENCE_DB)"))')"

# delete the main Django database as well..
nuke-all: nuke
	rm -fv "$$(python -c 'import os; print(os.path.join("$(DB_DIR)", "$(DJANGO_DB)"))')"



frontend-install:
	cd frontend && \
	npm install

frontend-run:
	cd frontend && \
	npm run serve







# ~~~~~ NGINX and GUNICORN ~~~~~ #
SOCKET:=unix:$(CURDIR)/Rx-Adherence-app.sock
NGINX_PREFIX:=$(CURDIR)
NGINX_CONF:=nginx.conf
# nginx-conf:
nginx-start:
	nginx -p "$(NGINX_PREFIX)" -c "$(NGINX_CONF)"

nginx-stop:
	nginx -p "$(NGINX_PREFIX)" -c "$(NGINX_CONF)" -s quit

nginx-reload:
	nginx -p "$(NGINX_PREFIX)" -c "$(NGINX_CONF)" -s reload

nginx-test:
	nginx -p "$(NGINX_PREFIX)"  -c "$(NGINX_CONF)" -t

nginx-check:
	ps -ax | grep nginx



# gunicorn config stored separately
GUNICORN_NAME:=gunicorn-Rx-Adherence
GUNICORN_CONFIG:=gunicorn_config.py
GUNICORN_PIDFILE:=$(LOG_DIR)/gunicorn.pid
GUNICORN_ACCESS_LOG:=$(LOG_DIR)/gunicorn.access.log
GUNICORN_ERROR_LOG:=$(LOG_DIR)/gunicorn.error.log
GUNICORN_LOG:=$(LOG_DIR)/gunicorn.log
gunicorn-start:
	gunicorn webapp.wsgi \
	--bind "$(SOCKET)" \
	--config "$(GUNICORN_CONFIG)" \
	--pid "$(GUNICORN_PIDFILE)" \
	--access-logfile "$(GUNICORN_ACCESS_LOG)" \
	--error-logfile "$(GUNICORN_ERROR_LOG)" \
	--log-file "$(GUNICORN_LOG)" \
	--name "$(GUNICORN_NAME)"
	# \
	# --daemon

gunicorn-check:
	ps -ax | grep gunicorn

GUNICORN_PID:=
gunicorn-stop: GUNICORN_PID=$(shell head -1 $(GUNICORN_PIDFILE))
gunicorn-stop: $(GUNICORN_PIDFILE)
	kill "$(GUNICORN_PID)"
