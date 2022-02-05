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
            "black==22.1.0",
            "isort==5.10.1",
            "flake8==4.0.1",
            "mypy==0.931",
            "pytest==6.2.5",
            "coverage==6.3.1",
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
