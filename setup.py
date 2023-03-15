from setuptools import setup, find_packages

# Get version number
def getVersionNumber():
    with open("easy_arrow/VERSION", "r") as vfile:
        version = vfile.read().strip()
    return version


__version__ = getVersionNumber()

PROJECT_URLS = {
    "Bug Tracker": "https://github.com/kmdalton/easy-arrow/issues",
    "Source Code": "https://github.com/kmdalton/easy-arrow",
}


LONG_DESCRIPTION = """
This is a simple alternative for drawing fancy arrows in matplotlib.
"""

setup(
    name="easy-arrow",
    version=__version__,
    author="Kevin M. Dalton",
    license="MIT",
    include_package_data=True,
    packages=find_packages(),
    long_description=LONG_DESCRIPTION,
    description="Easily plot nice-looking arrows with matplotlib",
    project_urls=PROJECT_URLS,
    python_requires=">=3.6",
    url="https://github.com/kmdalton/easy-arrow",
    install_requires=[
        "matplotlib",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
)

