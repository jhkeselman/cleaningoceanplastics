// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from services:srv/KalmanState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "services/srv/kalman_state.h"


#ifndef SERVICES__SRV__DETAIL__KALMAN_STATE__STRUCT_H_
#define SERVICES__SRV__DETAIL__KALMAN_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/KalmanState in the package services.
typedef struct services__srv__KalmanState_Request
{
  uint8_t structure_needs_at_least_one_member;
} services__srv__KalmanState_Request;

// Struct for a sequence of services__srv__KalmanState_Request.
typedef struct services__srv__KalmanState_Request__Sequence
{
  services__srv__KalmanState_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} services__srv__KalmanState_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'state'
#include "std_msgs/msg/detail/float32_multi_array__struct.h"

/// Struct defined in srv/KalmanState in the package services.
typedef struct services__srv__KalmanState_Response
{
  std_msgs__msg__Float32MultiArray state;
} services__srv__KalmanState_Response;

// Struct for a sequence of services__srv__KalmanState_Response.
typedef struct services__srv__KalmanState_Response__Sequence
{
  services__srv__KalmanState_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} services__srv__KalmanState_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  services__srv__KalmanState_Event__request__MAX_SIZE = 1
};
// response
enum
{
  services__srv__KalmanState_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/KalmanState in the package services.
typedef struct services__srv__KalmanState_Event
{
  service_msgs__msg__ServiceEventInfo info;
  services__srv__KalmanState_Request__Sequence request;
  services__srv__KalmanState_Response__Sequence response;
} services__srv__KalmanState_Event;

// Struct for a sequence of services__srv__KalmanState_Event.
typedef struct services__srv__KalmanState_Event__Sequence
{
  services__srv__KalmanState_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} services__srv__KalmanState_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SERVICES__SRV__DETAIL__KALMAN_STATE__STRUCT_H_
