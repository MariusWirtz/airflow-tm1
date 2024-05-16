from contextlib import closing
from typing import Any, Dict
from TM1py.Services import TM1Service
from airflow.hooks.base import BaseHook


class TM1Hook(BaseHook):

    conn_name_attr = "tm1_conn_id"
    default_conn_name = "tm1_default"
    conn_type = "tm1"
    hook_name = "TM1"

    """
    Interact with IBM Cognos TM1, using the TM1py library.
    """

    def __init__(self, tm1_conn_id: str, **kwargs) -> None:
        """
        A hook that uses TM1py to connect to a TM1 database.
        :param tm1_conn_id: The name of the TM1 connection to use.
        :type tm1_conn_id: str
        """
        super().__init__(**kwargs)
        self.tm1_conn_id = tm1_conn_id
        self.tm1: TM1Service = None
        self.address = None
        self.port = None
        self.instance_name = None

    def get_conn(self) -> TM1Service:
        """
        Uses the connection details to create and return an instance of a TM1Service object.
        :return: TM1Service
        """
        conn = self.get_connection(self.tm1_conn_id)
        self.address = conn.host
        self.port = conn.port

        # check for relevant additional parameters in conn.extra
        # except session_id as not sure if this makes sense in an Airflow context
        extra_arg_names = [
            "base_url",
            "decode_b64",
            "namespace",
            "ssl",
            "session_context",
            "timeout",
            "connection_pool_size",
        ]
        extra_args = {
            name: val
            for name, val in conn.extra_dejson.items()
            if name in extra_arg_names
        }

        # Set a default for session context for easier identification in TM1top etc.
        if "session_context" not in extra_args:
            extra_args["session_context"] = "Airflow"

        self.tm1 = TM1Service(
            address=self.address,
            port=self.port,
            user=conn.login,
            password=conn.password,
            **extra_args
        )

        self.instance_name = self.tm1.server.get_server_name()

        return self.tm1
    

    def test_connection(self):
        status, message = False, ''
        try:
            tm1 = self.get_conn()
            status = tm1.connection.is_connected()
            message = 'Connection successfully tested'
        except Exception as e:
            status = False
            message = str(e)

        return status, message

 
    def logout(self):
        self.tm1.logout()
