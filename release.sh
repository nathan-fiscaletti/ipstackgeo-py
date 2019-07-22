#!/bin/bash

if [[ "$1" == "build" ]]; then
    rm -rf ./dist/*
    python3 setup.py sdist bdist_wheel
    exit
fi

if [[ "$1" == "upload-test" ]]; then
    python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    exit
fi

if [[ "$1" == "upload" ]]; then
    python3 -m twine upload dist/*
fi