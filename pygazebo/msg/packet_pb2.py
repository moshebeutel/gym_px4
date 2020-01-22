# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: packet.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import time_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='packet.proto',
  package='gazebo.msgs',
  serialized_pb=_b('\n\x0cpacket.proto\x12\x0bgazebo.msgs\x1a\ntime.proto\"Q\n\x06Packet\x12 \n\x05stamp\x18\x01 \x02(\x0b\x32\x11.gazebo.msgs.Time\x12\x0c\n\x04type\x18\x02 \x02(\t\x12\x17\n\x0fserialized_data\x18\x03 \x02(\x0c')
  ,
  dependencies=[time_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PACKET = _descriptor.Descriptor(
  name='Packet',
  full_name='gazebo.msgs.Packet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stamp', full_name='gazebo.msgs.Packet.stamp', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='gazebo.msgs.Packet.type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serialized_data', full_name='gazebo.msgs.Packet.serialized_data', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=122,
)

_PACKET.fields_by_name['stamp'].message_type = time_pb2._TIME
DESCRIPTOR.message_types_by_name['Packet'] = _PACKET

Packet = _reflection.GeneratedProtocolMessageType('Packet', (_message.Message,), dict(
  DESCRIPTOR = _PACKET,
  __module__ = 'packet_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Packet)
  ))
_sym_db.RegisterMessage(Packet)


# @@protoc_insertion_point(module_scope)
