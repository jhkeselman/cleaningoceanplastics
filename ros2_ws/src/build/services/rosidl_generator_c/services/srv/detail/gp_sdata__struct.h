// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from services:srv/GPSdata.idl
// generated code does not contain a copyright notice

#ifndef SERVICES__SRV__DETAIL__GP_SDATA__STRUCT_H_
#define SERVICES__SRV__DETAIL__GP_SDATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GPSdata in the package services.
typedef struct services__srv__GPSdata_Request
{
  uint8_t structure_needs_at_least_one_member;
} services__srv__GPSdata_Request;

// Struct for a sequence of services__srv__GPSdata_Request.
typedef struct services__srv__GPSdata_Request__Sequence
{
  services__srv__GPSdata_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} services__srv__GPSdata_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'fix'
#include "sensor_msgs/msg/detail/nav_sat_fix__struct.h"

/// Struct defined in srv/GPSdata in the package services.
typedef struct services__srv__GPSdata_Response
{
  sensor_msgs__msg__NavSatFix fix;
} services__srv__GPSdata_Response;

// Struct for a sequence of services__srv__GPSdata_Response.
typedef struct services__srv__GPSdata_Response__Sequence
{
  services__srv__GPSdata_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} services__srv__GPSdata_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SERVICES__SRV__DETAIL__GP_SDATA__STRUCT_H_
