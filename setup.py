import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="airflow-provider-tm1",
    version="0.0.1",
    author="Akos Andras Nagy, Alexander Sutcliffe, Marius Wirtz",
    author_email="akos.nagy@knowledgeseed.ch",
    description="A package to simplify connecting to the TM1 REST API from Apache Airflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KnowledgeSeed/airflow-provider-tm1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["apache-airflow", "TM1py", ],
    tests_require=["pytest", ],
    extras_require={"devel": ["pre-commit"], },
    entry_points={
        "apache_airflow_provider": [
            "provider_info=airflow_provider_tm1.__init__:get_provider_info"
        ]
    },
)
