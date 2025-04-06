// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from services:srv/KalmanState.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "services/srv/detail/kalman_state__struct.h"
#include "services/srv/detail/kalman_state__type_support.h"
#include "services/srv/detail/kalman_state__functions.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace services
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _KalmanState_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _KalmanState_Request_type_support_ids_t;

static const _KalmanState_Request_type_support_ids_t _KalmanState_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _KalmanState_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _KalmanState_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _KalmanState_Request_type_support_symbol_names_t _KalmanState_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, services, srv, KalmanState_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Request)),
  }
};

typedef struct _KalmanState_Request_type_support_data_t
{
  void * data[2];
} _KalmanState_Request_type_support_data_t;

static _KalmanState_Request_type_support_data_t _KalmanState_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _KalmanState_Request_message_typesupport_map = {
  2,
  "services",
  &_KalmanState_Request_message_typesupport_ids.typesupport_identifier[0],
  &_KalmanState_Request_message_typesupport_symbol_names.symbol_name[0],
  &_KalmanState_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t KalmanState_Request_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_KalmanState_Request_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &services__srv__KalmanState_Request__get_type_hash,
  &services__srv__KalmanState_Request__get_type_description,
  &services__srv__KalmanState_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace services

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, services, srv, KalmanState_Request)() {
  return &::services::srv::rosidl_typesupport_c::KalmanState_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "services/srv/detail/kalman_state__struct.h"
// already included above
// #include "services/srv/detail/kalman_state__type_support.h"
// already included above
// #include "services/srv/detail/kalman_state__functions.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace services
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _KalmanState_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _KalmanState_Response_type_support_ids_t;

static const _KalmanState_Response_type_support_ids_t _KalmanState_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _KalmanState_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _KalmanState_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _KalmanState_Response_type_support_symbol_names_t _KalmanState_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, services, srv, KalmanState_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Response)),
  }
};

typedef struct _KalmanState_Response_type_support_data_t
{
  void * data[2];
} _KalmanState_Response_type_support_data_t;

static _KalmanState_Response_type_support_data_t _KalmanState_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _KalmanState_Response_message_typesupport_map = {
  2,
  "services",
  &_KalmanState_Response_message_typesupport_ids.typesupport_identifier[0],
  &_KalmanState_Response_message_typesupport_symbol_names.symbol_name[0],
  &_KalmanState_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t KalmanState_Response_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_KalmanState_Response_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &services__srv__KalmanState_Response__get_type_hash,
  &services__srv__KalmanState_Response__get_type_description,
  &services__srv__KalmanState_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace services

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, services, srv, KalmanState_Response)() {
  return &::services::srv::rosidl_typesupport_c::KalmanState_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "services/srv/detail/kalman_state__struct.h"
// already included above
// #include "services/srv/detail/kalman_state__type_support.h"
// already included above
// #include "services/srv/detail/kalman_state__functions.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace services
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _KalmanState_Event_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _KalmanState_Event_type_support_ids_t;

static const _KalmanState_Event_type_support_ids_t _KalmanState_Event_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _KalmanState_Event_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _KalmanState_Event_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _KalmanState_Event_type_support_symbol_names_t _KalmanState_Event_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, services, srv, KalmanState_Event)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState_Event)),
  }
};

typedef struct _KalmanState_Event_type_support_data_t
{
  void * data[2];
} _KalmanState_Event_type_support_data_t;

static _KalmanState_Event_type_support_data_t _KalmanState_Event_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _KalmanState_Event_message_typesupport_map = {
  2,
  "services",
  &_KalmanState_Event_message_typesupport_ids.typesupport_identifier[0],
  &_KalmanState_Event_message_typesupport_symbol_names.symbol_name[0],
  &_KalmanState_Event_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t KalmanState_Event_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_KalmanState_Event_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &services__srv__KalmanState_Event__get_type_hash,
  &services__srv__KalmanState_Event__get_type_description,
  &services__srv__KalmanState_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace services

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, services, srv, KalmanState_Event)() {
  return &::services::srv::rosidl_typesupport_c::KalmanState_Event_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "services/srv/detail/kalman_state__type_support.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/service_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
#include "service_msgs/msg/service_event_info.h"
#include "builtin_interfaces/msg/time.h"

namespace services
{

namespace srv
{

namespace rosidl_typesupport_c
{
typedef struct _KalmanState_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _KalmanState_type_support_ids_t;

static const _KalmanState_type_support_ids_t _KalmanState_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _KalmanState_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _KalmanState_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _KalmanState_type_support_symbol_names_t _KalmanState_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, services, srv, KalmanState)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, KalmanState)),
  }
};

typedef struct _KalmanState_type_support_data_t
{
  void * data[2];
} _KalmanState_type_support_data_t;

static _KalmanState_type_support_data_t _KalmanState_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _KalmanState_service_typesupport_map = {
  2,
  "services",
  &_KalmanState_service_typesupport_ids.typesupport_identifier[0],
  &_KalmanState_service_typesupport_symbol_names.symbol_name[0],
  &_KalmanState_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t KalmanState_service_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_KalmanState_service_typesupport_map),
  rosidl_typesupport_c__get_service_typesupport_handle_function,
  &KalmanState_Request_message_type_support_handle,
  &KalmanState_Response_message_type_support_handle,
  &KalmanState_Event_message_type_support_handle,
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

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace services

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_c, services, srv, KalmanState)() {
  return &::services::srv::rosidl_typesupport_c::KalmanState_service_type_support_handle;
}

#ifdef __cplusplus
}
#endif
