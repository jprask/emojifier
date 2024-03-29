# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: emojifier.proto

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
  name='emojifier.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x65mojifier.proto\")\n\tToEmojify\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65gree\x18\x02 \x01(\x05\"\x1d\n\tEmojified\x12\x10\n\x08response\x18\x01 \x01(\t\"(\n\tWordEmoji\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\r\n\x05\x65moji\x18\x02 \x01(\t22\n\tEmojifier\x12%\n\x07\x45mojify\x12\n.ToEmojify\x1a\n.Emojified(\x01\x30\x01\x32,\n\x0b\x45mojiGetter\x12\x1d\n\x03Get\x12\n.ToEmojify\x1a\n.WordEmojib\x06proto3')
)




_TOEMOJIFY = _descriptor.Descriptor(
  name='ToEmojify',
  full_name='ToEmojify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='ToEmojify.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='degree', full_name='ToEmojify.degree', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=60,
)


_EMOJIFIED = _descriptor.Descriptor(
  name='Emojified',
  full_name='Emojified',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='Emojified.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=91,
)


_WORDEMOJI = _descriptor.Descriptor(
  name='WordEmoji',
  full_name='WordEmoji',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='WordEmoji.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emoji', full_name='WordEmoji.emoji', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=133,
)

DESCRIPTOR.message_types_by_name['ToEmojify'] = _TOEMOJIFY
DESCRIPTOR.message_types_by_name['Emojified'] = _EMOJIFIED
DESCRIPTOR.message_types_by_name['WordEmoji'] = _WORDEMOJI
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ToEmojify = _reflection.GeneratedProtocolMessageType('ToEmojify', (_message.Message,), dict(
  DESCRIPTOR = _TOEMOJIFY,
  __module__ = 'emojifier_pb2'
  # @@protoc_insertion_point(class_scope:ToEmojify)
  ))
_sym_db.RegisterMessage(ToEmojify)

Emojified = _reflection.GeneratedProtocolMessageType('Emojified', (_message.Message,), dict(
  DESCRIPTOR = _EMOJIFIED,
  __module__ = 'emojifier_pb2'
  # @@protoc_insertion_point(class_scope:Emojified)
  ))
_sym_db.RegisterMessage(Emojified)

WordEmoji = _reflection.GeneratedProtocolMessageType('WordEmoji', (_message.Message,), dict(
  DESCRIPTOR = _WORDEMOJI,
  __module__ = 'emojifier_pb2'
  # @@protoc_insertion_point(class_scope:WordEmoji)
  ))
_sym_db.RegisterMessage(WordEmoji)



_EMOJIFIER = _descriptor.ServiceDescriptor(
  name='Emojifier',
  full_name='Emojifier',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=135,
  serialized_end=185,
  methods=[
  _descriptor.MethodDescriptor(
    name='Emojify',
    full_name='Emojifier.Emojify',
    index=0,
    containing_service=None,
    input_type=_TOEMOJIFY,
    output_type=_EMOJIFIED,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EMOJIFIER)

DESCRIPTOR.services_by_name['Emojifier'] = _EMOJIFIER


_EMOJIGETTER = _descriptor.ServiceDescriptor(
  name='EmojiGetter',
  full_name='EmojiGetter',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=187,
  serialized_end=231,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='EmojiGetter.Get',
    index=0,
    containing_service=None,
    input_type=_TOEMOJIFY,
    output_type=_WORDEMOJI,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EMOJIGETTER)

DESCRIPTOR.services_by_name['EmojiGetter'] = _EMOJIGETTER

# @@protoc_insertion_point(module_scope)
