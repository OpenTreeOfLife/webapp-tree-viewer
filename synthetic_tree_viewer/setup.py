import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.txt")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.txt")) as f:
    CHANGES = f.read()

requires = [
    "authomatic",
    "bleach",
    "markdown",
    "plaster_pastedeploy",
    "pyramid",
    "pyramid_debugtoolbar",
    "pyramid_jinja2",
    "pyramid_retry",
    "pytz",
    "requests",
    "waitress",
]

tests_require = [
    "pytest",
    "pytest-cov",
    "WebTest",
]

setup(
    name="synthetic_tree_viewer",
    version="0.0",
    description="synthetic tree viewer",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="",
    author_email="",
    url="",
    keywords="web pyramid pylons",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        "testing": tests_require,
    },
    install_requires=requires,
    entry_points={
        "paste.app_factory": [
            "main = synthetic_tree_viewer:main",
        ],
    },
)
