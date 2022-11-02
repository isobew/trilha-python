from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="img-processing-pcg",
    version="0.0.1",
    author="Isabella Firmino",
    author_email="isabella.mfbr@gmail.com",
    description="Test version - Image processing. This project belongs to Karina Tiemi Kato, Tech Lead, Machine Learning Engineer, Data Scientist Specialist. This package is a demo for simulation of upload on the Test Pypi website, and it's from class of the Bootcamp Geração Tech Unimed-BH - Ciência de Dados.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/isobew/trilha-python/tree/main/pacotes_process_img/image-processing-package"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)