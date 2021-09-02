import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reinvent_models",
    version="0.0.7",
    author="PaccMann Team",
    description="Generative models for Reinvent adapted for PaccMann",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PaccMann/reinvent_models",
    packages=setuptools.find_packages(exclude=("testing",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["numpy", "torch", "dacite"],
)
