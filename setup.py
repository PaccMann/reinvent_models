import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reinvent_models",
    version="0.0.7",
    author="MolecularAI",
    author_email="patronov@gmail.com",
    description="Generative models for Reinvent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.astrazeneca.net/scm/com/reinvent_models.git",
    packages=setuptools.find_packages(exclude=("testing",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["numpy", "torch", "dacite"],
)
