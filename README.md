# airflow-tm1

A package that provides a hook to simplify connecting to the IBM Cognos TM1 / Planning Analytics REST API.

## Requirements

* Python 3.6+
* Airflow
* TM1py

## Development

```
python -m venv .env
source .env/Scripts/activate
python -m pip install -r requirements.txt
python setup.py bdist_wheel
```

## Installation

Install with pip `pip install airflow-tm1`

## Usage

Create a connection in Airflow with at least the following parameters set:

* Host
* Login
* Port
* Extras
  * ssl

Any other parameter accepted by the TM1py RestService constructor (eg base_url, namespace etc) can also be added as a key in the Extras field in the connection.

In your DAG file:

```python
from airflow_tm1.hooks.tm1 import TM1Hook

tm1_hook = TM1Hook(tm1_conn_id="tm1_default")
tm1 = tm1_hook.get_conn()
```

This will attempt to connect to the TM1 server using the details provided and initialise an instance of the TM1Service class than be accessed at `tm1_hook.tm1`

See [TM1py](https://github.com/cubewise-code/tm1py) for more details.

## License

See [LICENSE](https://github.com/scrambldchannel/airflow-tm1/LICENSE)



