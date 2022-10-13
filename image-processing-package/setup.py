from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Processamento_de_imagem",
    version="0.0.1",
    author="Gustavo Costa",
    author_email="gustavoalbano1998@gmail.com",
    description="Pacote de processamento de imagens com skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GustavoAlbano98/Processador_de_Imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
