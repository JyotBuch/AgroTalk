# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/appengine_v1alpha/proto/domain.proto

from cloudsdk.google.protobuf import descriptor as _descriptor
from cloudsdk.google.protobuf import message as _message
from cloudsdk.google.protobuf import reflection as _reflection
from cloudsdk.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/appengine_v1alpha/proto/domain.proto',
  package='google.appengine.v1alpha',
  syntax='proto3',
  serialized_options=b'\n\034com.google.appengine.v1alphaB\013DomainProtoP\001ZAgoogle.golang.org/genproto/googleapis/appengine/v1alpha;appengine',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1google/cloud/appengine_v1alpha/proto/domain.proto\x12\x18google.appengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\",\n\x10\x41uthorizedDomain\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\tBp\n\x1c\x63om.google.appengine.v1alphaB\x0b\x44omainProtoP\x01ZAgoogle.golang.org/genproto/googleapis/appengine/v1alpha;appengineb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_AUTHORIZEDDOMAIN = _descriptor.Descriptor(
  name='AuthorizedDomain',
  full_name='google.appengine.v1alpha.AuthorizedDomain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.appengine.v1alpha.AuthorizedDomain.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.appengine.v1alpha.AuthorizedDomain.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=153,
)

DESCRIPTOR.message_types_by_name['AuthorizedDomain'] = _AUTHORIZEDDOMAIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthorizedDomain = _reflection.GeneratedProtocolMessageType('AuthorizedDomain', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZEDDOMAIN,
  '__module__' : 'google.cloud.appengine_v1alpha.proto.domain_pb2'
  ,
  '__doc__': """A domain that a user has been authorized to administer. To authorize
  use of a domain, verify ownership via `Webmaster Central
  <https://www.google.com/webmasters/verification/home>`__.
  
  Attributes:
      name:
          Full path to the ``AuthorizedDomain`` resource in the API.
          Example: ``apps/myapp/authorizedDomains/example.com``.
          @OutputOnly
      id:
          Fully qualified domain name of the domain authorized for use.
          Example: ``example.com``.
  """,
  # @@protoc_insertion_point(class_scope:google.appengine.v1alpha.AuthorizedDomain)
  })
_sym_db.RegisterMessage(AuthorizedDomain)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
