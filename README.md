# airflow-providers-tm1

A package by Knowledgeseed and Cubewise that provides a hook to simplify connecting to the IBM Cognos TM1 / Planning Analytics REST API.

https://github.com/KnowledgeSeed/airflow-providers-tm1

This repository is a fork of https://github.com/MariusWirtz/airflow-tm1 and https://github.com/scrambldchannel/airflow-tm1 which offer only Airflow 1.x compatibility.

The fork upgrades the provider to ensure Airflow 2.x compatibility. Some parts and have been reused from https://github.com/scrambldchannel/airflow-provider-tm1.

## Requirements

* Python 3.7+
* Airflow 2.2+
* TM1py 1.4.1+

## Development

```
python -m venv .env
source .env/bin/activate
python -m pip install -r requirements.txt
python -m build
```

## Installation

Install with pip `pip install airflow-providers-tm1`

## Usage

Create a connection in Airflow with at least the following parameters set:

* Host
* Login
* Port
* Extras
  * ssl

Any other parameter accepted by the TM1py RestService constructor (eg base_url, namespace etc) can also be added as a key in the Extras field in the connection.

![airflow_tm1_conn](docs/airflow_tm1_conn.png)

In your DAG file:

```python
from airflow_tm1.hooks.tm1 import TM1Hook

tm1_hook = TM1Hook(tm1_conn_id="tm1_default")
tm1 = tm1_hook.get_conn()
```

This will attempt to connect to the TM1 server using the details provided and initialise an instance of the TM1Service class than be accessed at `tm1_hook.tm1`

See [TM1py](https://github.com/cubewise-code/tm1py) for more details.

## Manual integration testing

Use `tests_integration/docker-compose.yaml` as a baseline, which spins up an Airflow including the TM1 provider and a base TM1 database to test against. Please note that `tm1-docker` image is properietary IBM product wrapped in Docker by Knowledgeseed and therefore it is only available internally for Knowledgeseed developers.

To obtain a licensed IBM TM1 database for testing or production purpose, please see https://www.ibm.com/topics/tm1 for further details.

## License

See [LICENSE](https://github.com/scrambldchannel/airflow-tm1/LICENSE)



