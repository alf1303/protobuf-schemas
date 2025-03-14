# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wavesmy/node/grpc/transactions_api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wavesmy import recipient_pb2 as wavesmy_dot_recipient__pb2
from wavesmy import transaction_pb2 as wavesmy_dot_transaction__pb2
from wavesmy import invoke_script_result_pb2 as wavesmy_dot_invoke__script__result__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(wavesmy/node/grpc/transactions_api.proto\x12\x11wavesmy.node.grpc\x1a\x17wavesmy/recipient.proto\x1a\x19wavesmy/transaction.proto\x1a\"wavesmy/invoke_script_result.proto\"\xe8\x01\n\x11TransactionStatus\x12\n\n\x02id\x18\x01 \x01(\x0c\x12;\n\x06status\x18\x02 \x01(\x0e\x32+.wavesmy.node.grpc.TransactionStatus.Status\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12@\n\x12\x61pplication_status\x18\x04 \x01(\x0e\x32$.wavesmy.node.grpc.ApplicationStatus\"8\n\x06Status\x12\x0e\n\nNOT_EXISTS\x10\x00\x12\x0f\n\x0bUNCONFIRMED\x10\x01\x12\r\n\tCONFIRMED\x10\x02\"\xdf\x01\n\x13TransactionResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12/\n\x0btransaction\x18\x03 \x01(\x0b\x32\x1a.wavesmy.SignedTransaction\x12@\n\x12\x61pplication_status\x18\x04 \x01(\x0e\x32$.wavesmy.node.grpc.ApplicationStatus\x12\x39\n\x14invoke_script_result\x18\x05 \x01(\x0b\x32\x1b.wavesmy.InvokeScriptResult\"e\n\x13TransactionsRequest\x12\x0e\n\x06sender\x18\x01 \x01(\x0c\x12%\n\trecipient\x18\x02 \x01(\x0b\x32\x12.wavesmy.Recipient\x12\x17\n\x0ftransaction_ids\x18\x03 \x03(\x0c\"2\n\x17TransactionsByIdRequest\x12\x17\n\x0ftransaction_ids\x18\x03 \x03(\x0c\"8\n\x14\x43\x61lculateFeeResponse\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\"S\n\x0bSignRequest\x12)\n\x0btransaction\x18\x01 \x01(\x0b\x32\x14.wavesmy.Transaction\x12\x19\n\x11signer_public_key\x18\x02 \x01(\x0c\"z\n\x1aInvokeScriptResultResponse\x12/\n\x0btransaction\x18\x01 \x01(\x0b\x32\x1a.wavesmy.SignedTransaction\x12+\n\x06result\x18\x02 \x01(\x0b\x32\x1b.wavesmy.InvokeScriptResult*L\n\x11\x41pplicationStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\x1b\n\x17SCRIPT_EXECUTION_FAILED\x10\x02\x32\xb7\x04\n\x0fTransactionsApi\x12\x63\n\x0fGetTransactions\x12&.wavesmy.node.grpc.TransactionsRequest\x1a&.wavesmy.node.grpc.TransactionResponse0\x01\x12o\n\x0fGetStateChanges\x12&.wavesmy.node.grpc.TransactionsRequest\x1a-.wavesmy.node.grpc.InvokeScriptResultResponse\"\x03\x88\x02\x01\x30\x01\x12\x61\n\x0bGetStatuses\x12*.wavesmy.node.grpc.TransactionsByIdRequest\x1a$.wavesmy.node.grpc.TransactionStatus0\x01\x12\x62\n\x0eGetUnconfirmed\x12&.wavesmy.node.grpc.TransactionsRequest\x1a&.wavesmy.node.grpc.TransactionResponse0\x01\x12\x42\n\x04Sign\x12\x1e.wavesmy.node.grpc.SignRequest\x1a\x1a.wavesmy.SignedTransaction\x12\x43\n\tBroadcast\x12\x1a.wavesmy.SignedTransaction\x1a\x1a.wavesmy.SignedTransactionBu\n\x1a\x63om.wavesplatform.api.grpcZEgithub.com/wavesplatform/gowaves/pkg/grpc/generated/wavesmy/node/grpc\xaa\x02\x0fWaves.Node.Grpcb\x06proto3')

_APPLICATIONSTATUS = DESCRIPTOR.enum_types_by_name['ApplicationStatus']
ApplicationStatus = enum_type_wrapper.EnumTypeWrapper(_APPLICATIONSTATUS)
UNKNOWN = 0
SUCCEEDED = 1
SCRIPT_EXECUTION_FAILED = 2


_TRANSACTIONSTATUS = DESCRIPTOR.message_types_by_name['TransactionStatus']
_TRANSACTIONRESPONSE = DESCRIPTOR.message_types_by_name['TransactionResponse']
_TRANSACTIONSREQUEST = DESCRIPTOR.message_types_by_name['TransactionsRequest']
_TRANSACTIONSBYIDREQUEST = DESCRIPTOR.message_types_by_name['TransactionsByIdRequest']
_CALCULATEFEERESPONSE = DESCRIPTOR.message_types_by_name['CalculateFeeResponse']
_SIGNREQUEST = DESCRIPTOR.message_types_by_name['SignRequest']
_INVOKESCRIPTRESULTRESPONSE = DESCRIPTOR.message_types_by_name['InvokeScriptResultResponse']
_TRANSACTIONSTATUS_STATUS = _TRANSACTIONSTATUS.enum_types_by_name['Status']
TransactionStatus = _reflection.GeneratedProtocolMessageType('TransactionStatus', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONSTATUS,
  '__module__' : 'wavesmy.node.grpc.transactions_api_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.node.grpc.TransactionStatus)
  })
