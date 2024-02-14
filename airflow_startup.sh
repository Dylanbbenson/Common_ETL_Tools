#!/bin/bash

sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade

sudo apt install pip

sudo apt install python3.10-venv

python3 -m venv airflow_venv

source airflow_venv/bin/activate

sudo pip install pandas

sudo pip install apache-airflow

#optional install
pip install Flask-Session==0.5.0 

pip install kubernetes

source airflow_venv/bin/activate

airflow standalone