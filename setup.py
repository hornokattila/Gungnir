import setuptools

import settings

setuptools.setup(
    **settings.settings["system"],
    install_requires=open("requirements.txt").readlines(),
    long_description=open("README.md").read(),
    packages=setuptools.find_packages(),
    python_requires=">=3.11"
)
