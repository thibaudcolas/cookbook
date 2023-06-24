import io

from setuptools import find_packages, setup  # type: ignore

from cookbook import (
    __author__,
    __author_email__,
    __copyright__,
    __description__,
    __license__,
    __name__,
    __url__,
    __version__,
)

with io.open("README.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name=__name__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    copyright=__copyright__,
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    package_data={"cookbook": ["py.typed"]},
    keywords=[
        "cookbook",
        "recipes",
        "guidelines",
        "code reviews",
        "pull requests",
        "best practices",
        "programming",
        "configuration",
        "styleguide"
    ],
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
        "dev": [
            "black==23.3.0",
            "isort==5.12.0",
            "flake8==6.0.0",
            "mypy==1.4.0",
            "pytest==7.4.0",
            "coverage==7.2.7",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Quality Assurance",
        "Typing :: Typed",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
