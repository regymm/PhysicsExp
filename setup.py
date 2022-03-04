# -*- coding:utf-8 -*-
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="physicsexp",
    version="0.0.3",
    author="regymm",
    author_email="username@mail.ustc.edu.cn",
    description="A simple wrapper of numpy and matplotlib to make physics experiment data analyse easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/regymm/PhysicsExp",
    packages=['physicsexp'],
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'python-docx'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
