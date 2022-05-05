# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jobs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\njobs.proto\x12\x04jobs\"f\n\x0bJobResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x1a\n\x05level\x18\x03 \x01(\x0e\x32\x0b.jobs.Level\x12\x0e\n\x06salary\x18\x04 \x01(\x01\x12\x10\n\x08location\x18\x05 \x01(\t\"\x1b\n\nJobRequest\x12\r\n\x05title\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"H\n\x06\x41\x64\x64Job\x12\r\n\x05title\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\t\x12\x0e\n\x06salary\x18\x03 \x01(\x01\x12\x10\n\x08location\x18\x04 \x01(\t*+\n\x05Level\x12\n\n\x06Junior\x10\x00\x12\n\n\x06Middle\x10\x01\x12\n\n\x06Senior\x10\x03\x32\x97\x01\n\nJobService\x12\x30\n\x07GetJobs\x12\x10.jobs.JobRequest\x1a\x11.jobs.JobResponse0\x01\x12/\n\x0bGetListJobs\x12\x0b.jobs.Empty\x1a\x11.jobs.JobResponse0\x01\x12&\n\tCreateJob\x12\x0c.jobs.AddJob\x1a\x0b.jobs.Emptyb\x06proto3')

_LEVEL = DESCRIPTOR.enum_types_by_name['Level']
Level = enum_type_wrapper.EnumTypeWrapper(_LEVEL)
Junior = 0
Middle = 1
Senior = 3


_JOBRESPONSE = DESCRIPTOR.message_types_by_name['JobResponse']
_JOBREQUEST = DESCRIPTOR.message_types_by_name['JobRequest']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_ADDJOB = DESCRIPTOR.message_types_by_name['AddJob']
JobResponse = _reflection.GeneratedProtocolMessageType('JobResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOBRESPONSE,
  '__module__' : 'jobs_pb2'
  # @@protoc_insertion_point(class_scope:jobs.JobResponse)
  })
_sym_db.RegisterMessage(JobResponse)

JobRequest = _reflection.GeneratedProtocolMessageType('JobRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOBREQUEST,
  '__module__' : 'jobs_pb2'
  # @@protoc_insertion_point(class_scope:jobs.JobRequest)
  })
_sym_db.RegisterMessage(JobRequest)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'jobs_pb2'
  # @@protoc_insertion_point(class_scope:jobs.Empty)
  })
_sym_db.RegisterMessage(Empty)

AddJob = _reflection.GeneratedProtocolMessageType('AddJob', (_message.Message,), {
  'DESCRIPTOR' : _ADDJOB,
  '__module__' : 'jobs_pb2'
  # @@protoc_insertion_point(class_scope:jobs.AddJob)
  })
_sym_db.RegisterMessage(AddJob)

_JOBSERVICE = DESCRIPTOR.services_by_name['JobService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LEVEL._serialized_start=236
  _LEVEL._serialized_end=279
  _JOBRESPONSE._serialized_start=20
  _JOBRESPONSE._serialized_end=122
  _JOBREQUEST._serialized_start=124
  _JOBREQUEST._serialized_end=151
  _EMPTY._serialized_start=153
  _EMPTY._serialized_end=160
  _ADDJOB._serialized_start=162
  _ADDJOB._serialized_end=234
  _JOBSERVICE._serialized_start=282
  _JOBSERVICE._serialized_end=433
# @@protoc_insertion_point(module_scope)
