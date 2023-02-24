from typing import ClassVar as _ClassVar
from typing import List

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper


DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
DESCRIPTOR: _descriptor.FileDescriptor
ENUM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
ENUM_VALUE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
METHOD_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
SERVICE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
SERVICE_EXECUTION_SITE_FIELD_NUMBER: _ClassVar[int]
description: _descriptor.FieldDescriptor
enum_description: _descriptor.FieldDescriptor
enum_value_description: _descriptor.FieldDescriptor
k_EProtoExecutionSiteSteamClient: EProtoExecutionSite
k_EProtoExecutionSiteUnknown: EProtoExecutionSite
method_description: _descriptor.FieldDescriptor
service_description: _descriptor.FieldDescriptor
service_execution_site: _descriptor.FieldDescriptor

class NoResponse(_message.Message):
    __slots__: List[str] = []
    def __init__(self) -> None: ...

class EProtoExecutionSite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []
