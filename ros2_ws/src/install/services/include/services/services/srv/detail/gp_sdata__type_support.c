// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from services:srv/GPSdata.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "services/srv/detail/gp_sdata__rosidl_typesupport_introspection_c.h"
#include "services/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "services/srv/detail/gp_sdata__functions.h"
#include "services/srv/detail/gp_sdata__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  services__srv__GPSdata_Request__init(message_memory);
}

void services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_fini_function(void * message_memory)
{
  services__srv__GPSdata_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(services__srv__GPSdata_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_message_members = {
  "services__srv",  // message namespace
  "GPSdata_Request",  // message name
  1,  // number of fields
  sizeof(services__srv__GPSdata_Request),
  services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_message_member_array,  // message members
  services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_message_type_support_handle = {
  0,
  &services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_services
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, GPSdata_Request)() {
  if (!services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_message_type_support_handle.typesupport_identifier) {
    services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &services__srv__GPSdata_Request__rosidl_typesupport_introspection_c__GPSdata_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "services/srv/detail/gp_sdata__rosidl_typesupport_introspection_c.h"
// already included above
// #include "services/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "services/srv/detail/gp_sdata__functions.h"
// already included above
// #include "services/srv/detail/gp_sdata__struct.h"


// Include directives for member types
// Member `fix`
#include "sensor_msgs/msg/nav_sat_fix.h"
// Member `fix`
#include "sensor_msgs/msg/detail/nav_sat_fix__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  services__srv__GPSdata_Response__init(message_memory);
}

void services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_fini_function(void * message_memory)
{
  services__srv__GPSdata_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_message_member_array[1] = {
  {
    "fix",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(services__srv__GPSdata_Response, fix),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_message_members = {
  "services__srv",  // message namespace
  "GPSdata_Response",  // message name
  1,  // number of fields
  sizeof(services__srv__GPSdata_Response),
  services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_message_member_array,  // message members
  services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_message_type_support_handle = {
  0,
  &services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_services
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, GPSdata_Response)() {
  services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, NavSatFix)();
  if (!services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_message_type_support_handle.typesupport_identifier) {
    services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &services__srv__GPSdata_Response__rosidl_typesupport_introspection_c__GPSdata_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "services/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "services/srv/detail/gp_sdata__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers services__srv__detail__gp_sdata__rosidl_typesupport_introspection_c__GPSdata_service_members = {
  "services__srv",  // service namespace
  "GPSdata",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // services__srv__detail__gp_sdata__rosidl_typesupport_introspection_c__GPSdata_Request_message_type_support_handle,
  NULL  // response message
  // services__srv__detail__gp_sdata__rosidl_typesupport_introspection_c__GPSdata_Response_message_type_support_handle
};

static rosidl_service_type_support_t services__srv__detail__gp_sdata__rosidl_typesupport_introspection_c__GPSdata_service_type_support_handle = {
  0,
  &services__srv__detail__gp_sdata__rosidl_typesupport_introspection_c__GPSdata_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, GPSdata_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, GPSdata_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_services
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, GPSdata)() {
  if (!services__srv__detail__gp_sdata__rosidl_typesupport_introspection_c__GPSdata_service_type_support_handle.typesupport_identifier) {
    services__srv__detail__gp_sdata__rosidl_typesupport_introspection_c__GPSdata_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)services__srv__detail__gp_sdata__rosidl_typesupport_introspection_c__GPSdata_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, GPSdata_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, GPSdata_Response)()->data;
  }

  return &services__srv__detail__gp_sdata__rosidl_typesupport_introspection_c__GPSdata_service_type_support_handle;
}
