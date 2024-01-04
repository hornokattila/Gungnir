import setuptools

import settings

setuptools.setup(
    install_requires=open("requirements.txt").readlines(),
    long_description=open("README.md").read(),
    packages=setuptools.find_packages(),
    python_requires=">=3.12",
    **settings.settings["system"]
)
