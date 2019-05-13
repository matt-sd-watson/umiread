import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="umiread",
    version="1.1.0",
    author="Matthew Watson",
    author_email="matt.sd.watson@gmail.com",
    description="Lightweight utility for 10x single cell assays",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matt-sd-watson/umiread",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], install_requires=['gzip', 'itertools', 'glob', 'numpy', 'collections'
                         'pandas', 'matplotlib'],
)
