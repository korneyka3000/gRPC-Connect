# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: question.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0equestion.proto\x12\x08question\"\x1f\n\x0fQuestionRequest\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\"\"\n\x10QuestionResponse\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t2L\n\x04Quiz\x12\x44\n\x0bGetQuestion\x12\x19.question.QuestionRequest\x1a\x1a.question.QuestionResponseb\x06proto3')



_QUESTIONREQUEST = DESCRIPTOR.message_types_by_name['QuestionRequest']
_QUESTIONRESPONSE = DESCRIPTOR.message_types_by_name['QuestionResponse']
QuestionRequest = _reflection.GeneratedProtocolMessageType('QuestionRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUESTIONREQUEST,
  '__module__' : 'question_pb2'
  # @@protoc_insertion_point(class_scope:question.QuestionRequest)
  })
_sym_db.RegisterMessage(QuestionRequest)

QuestionResponse = _reflection.GeneratedProtocolMessageType('QuestionResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUESTIONRESPONSE,
  '__module__' : 'question_pb2'
  # @@protoc_insertion_point(class_scope:question.QuestionResponse)
  })
_sym_db.RegisterMessage(QuestionResponse)

_QUIZ = DESCRIPTOR.services_by_name['Quiz']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUESTIONREQUEST._serialized_start=28
  _QUESTIONREQUEST._serialized_end=59
  _QUESTIONRESPONSE._serialized_start=61
  _QUESTIONRESPONSE._serialized_end=95
  _QUIZ._serialized_start=97
  _QUIZ._serialized_end=173
# @@protoc_insertion_point(module_scope)
