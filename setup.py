from setuptools import setup, find_packages

from elizur import VERSION


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    author="Tanner Rollefson",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
    ],
    description="Elizur is an open source finance package for actuaries, finance professionals, and students",
    install_requires=["numpy>=1.18", "makefun>=1.9.2"],
    extras_require={
        "dev": [
            "black",
            "coveralls",
            "mock",
            "pylint",
            "pytest",
            "pytest-cov",
            "sphinx",
            "sphinx_rtd_theme",
        ]
    },
    keywords="actuary, actuarial, life, contingencies, finance, math, elizur",
    long_description=readme(),
    long_description_content_type="text/markdown",
    name="elizur",
    packages=find_packages(include=["elizur*"]),
    project_urls={
        "Documentation": "https://trollefson.github.io/elizur",
        "Source": "https://github.com/trollefson/elizur",
    },
    url="https://github.com/trollefson/elizur",
    version=VERSION,
    zip_safe=False,
)
