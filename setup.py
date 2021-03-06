import os
from typing import List

from setuptools import find_packages, setup

import mlflow_extend

ROOT = os.path.abspath(os.path.dirname(__file__))


# Use README.md as a long description.
def get_long_description() -> str:
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as f:
        return f.read()


def get_install_requires() -> List[str]:
    with open(os.path.join(ROOT, "requirements.txt"), encoding="utf-8") as f:
        return [
            line.strip()
            for line in f.readlines()
            if not (line.startswith("#") or (line.strip() == ""))
        ]


setup(
    name="mlflow-extend",
    version=mlflow_extend.__version__,
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=get_install_requires(),
    maintainer="harupy",
    maintainer_email="hkawamura0130@gmail.com",
    url="https://github.com/harupy/mlflow-extend",
    project_urls={
        "Documentation": "https://mlflow-extend.readthedocs.io/en/latest/index.html",
        "Source Code": "https://github.com/harupy/mlflow-extend",
        "Bug Tracker": "https://github.com/harupy/mlflow-extend/issues",
    },
    description="Extend MLflow's functionality",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
