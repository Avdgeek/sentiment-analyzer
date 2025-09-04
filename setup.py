# setup.py
from setuptools import setup, find_packages

setup(
    name="sentiment-analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask==2.3.3",
        "transformers==4.36.2",
        "torch==2.8.0",
        "numpy==1.24.3",
        "gunicorn==21.2.0"
    ],
    python_requires=">=3.8",
)
