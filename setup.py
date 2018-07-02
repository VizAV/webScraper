from distutils.core import setup

setup(
    # Application name:
    name="webScraper",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="vishwanathAV",
    author_email="vishwanathavin@gmail.com",

    # Packages
    packages=["webScraper"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/webScraper_v010/",

    #
    # license="LICENSE.txt",
    description="Extracts the html from JSON depending upon the ",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "bs4","lxml"
    ],
)