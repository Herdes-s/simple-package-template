from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="soma_saudacao",
    version="0.0.1",
    author="Herdes",
    author_email="my_email",
    description="funcção de soma e de saudção",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url='',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)