_sym_db.RegisterMessage(TransactionStatus)

TransactionResponse = _reflection.GeneratedProtocolMessageType('TransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONRESPONSE,
  '__module__' : 'wavesmy.node.grpc.transactions_api_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.node.grpc.TransactionResponse)
  })
_sym_db.RegisterMessage(TransactionResponse)

TransactionsRequest = _reflection.GeneratedProtocolMessageType('TransactionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONSREQUEST,
  '__module__' : 'wavesmy.node.grpc.transactions_api_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.node.grpc.TransactionsRequest)
  })
_sym_db.RegisterMessage(TransactionsRequest)

TransactionsByIdRequest = _reflection.GeneratedProtocolMessageType('TransactionsByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONSBYIDREQUEST,
  '__module__' : 'wavesmy.node.grpc.transactions_api_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.node.grpc.TransactionsByIdRequest)
  })
_sym_db.RegisterMessage(TransactionsByIdRequest)

CalculateFeeResponse = _reflection.GeneratedProtocolMessageType('CalculateFeeResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATEFEERESPONSE,
  '__module__' : 'wavesmy.node.grpc.transactions_api_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.node.grpc.CalculateFeeResponse)
  })
_sym_db.RegisterMessage(CalculateFeeResponse)

SignRequest = _reflection.GeneratedProtocolMessageType('SignRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNREQUEST,
  '__module__' : 'wavesmy.node.grpc.transactions_api_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.node.grpc.SignRequest)
  })
_sym_db.RegisterMessage(SignRequest)

InvokeScriptResultResponse = _reflection.GeneratedProtocolMessageType('InvokeScriptResultResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVOKESCRIPTRESULTRESPONSE,
  '__module__' : 'wavesmy.node.grpc.transactions_api_pb2'
  # @@protoc_insertion_point(class_scope:wavesmy.node.grpc.InvokeScriptResultResponse)
  })
_sym_db.RegisterMessage(InvokeScriptResultResponse)

_TRANSACTIONSAPI = DESCRIPTOR.services_by_name['TransactionsApi']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.wavesplatform.api.grpcZEgithub.com/wavesplatform/gowaves/pkg/grpc/generated/wavesmy/node/grpc\252\002\017Waves.Node.Grpc'
  _TRANSACTIONSAPI.methods_by_name['GetStateChanges']._options = None
  _TRANSACTIONSAPI.methods_by_name['GetStateChanges']._serialized_options = b'\210\002\001'
  _APPLICATIONSTATUS._serialized_start=1034
  _APPLICATIONSTATUS._serialized_end=1110
  _TRANSACTIONSTATUS._serialized_start=152
  _TRANSACTIONSTATUS._serialized_end=384
  _TRANSACTIONSTATUS_STATUS._serialized_start=328
  _TRANSACTIONSTATUS_STATUS._serialized_end=384
  _TRANSACTIONRESPONSE._serialized_start=387
  _TRANSACTIONRESPONSE._serialized_end=610
  _TRANSACTIONSREQUEST._serialized_start=612
  _TRANSACTIONSREQUEST._serialized_end=713
  _TRANSACTIONSBYIDREQUEST._serialized_start=715
  _TRANSACTIONSBYIDREQUEST._serialized_end=765
  _CALCULATEFEERESPONSE._serialized_start=767
  _CALCULATEFEERESPONSE._serialized_end=823
  _SIGNREQUEST._serialized_start=825
  _SIGNREQUEST._serialized_end=908
  _INVOKESCRIPTRESULTRESPONSE._serialized_start=910
  _INVOKESCRIPTRESULTRESPONSE._serialized_end=1032
  _TRANSACTIONSAPI._serialized_start=1113
  _TRANSACTIONSAPI._serialized_end=1680
# @@protoc_insertion_point(module_scope)
