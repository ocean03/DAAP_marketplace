# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: marketplace_processor/protobuf/rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='marketplace_processor/protobuf/rule.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n)marketplace_processor/protobuf/rule.proto\"\xe7\x02\n\x04Rule\x12\x1c\n\x04type\x18\x01 \x01(\x0e\x32\x0e.Rule.RuleType\x12\r\n\x05value\x18\x02 \x01(\x0c\"\xb1\x02\n\x08RuleType\x12\x0e\n\nRULE_UNSET\x10\x00\x12\x1b\n\x17OWNER_HOLDINGS_INFINITE\x10\x64\x12\x19\n\x15\x41LL_HOLDINGS_INFINITE\x10\x65\x12\x14\n\x10NOT_TRANSFERABLE\x10\x66\x12\x18\n\x14REQUIRE_SOURCE_TYPES\x10g\x12\x18\n\x14REQUIRE_TARGET_TYPES\x10h\x12\x1d\n\x19REQUIRE_SOURCE_QUANTITIES\x10i\x12\x1d\n\x19REQUIRE_TARGET_QUANTITIES\x10j\x12\x12\n\rEXCHANGE_ONCE\x10\xc8\x01\x12\x1e\n\x19\x45XCHANGE_ONCE_PER_ACCOUNT\x10\xc9\x01\x12!\n\x1c\x45XCHANGE_LIMITED_TO_ACCOUNTS\x10\xca\x01\x62\x06proto3')
)



_RULE_RULETYPE = _descriptor.EnumDescriptor(
  name='RuleType',
  full_name='Rule.RuleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RULE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OWNER_HOLDINGS_INFINITE', index=1, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALL_HOLDINGS_INFINITE', index=2, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_TRANSFERABLE', index=3, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUIRE_SOURCE_TYPES', index=4, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUIRE_TARGET_TYPES', index=5, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUIRE_SOURCE_QUANTITIES', index=6, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUIRE_TARGET_QUANTITIES', index=7, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCHANGE_ONCE', index=8, number=200,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCHANGE_ONCE_PER_ACCOUNT', index=9, number=201,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCHANGE_LIMITED_TO_ACCOUNTS', index=10, number=202,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=100,
  serialized_end=405,
)
_sym_db.RegisterEnumDescriptor(_RULE_RULETYPE)


_RULE = _descriptor.Descriptor(
  name='Rule',
  full_name='Rule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Rule.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Rule.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RULE_RULETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=405,
)

_RULE.fields_by_name['type'].enum_type = _RULE_RULETYPE
_RULE_RULETYPE.containing_type = _RULE
DESCRIPTOR.message_types_by_name['Rule'] = _RULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Rule = _reflection.GeneratedProtocolMessageType('Rule', (_message.Message,), dict(
  DESCRIPTOR = _RULE,
  __module__ = 'marketplace_processor.protobuf.rule_pb2'
  # @@protoc_insertion_point(class_scope:Rule)
  ))
_sym_db.RegisterMessage(Rule)


# @@protoc_insertion_point(module_scope)
