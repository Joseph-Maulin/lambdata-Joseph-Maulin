
# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-Joseph-Maulin", # the name that you will install via pip
    version="1.1",
    author="Joseph Maulin",
    author_email="joseph_l_maulin@gmail.com",
    description="Helper functions for data science",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Joseph-Maulin/lambdata-Joseph-Maulin",
    #keywords="",
    packages=find_packages() # ["helper_functions"]
)
