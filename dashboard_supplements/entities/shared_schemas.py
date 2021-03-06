"""Reusable base schemas for utilization by the various entity schemas."""
from typing import Any

import marshmallow


class CamelCaseSchema(marshmallow.Schema):
    """A Schema that marshals data with camelcased keys."""

    def on_bind_field(self, field_name: str, field_obj: Any) -> None:
        """Camelize field keys."""
        field_obj.data_key = self.camelize(field_obj.data_key or field_name)

    @staticmethod
    def camelize(snake_str: str) -> str:
        """Convert snake_string to camelCase Format."""
        first, *others = snake_str.split("_")
        return "".join([first.lower(), *map(str.title, others)])
