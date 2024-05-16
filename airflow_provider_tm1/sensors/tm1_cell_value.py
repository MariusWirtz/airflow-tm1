from operator import eq, ge, gt, le, lt, ne
from typing import Dict, Optional, Union

from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

from airflow_tm1.hooks.tm1 import TM1Hook


class TM1CellValueSensor(BaseSensorOperator):
    """
    Checks the value of a single cell in a TM1 cube.
    """

    template_fields = ("cube", "elements")
    ui_color = "#f0eee4"

    @apply_defaults
    def __init__(
        self,
        cube: str,
        elements: str,
        tm1_conn_id: str,
        value: Union[str, float],
        op=eq,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.tm1_conn_id = tm1_conn_id
        self.cube = cube
        self.elements = elements
        self.op = op
        self.value = value

    def poke(self, context: Dict) -> bool:

        tm1_hook = TM1Hook(tm1_conn_id=self.tm1_conn_id)

        tm1 = tm1_hook.get_conn()

        return self.op(tm1.data.get_value(cube_name=self.cube, element_string=self.elements), self.value)
