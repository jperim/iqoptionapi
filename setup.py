"""The python wrapper for IQ Option API package setup."""
from setuptools import (setup, find_packages)

setup(
    name="iqoptionapi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests", "websocket-client"],
    include_package_data=True,
    description="Best IQ Option API for python",
    long_description="Best IQ Option API for python",
    url="https://github.com/iqoptionapi/iqoptionapi",
    author="Rafael Faria",
    zip_safe=False
)
