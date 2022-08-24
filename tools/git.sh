#!/bin/bash


# Git Setup Multiple Repository
git remote add gitlab git@gitlab.com:progdevlab/vuejs_framework_oidc.git
git remote set-url --add --push origin git@gitlab.com:progdevlab/vuejs_framework_oidc.git

git remote add github git@github.com:ProgDevLab/VueJS_Framework_OIDC.git
git remote set-url --add --push origin git@github.com:ProgDevLab/VueJS_Framework_OIDC.git


# Display Config
git remote show origin

git config --list
