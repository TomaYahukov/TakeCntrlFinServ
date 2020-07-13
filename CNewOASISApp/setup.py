#From packaging.python.org/tutorials/packaging-projects/
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NewOASISApp-TomaYahukov",
    version="0.0.1",
    author="TomaYahukov",
    author_email="tomayahukov@yahoo.com",
    description="Project with a mission to reserect OASIS Class Lib and to utilize it to create and maintain a Persons databae.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TomaYahukov/TakeCntrlFinServ/CNewOASISApp.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
