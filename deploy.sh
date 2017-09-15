#!/usr/bin/env bash

# Script for deployment of the app

FLASK_APP = "app.py"
VENV_FOLDER = "flask_virtual_env"

setup_virtualenv(){
    sudo pip install virtualenv;
    mkdir $(VENV_FOLDER);
    cd $(VENV_FOLDER);
    virtualenv venv;
    source venv/bin/activate;
    pip install -r requirements.txt;
}

main(){
    setup_virtualenv
    export FLASK_APP=$(FLASK_APP)
    chmod +x $(FLASK_APP)
    ./$(FLASK_APP)
}

main




