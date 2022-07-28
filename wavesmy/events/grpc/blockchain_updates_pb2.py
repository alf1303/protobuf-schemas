# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wavesmy/events/grpc/blockchain_updates.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wavesmy.events import events_pb2 as wavesmy_dot_events_dot_events__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,wavesmy/events/grpc/blockchain_updates.proto\x12\x13wavesmy.events.grpc\x1a\x1bwavesmy/events/events.proto\"\'\n\x15GetBlockUpdateRequest\x12\x0e\n\x06height\x18\x01 \x01(\x05\"K\n\x16GetBlockUpdateResponse\x12\x31\n\x06update\x18\x01 \x01(\x0b\x32!.wavesmy.events.BlockchainUpdated\"E\n\x1bGetBlockUpdatesRangeRequest\x12\x13\n\x0b\x66rom_height\x18\x01 \x01(\x05\x12\x11\n\tto_height\x18\x02 \x01(\x05\"R\n\x1cGetBlockUpdatesRangeResponse\x12\x32\n\x07updates\x18\x01 \x03(\x0b\x32!.wavesmy.events.BlockchainUpdated\":\n\x10SubscribeRequest\x12\x13\n\x0b\x66rom_height\x18\x01 \x01(\x05\x12\x11\n\tto_height\x18\x02 \x01(\x05\"C\n\x0eSubscribeEvent\x12\x31\n\x06update\x18\x01 \x01(\x0b\x32!.wavesmy.events.BlockchainUpdated2\xd9\x02\n\x14\x42lockchainUpdatesApi\x12i\n\x0eGetBlockUpdate\x12*.wavesmy.events.grpc.GetBlockUpdateRequest\x1a+.wavesmy.events.grpc.GetBlockUpdateResponse\x12{\n\x14GetBlockUpdatesRange\x12\x30.wavesmy.events.grpc.GetBlockUpdatesRangeRequest\x1a\x31.wavesmy.events.grpc.GetBlockUpdatesRangeResponse\x12Y\n\tSubscribe\x12%.wavesmy.events.grpc.SubscribeRequest\x1a#.wavesmy.events.grpc.SubscribeEvent0\x01\x42\x89\x01\n*com.wavesplatform.events.api.grpc.protobufZGgithub.com/wavesplatform/gowaves/pkg/grpc/generated/wavesmy/events/grpc\xaa\x02\x11Waves.Events.Grpcb\x06proto3')



_GETBLOCKUPDATEREQUEST = DESCRIPTOR.message_types_by_name['GetBlockUpdateRequest']
_GETBLOCKUPDATERESPONSE = DESCRIPTOR.message_types_by_name['GetBlockUpdateResponse']
_GETBLOCKUPDATESRANGEREQUEST = DESCRIPTOR.message_types_by_name['GetBlockUpdatesRangeRequest']
_GETBLOCKUPDATESRANGERESPONSE = DESCRIPTOR.message_types_by_name['GetBlockUpdatesRangeResponse']
_SUBSCRIBEREQUEST = DESCRIPTOR.message_types_by_name['SubscribeRequest']
_SUBSCRIBEEVENT = DESCRIPTOR.message_types_by_name['SubscribeEvent']
GetBlockUpdateRequest = _reflection.GeneratedProtocolMessageType('GetBlockUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKUPDATEREQUEST,
  '__module__' : 'wavesmy.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.events.grpc.GetBlockUpdateRequest)
  })
_sym_db.RegisterMessage(GetBlockUpdateRequest)

GetBlockUpdateResponse = _reflection.GeneratedProtocolMessageType('GetBlockUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKUPDATERESPONSE,
  '__module__' : 'wavesmy.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.events.grpc.GetBlockUpdateResponse)
  })
_sym_db.RegisterMessage(GetBlockUpdateResponse)

GetBlockUpdatesRangeRequest = _reflection.GeneratedProtocolMessageType('GetBlockUpdatesRangeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKUPDATESRANGEREQUEST,
  '__module__' : 'wavesmy.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.events.grpc.GetBlockUpdatesRangeRequest)
  })
_sym_db.RegisterMessage(GetBlockUpdatesRangeRequest)

GetBlockUpdatesRangeResponse = _reflection.GeneratedProtocolMessageType('GetBlockUpdatesRangeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKUPDATESRANGERESPONSE,
  '__module__' : 'wavesmy.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.events.grpc.GetBlockUpdatesRangeResponse)
  })
_sym_db.RegisterMessage(GetBlockUpdatesRangeResponse)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'wavesmy.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.events.grpc.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

SubscribeEvent = _reflection.GeneratedProtocolMessageType('SubscribeEvent', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEEVENT,
  '__module__' : 'wavesmy.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.events.grpc.SubscribeEvent)
  })
_sym_db.RegisterMessage(SubscribeEvent)

_BLOCKCHAINUPDATESAPI = DESCRIPTOR.services_by_name['BlockchainUpdatesApi']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n*com.wavesplatform.events.api.grpc.protobufZGgithub.com/wavesplatform/gowaves/pkg/grpc/generated/wavesmy/events/grpc\252\002\021Waves.Events.Grpc'
  _GETBLOCKUPDATEREQUEST._serialized_start=98
  _GETBLOCKUPDATEREQUEST._serialized_end=137
  _GETBLOCKUPDATERESPONSE._serialized_start=139
  _GETBLOCKUPDATERESPONSE._serialized_end=214
  _GETBLOCKUPDATESRANGEREQUEST._serialized_start=216
  _GETBLOCKUPDATESRANGEREQUEST._serialized_end=285
  _GETBLOCKUPDATESRANGERESPONSE._serialized_start=287
  _GETBLOCKUPDATESRANGERESPONSE._serialized_end=369
  _SUBSCRIBEREQUEST._serialized_start=371
  _SUBSCRIBEREQUEST._serialized_end=429
  _SUBSCRIBEEVENT._serialized_start=431
  _SUBSCRIBEEVENT._serialized_end=498
  _BLOCKCHAINUPDATESAPI._serialized_start=501
  _BLOCKCHAINUPDATESAPI._serialized_end=846
# @@protoc_insertion_point(module_scope)
