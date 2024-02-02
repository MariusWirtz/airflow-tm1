import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="airflow-tm1",
    version="0.0.9",
    author="Alexander Sutcliffe",
    author_email="sutcliffe.alex@gmail.com",
    description="A package to simplify connecting to the TM1 REST API from Apache Airflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scrambldchannel/airflow-tm1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["apache-airflow", "TM1py", ],
    tests_require=["pytest", ],
    extras_require={"devel": ["pre-commit"], },
    entry_points={
        "apache_airflow_provider": [
            "provider_info=airflow_tm1.__init__:get_provider_info"
        ]
    },
)
