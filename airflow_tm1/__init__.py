## This is needed to allow Airflow to pick up specific metadata fields it needs for certain features. We recognize it's a bit unclean to define these in multiple places, but at this point it's the only workaround if you'd like your custom conn type to show up in the Airflow UI.
def get_provider_info():
    return {
        "package-name": "airflow-tm1",
        "name": "Airflow TM1",
        "description": "Apache Airflow Provider for TM1",
        'hooks': [{'integration-name': 'Apache Airflow Provider TM1', 'python-modules': ['airflow_tm1.hooks.tm1']}],
        'hook-class-names': ['airflow_tm1.hooks.tm1.TM1Hook'],
        'connection-types': [
            {'hook-class-name': 'airflow_tm1.hooks.tm1.TM1Hook', 'connection-type': 'tm1'}
        ], 
    }