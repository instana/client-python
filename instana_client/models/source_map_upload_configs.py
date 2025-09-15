# coding: utf-8
from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Set
from typing_extensions import Self
from instana_client.models.source_map_upload_config import SourceMapUploadConfig

class SourceMapUploadConfigs(BaseModel):
    """
    SourceMapUploadConfigs
    """ # noqa: E501
    configs: List[SourceMapUploadConfig] = Field(alias="configs")
    __properties: ClassVar[List[str]] = ["configs"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SourceMapUploadConfigs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias."""
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceMapUploadConfigs from a dict"""
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate({
            "configs": obj.get("configs")
        })
        return _obj
