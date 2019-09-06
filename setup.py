from setuptools import setup

with open("README.md") as fh:
    long_desc = fh.read()

setup(
    name="minfinder",
    description="Find minimum of array having a special structure",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="Ishan Bhatt",
    packages=["minfinder"],
    include_package_data=True,
    licence="Public",
    version="0.0.1",
    maintainer_email="ishan_bhatt@hotmail.com",
    test_suite="tests",
    python_requires='>=3.6',
)
