# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/api/tenant.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63hirpstack-api/api/tenant.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x95\x02\n\x06Tenant\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x19\n\x11\x63\x61n_have_gateways\x18\x04 \x01(\x08\x12\x19\n\x11max_gateway_count\x18\x05 \x01(\r\x12\x18\n\x10max_device_count\x18\x06 \x01(\r\x12\x1b\n\x13private_gateways_up\x18\x07 \x01(\x08\x12\x1d\n\x15private_gateways_down\x18\x08 \x01(\x08\x12#\n\x04tags\x18\t \x03(\x0b\x32\x15.api.Tenant.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x96\x02\n\x0eTenantListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x19\n\x11\x63\x61n_have_gateways\x18\x05 \x01(\x08\x12\x1b\n\x13private_gateways_up\x18\x06 \x01(\x08\x12\x1d\n\x15private_gateways_down\x18\t \x01(\x08\x12\x19\n\x11max_gateway_count\x18\x07 \x01(\r\x12\x18\n\x10max_device_count\x18\x08 \x01(\r\"2\n\x13\x43reateTenantRequest\x12\x1b\n\x06tenant\x18\x01 \x01(\x0b\x32\x0b.api.Tenant\"\"\n\x14\x43reateTenantResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x1e\n\x10GetTenantRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x90\x01\n\x11GetTenantResponse\x12\x1b\n\x06tenant\x18\x01 \x01(\x0b\x32\x0b.api.Tenant\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"2\n\x13UpdateTenantRequest\x12\x1b\n\x06tenant\x18\x01 \x01(\x0b\x32\x0b.api.Tenant\"!\n\x13\x44\x65leteTenantRequest\x12\n\n\x02id\x18\x01 \x01(\t\"T\n\x12ListTenantsRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0e\n\x06search\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\"O\n\x13ListTenantsResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\r\x12#\n\x06result\x18\x02 \x03(\x0b\x32\x13.api.TenantListItem\"\x84\x01\n\nTenantUser\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x10\n\x08is_admin\x18\x03 \x01(\x08\x12\x17\n\x0fis_device_admin\x18\x04 \x01(\x08\x12\x18\n\x10is_gateway_admin\x18\x05 \x01(\x08\x12\r\n\x05\x65mail\x18\x06 \x01(\t\"\xec\x01\n\x12TenantUserListItem\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x10\n\x08is_admin\x18\x06 \x01(\x08\x12\x17\n\x0fis_device_admin\x18\x07 \x01(\x08\x12\x18\n\x10is_gateway_admin\x18\x08 \x01(\x08\"<\n\x14\x41\x64\x64TenantUserRequest\x12$\n\x0btenant_user\x18\x01 \x01(\x0b\x32\x0f.api.TenantUser\":\n\x14GetTenantUserRequest\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"\x9d\x01\n\x15GetTenantUserResponse\x12$\n\x0btenant_user\x18\x01 \x01(\x0b\x32\x0f.api.TenantUser\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"?\n\x17UpdateTenantUserRequest\x12$\n\x0btenant_user\x18\x01 \x01(\x0b\x32\x0f.api.TenantUser\"=\n\x17\x44\x65leteTenantUserRequest\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"J\n\x16ListTenantUsersRequest\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\r\x12\x0e\n\x06offset\x18\x03 \x01(\r\"W\n\x17ListTenantUsersResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\r\x12\'\n\x06result\x18\x02 \x03(\x0b\x32\x17.api.TenantUserListItem2\xa2\x08\n\rTenantService\x12V\n\x06\x43reate\x12\x18.api.CreateTenantRequest\x1a\x19.api.CreateTenantResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/api/tenants:\x01*\x12O\n\x03Get\x12\x15.api.GetTenantRequest\x1a\x16.api.GetTenantResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/api/tenants/{id}\x12_\n\x06Update\x12\x18.api.UpdateTenantRequest\x1a\x16.google.protobuf.Empty\"#\x82\xd3\xe4\x93\x02\x1d\x1a\x18/api/tenants/{tenant.id}:\x01*\x12U\n\x06\x44\x65lete\x12\x18.api.DeleteTenantRequest\x1a\x16.google.protobuf.Empty\"\x19\x82\xd3\xe4\x93\x02\x13*\x11/api/tenants/{id}\x12O\n\x04List\x12\x17.api.ListTenantsRequest\x1a\x18.api.ListTenantsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/api/tenants\x12s\n\x07\x41\x64\x64User\x12\x19.api.AddTenantUserRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02/\"*/api/tenants/{tenant_user.tenant_id}/users:\x01*\x12r\n\x07GetUser\x12\x19.api.GetTenantUserRequest\x1a\x1a.api.GetTenantUserResponse\"0\x82\xd3\xe4\x93\x02*\x12(/api/tenants/{tenant_id}/users/{user_id}\x12\x8f\x01\n\nUpdateUser\x12\x1c.api.UpdateTenantUserRequest\x1a\x16.google.protobuf.Empty\"K\x82\xd3\xe4\x93\x02\x45\x1a@/api/tenants/{tenant_user.tenant_id}/users/{tenant_user.user_id}:\x01*\x12t\n\nDeleteUser\x12\x1c.api.DeleteTenantUserRequest\x1a\x16.google.protobuf.Empty\"0\x82\xd3\xe4\x93\x02**(/api/tenants/{tenant_id}/users/{user_id}\x12n\n\tListUsers\x12\x1b.api.ListTenantUsersRequest\x1a\x1c.api.ListTenantUsersResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/api/tenants/{tenant_id}/usersBc\n\x11io.chirpstack.apiB\x0bTenantProtoP\x01Z.github.com/chirpstack/chirpstack/api/go/v4/api\xaa\x02\x0e\x43hirpstack.Apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.api.tenant_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021io.chirpstack.apiB\013TenantProtoP\001Z.github.com/chirpstack/chirpstack/api/go/v4/api\252\002\016Chirpstack.Api'
  _globals['_TENANT_TAGSENTRY']._options = None
  _globals['_TENANT_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_TENANTSERVICE'].methods_by_name['Create']._options = None
  _globals['_TENANTSERVICE'].methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\021\"\014/api/tenants:\001*'
  _globals['_TENANTSERVICE'].methods_by_name['Get']._options = None
  _globals['_TENANTSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\023\022\021/api/tenants/{id}'
  _globals['_TENANTSERVICE'].methods_by_name['Update']._options = None
  _globals['_TENANTSERVICE'].methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\035\032\030/api/tenants/{tenant.id}:\001*'
  _globals['_TENANTSERVICE'].methods_by_name['Delete']._options = None
  _globals['_TENANTSERVICE'].methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\023*\021/api/tenants/{id}'
  _globals['_TENANTSERVICE'].methods_by_name['List']._options = None
  _globals['_TENANTSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\016\022\014/api/tenants'
  _globals['_TENANTSERVICE'].methods_by_name['AddUser']._options = None
  _globals['_TENANTSERVICE'].methods_by_name['AddUser']._serialized_options = b'\202\323\344\223\002/\"*/api/tenants/{tenant_user.tenant_id}/users:\001*'
  _globals['_TENANTSERVICE'].methods_by_name['GetUser']._options = None
  _globals['_TENANTSERVICE'].methods_by_name['GetUser']._serialized_options = b'\202\323\344\223\002*\022(/api/tenants/{tenant_id}/users/{user_id}'
  _globals['_TENANTSERVICE'].methods_by_name['UpdateUser']._options = None
  _globals['_TENANTSERVICE'].methods_by_name['UpdateUser']._serialized_options = b'\202\323\344\223\002E\032@/api/tenants/{tenant_user.tenant_id}/users/{tenant_user.user_id}:\001*'
  _globals['_TENANTSERVICE'].methods_by_name['DeleteUser']._options = None
  _globals['_TENANTSERVICE'].methods_by_name['DeleteUser']._serialized_options = b'\202\323\344\223\002**(/api/tenants/{tenant_id}/users/{user_id}'
  _globals['_TENANTSERVICE'].methods_by_name['ListUsers']._options = None
  _globals['_TENANTSERVICE'].methods_by_name['ListUsers']._serialized_options = b'\202\323\344\223\002 \022\036/api/tenants/{tenant_id}/users'
  _globals['_TENANT']._serialized_start=133
  _globals['_TENANT']._serialized_end=410
  _globals['_TENANT_TAGSENTRY']._serialized_start=367
  _globals['_TENANT_TAGSENTRY']._serialized_end=410
  _globals['_TENANTLISTITEM']._serialized_start=413
  _globals['_TENANTLISTITEM']._serialized_end=691
  _globals['_CREATETENANTREQUEST']._serialized_start=693
  _globals['_CREATETENANTREQUEST']._serialized_end=743
  _globals['_CREATETENANTRESPONSE']._serialized_start=745
  _globals['_CREATETENANTRESPONSE']._serialized_end=779
  _globals['_GETTENANTREQUEST']._serialized_start=781
  _globals['_GETTENANTREQUEST']._serialized_end=811
  _globals['_GETTENANTRESPONSE']._serialized_start=814
  _globals['_GETTENANTRESPONSE']._serialized_end=958
  _globals['_UPDATETENANTREQUEST']._serialized_start=960
  _globals['_UPDATETENANTREQUEST']._serialized_end=1010
  _globals['_DELETETENANTREQUEST']._serialized_start=1012
  _globals['_DELETETENANTREQUEST']._serialized_end=1045
  _globals['_LISTTENANTSREQUEST']._serialized_start=1047
  _globals['_LISTTENANTSREQUEST']._serialized_end=1131
  _globals['_LISTTENANTSRESPONSE']._serialized_start=1133
  _globals['_LISTTENANTSRESPONSE']._serialized_end=1212
  _globals['_TENANTUSER']._serialized_start=1215
  _globals['_TENANTUSER']._serialized_end=1347
  _globals['_TENANTUSERLISTITEM']._serialized_start=1350
  _globals['_TENANTUSERLISTITEM']._serialized_end=1586
  _globals['_ADDTENANTUSERREQUEST']._serialized_start=1588
  _globals['_ADDTENANTUSERREQUEST']._serialized_end=1648
  _globals['_GETTENANTUSERREQUEST']._serialized_start=1650
  _globals['_GETTENANTUSERREQUEST']._serialized_end=1708
  _globals['_GETTENANTUSERRESPONSE']._serialized_start=1711
  _globals['_GETTENANTUSERRESPONSE']._serialized_end=1868
  _globals['_UPDATETENANTUSERREQUEST']._serialized_start=1870
  _globals['_UPDATETENANTUSERREQUEST']._serialized_end=1933
  _globals['_DELETETENANTUSERREQUEST']._serialized_start=1935
  _globals['_DELETETENANTUSERREQUEST']._serialized_end=1996
  _globals['_LISTTENANTUSERSREQUEST']._serialized_start=1998
  _globals['_LISTTENANTUSERSREQUEST']._serialized_end=2072
  _globals['_LISTTENANTUSERSRESPONSE']._serialized_start=2074
  _globals['_LISTTENANTUSERSRESPONSE']._serialized_end=2161
  _globals['_TENANTSERVICE']._serialized_start=2164
  _globals['_TENANTSERVICE']._serialized_end=3222
# @@protoc_insertion_point(module_scope)
