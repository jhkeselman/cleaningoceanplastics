// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from services:srv/KalmanState.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "services/srv/detail/kalman_state__rosidl_typesupport_introspection_c.h"
#include "services/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "services/srv/detail/kalman_state__functions.h"
#include "services/srv/detail/kalman_state__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  services__srv__KalmanState_Request__init(message_memory);
}

void services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_fini_function(void * message_memory)
{
  services__srv__KalmanState_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(services__srv__KalmanState_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_message_members = {
  "services__srv",  // message namespace
  "KalmanState_Request",  // message name
  1,  // number of fields
  sizeof(services__srv__KalmanState_Request),
  false,  // has_any_key_member_
  services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_message_member_array,  // message members
  services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_message_type_support_handle = {
  0,
  &services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_message_members,
  get_message_typesupport_handle_function,
  &services__srv__KalmanState_Request__get_type_hash,
  &services__srv__KalmanState_Request__get_type_description,
  &services__srv__KalmanState_Request__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_services
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Request)() {
  if (!services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_message_type_support_handle.typesupport_identifier) {
    services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "services/srv/detail/kalman_state__rosidl_typesupport_introspection_c.h"
// already included above
// #include "services/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "services/srv/detail/kalman_state__functions.h"
// already included above
// #include "services/srv/detail/kalman_state__struct.h"


// Include directives for member types
// Member `state`
#include "std_msgs/msg/float32_multi_array.h"
// Member `state`
#include "std_msgs/msg/detail/float32_multi_array__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  services__srv__KalmanState_Response__init(message_memory);
}

void services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_fini_function(void * message_memory)
{
  services__srv__KalmanState_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_message_member_array[1] = {
  {
    "state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(services__srv__KalmanState_Response, state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_message_members = {
  "services__srv",  // message namespace
  "KalmanState_Response",  // message name
  1,  // number of fields
  sizeof(services__srv__KalmanState_Response),
  false,  // has_any_key_member_
  services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_message_member_array,  // message members
  services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_message_type_support_handle = {
  0,
  &services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_message_members,
  get_message_typesupport_handle_function,
  &services__srv__KalmanState_Response__get_type_hash,
  &services__srv__KalmanState_Response__get_type_description,
  &services__srv__KalmanState_Response__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_services
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Response)() {
  services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Float32MultiArray)();
  if (!services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_message_type_support_handle.typesupport_identifier) {
    services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "services/srv/detail/kalman_state__rosidl_typesupport_introspection_c.h"
// already included above
// #include "services/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "services/srv/detail/kalman_state__functions.h"
// already included above
// #include "services/srv/detail/kalman_state__struct.h"


// Include directives for member types
// Member `info`
#include "service_msgs/msg/service_event_info.h"
// Member `info`
#include "service_msgs/msg/detail/service_event_info__rosidl_typesupport_introspection_c.h"
// Member `request`
// Member `response`
#include "services/srv/kalman_state.h"
// Member `request`
// Member `response`
// already included above
// #include "services/srv/detail/kalman_state__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  services__srv__KalmanState_Event__init(message_memory);
}

void services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_fini_function(void * message_memory)
{
  services__srv__KalmanState_Event__fini(message_memory);
}

size_t services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__size_function__KalmanState_Event__request(
  const void * untyped_member)
{
  const services__srv__KalmanState_Request__Sequence * member =
    (const services__srv__KalmanState_Request__Sequence *)(untyped_member);
  return member->size;
}

const void * services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_const_function__KalmanState_Event__request(
  const void * untyped_member, size_t index)
{
  const services__srv__KalmanState_Request__Sequence * member =
    (const services__srv__KalmanState_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void * services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_function__KalmanState_Event__request(
  void * untyped_member, size_t index)
{
  services__srv__KalmanState_Request__Sequence * member =
    (services__srv__KalmanState_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__fetch_function__KalmanState_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const services__srv__KalmanState_Request * item =
    ((const services__srv__KalmanState_Request *)
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_const_function__KalmanState_Event__request(untyped_member, index));
  services__srv__KalmanState_Request * value =
    (services__srv__KalmanState_Request *)(untyped_value);
  *value = *item;
}

void services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__assign_function__KalmanState_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  services__srv__KalmanState_Request * item =
    ((services__srv__KalmanState_Request *)
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_function__KalmanState_Event__request(untyped_member, index));
  const services__srv__KalmanState_Request * value =
    (const services__srv__KalmanState_Request *)(untyped_value);
  *item = *value;
}

bool services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__resize_function__KalmanState_Event__request(
  void * untyped_member, size_t size)
{
  services__srv__KalmanState_Request__Sequence * member =
    (services__srv__KalmanState_Request__Sequence *)(untyped_member);
  services__srv__KalmanState_Request__Sequence__fini(member);
  return services__srv__KalmanState_Request__Sequence__init(member, size);
}

size_t services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__size_function__KalmanState_Event__response(
  const void * untyped_member)
{
  const services__srv__KalmanState_Response__Sequence * member =
    (const services__srv__KalmanState_Response__Sequence *)(untyped_member);
  return member->size;
}

const void * services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_const_function__KalmanState_Event__response(
  const void * untyped_member, size_t index)
{
  const services__srv__KalmanState_Response__Sequence * member =
    (const services__srv__KalmanState_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void * services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_function__KalmanState_Event__response(
  void * untyped_member, size_t index)
{
  services__srv__KalmanState_Response__Sequence * member =
    (services__srv__KalmanState_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__fetch_function__KalmanState_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const services__srv__KalmanState_Response * item =
    ((const services__srv__KalmanState_Response *)
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_const_function__KalmanState_Event__response(untyped_member, index));
  services__srv__KalmanState_Response * value =
    (services__srv__KalmanState_Response *)(untyped_value);
  *value = *item;
}

void services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__assign_function__KalmanState_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  services__srv__KalmanState_Response * item =
    ((services__srv__KalmanState_Response *)
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_function__KalmanState_Event__response(untyped_member, index));
  const services__srv__KalmanState_Response * value =
    (const services__srv__KalmanState_Response *)(untyped_value);
  *item = *value;
}

bool services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__resize_function__KalmanState_Event__response(
  void * untyped_member, size_t size)
{
  services__srv__KalmanState_Response__Sequence * member =
    (services__srv__KalmanState_Response__Sequence *)(untyped_member);
  services__srv__KalmanState_Response__Sequence__fini(member);
  return services__srv__KalmanState_Response__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_member_array[3] = {
  {
    "info",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(services__srv__KalmanState_Event, info),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "request",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(services__srv__KalmanState_Event, request),  // bytes offset in struct
    NULL,  // default value
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__size_function__KalmanState_Event__request,  // size() function pointer
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_const_function__KalmanState_Event__request,  // get_const(index) function pointer
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_function__KalmanState_Event__request,  // get(index) function pointer
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__fetch_function__KalmanState_Event__request,  // fetch(index, &value) function pointer
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__assign_function__KalmanState_Event__request,  // assign(index, value) function pointer
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__resize_function__KalmanState_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(services__srv__KalmanState_Event, response),  // bytes offset in struct
    NULL,  // default value
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__size_function__KalmanState_Event__response,  // size() function pointer
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_const_function__KalmanState_Event__response,  // get_const(index) function pointer
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__get_function__KalmanState_Event__response,  // get(index) function pointer
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__fetch_function__KalmanState_Event__response,  // fetch(index, &value) function pointer
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__assign_function__KalmanState_Event__response,  // assign(index, value) function pointer
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__resize_function__KalmanState_Event__response  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_members = {
  "services__srv",  // message namespace
  "KalmanState_Event",  // message name
  3,  // number of fields
  sizeof(services__srv__KalmanState_Event),
  false,  // has_any_key_member_
  services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_member_array,  // message members
  services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_type_support_handle = {
  0,
  &services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_members,
  get_message_typesupport_handle_function,
  &services__srv__KalmanState_Event__get_type_hash,
  &services__srv__KalmanState_Event__get_type_description,
  &services__srv__KalmanState_Event__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_services
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Event)() {
  services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_msgs, msg, ServiceEventInfo)();
  services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Request)();
  services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Response)();
  if (!services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_type_support_handle.typesupport_identifier) {
    services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "services/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "services/srv/detail/kalman_state__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers services__srv__detail__kalman_state__rosidl_typesupport_introspection_c__KalmanState_service_members = {
  "services__srv",  // service namespace
  "KalmanState",  // service name
  // the following fields are initialized below on first access
  NULL,  // request message
  // services__srv__detail__kalman_state__rosidl_typesupport_introspection_c__KalmanState_Request_message_type_support_handle,
  NULL,  // response message
  // services__srv__detail__kalman_state__rosidl_typesupport_introspection_c__KalmanState_Response_message_type_support_handle
  NULL  // event_message
  // services__srv__detail__kalman_state__rosidl_typesupport_introspection_c__KalmanState_Response_message_type_support_handle
};


static rosidl_service_type_support_t services__srv__detail__kalman_state__rosidl_typesupport_introspection_c__KalmanState_service_type_support_handle = {
  0,
  &services__srv__detail__kalman_state__rosidl_typesupport_introspection_c__KalmanState_service_members,
  get_service_typesupport_handle_function,
  &services__srv__KalmanState_Request__rosidl_typesupport_introspection_c__KalmanState_Request_message_type_support_handle,
  &services__srv__KalmanState_Response__rosidl_typesupport_introspection_c__KalmanState_Response_message_type_support_handle,
  &services__srv__KalmanState_Event__rosidl_typesupport_introspection_c__KalmanState_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    services,
    srv,
    KalmanState
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    services,
    srv,
    KalmanState
  ),
  &services__srv__KalmanState__get_type_hash,
  &services__srv__KalmanState__get_type_description,
  &services__srv__KalmanState__get_type_description_sources,
};

// Forward declaration of message type support functions for service members
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Request)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Response)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Event)(void);

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_services
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState)(void) {
  if (!services__srv__detail__kalman_state__rosidl_typesupport_introspection_c__KalmanState_service_type_support_handle.typesupport_identifier) {
    services__srv__detail__kalman_state__rosidl_typesupport_introspection_c__KalmanState_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)services__srv__detail__kalman_state__rosidl_typesupport_introspection_c__KalmanState_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Response)()->data;
  }
  if (!service_members->event_members_) {
    service_members->event_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Event)()->data;
  }

  return &services__srv__detail__kalman_state__rosidl_typesupport_introspection_c__KalmanState_service_type_support_handle;
}
