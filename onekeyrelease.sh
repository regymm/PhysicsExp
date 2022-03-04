#!/bin/bash
python3 setup.py sdist bdist_wheel
sudo pip3 install --upgrade dist/physicsexp-0.0.2-py3-none-any.whl
