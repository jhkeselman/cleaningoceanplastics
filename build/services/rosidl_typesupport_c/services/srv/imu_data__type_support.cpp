// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from services:srv/IMUData.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "services/srv/detail/imu_data__struct.h"
#include "services/srv/detail/imu_data__type_support.h"
#include "services/srv/detail/imu_data__functions.h"
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

typedef struct _IMUData_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _IMUData_Request_type_support_ids_t;

static const _IMUData_Request_type_support_ids_t _IMUData_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _IMUData_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _IMUData_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _IMUData_Request_type_support_symbol_names_t _IMUData_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, services, srv, IMUData_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, IMUData_Request)),
  }
};

typedef struct _IMUData_Request_type_support_data_t
{
  void * data[2];
} _IMUData_Request_type_support_data_t;

static _IMUData_Request_type_support_data_t _IMUData_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _IMUData_Request_message_typesupport_map = {
  2,
  "services",
  &_IMUData_Request_message_typesupport_ids.typesupport_identifier[0],
  &_IMUData_Request_message_typesupport_symbol_names.symbol_name[0],
  &_IMUData_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t IMUData_Request_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_IMUData_Request_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &services__srv__IMUData_Request__get_type_hash,
  &services__srv__IMUData_Request__get_type_description,
  &services__srv__IMUData_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace services

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, services, srv, IMUData_Request)() {
  return &::services::srv::rosidl_typesupport_c::IMUData_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "services/srv/detail/imu_data__struct.h"
// already included above
// #include "services/srv/detail/imu_data__type_support.h"
// already included above
// #include "services/srv/detail/imu_data__functions.h"
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

typedef struct _IMUData_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _IMUData_Response_type_support_ids_t;

static const _IMUData_Response_type_support_ids_t _IMUData_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _IMUData_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _IMUData_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _IMUData_Response_type_support_symbol_names_t _IMUData_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, services, srv, IMUData_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, IMUData_Response)),
  }
};

typedef struct _IMUData_Response_type_support_data_t
{
  void * data[2];
} _IMUData_Response_type_support_data_t;

static _IMUData_Response_type_support_data_t _IMUData_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _IMUData_Response_message_typesupport_map = {
  2,
  "services",
  &_IMUData_Response_message_typesupport_ids.typesupport_identifier[0],
  &_IMUData_Response_message_typesupport_symbol_names.symbol_name[0],
  &_IMUData_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t IMUData_Response_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_IMUData_Response_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &services__srv__IMUData_Response__get_type_hash,
  &services__srv__IMUData_Response__get_type_description,
  &services__srv__IMUData_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace services

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, services, srv, IMUData_Response)() {
  return &::services::srv::rosidl_typesupport_c::IMUData_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "services/srv/detail/imu_data__struct.h"
// already included above
// #include "services/srv/detail/imu_data__type_support.h"
// already included above
// #include "services/srv/detail/imu_data__functions.h"
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

typedef struct _IMUData_Event_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _IMUData_Event_type_support_ids_t;

static const _IMUData_Event_type_support_ids_t _IMUData_Event_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _IMUData_Event_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _IMUData_Event_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _IMUData_Event_type_support_symbol_names_t _IMUData_Event_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, services, srv, IMUData_Event)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, IMUData_Event)),
  }
};

typedef struct _IMUData_Event_type_support_data_t
{
  void * data[2];
} _IMUData_Event_type_support_data_t;

static _IMUData_Event_type_support_data_t _IMUData_Event_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _IMUData_Event_message_typesupport_map = {
  2,
  "services",
  &_IMUData_Event_message_typesupport_ids.typesupport_identifier[0],
  &_IMUData_Event_message_typesupport_symbol_names.symbol_name[0],
  &_IMUData_Event_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t IMUData_Event_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_IMUData_Event_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &services__srv__IMUData_Event__get_type_hash,
  &services__srv__IMUData_Event__get_type_description,
  &services__srv__IMUData_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace services

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, services, srv, IMUData_Event)() {
  return &::services::srv::rosidl_typesupport_c::IMUData_Event_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "services/srv/detail/imu_data__type_support.h"
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
typedef struct _IMUData_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _IMUData_type_support_ids_t;

static const _IMUData_type_support_ids_t _IMUData_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _IMUData_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _IMUData_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _IMUData_type_support_symbol_names_t _IMUData_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, services, srv, IMUData)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, services, srv, IMUData)),
  }
};

typedef struct _IMUData_type_support_data_t
{
  void * data[2];
} _IMUData_type_support_data_t;

static _IMUData_type_support_data_t _IMUData_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _IMUData_service_typesupport_map = {
  2,
  "services",
  &_IMUData_service_typesupport_ids.typesupport_identifier[0],
  &_IMUData_service_typesupport_symbol_names.symbol_name[0],
  &_IMUData_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t IMUData_service_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_IMUData_service_typesupport_map),
  rosidl_typesupport_c__get_service_typesupport_handle_function,
  &IMUData_Request_message_type_support_handle,
  &IMUData_Response_message_type_support_handle,
  &IMUData_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    services,
    srv,
    IMUData
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    services,
    srv,
    IMUData
  ),
  &services__srv__IMUData__get_type_hash,
  &services__srv__IMUData__get_type_description,
  &services__srv__IMUData__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace services

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_c, services, srv, IMUData)() {
  return &::services::srv::rosidl_typesupport_c::IMUData_service_type_support_handle;
}

#ifdef __cplusplus
}
#endif
