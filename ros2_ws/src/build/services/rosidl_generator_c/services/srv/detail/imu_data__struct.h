// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from services:srv/IMUData.idl
// generated code does not contain a copyright notice

#ifndef SERVICES__SRV__DETAIL__IMU_DATA__STRUCT_H_
#define SERVICES__SRV__DETAIL__IMU_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/IMUData in the package services.
typedef struct services__srv__IMUData_Request
{
  uint8_t structure_needs_at_least_one_member;
} services__srv__IMUData_Request;

// Struct for a sequence of services__srv__IMUData_Request.
typedef struct services__srv__IMUData_Request__Sequence
{
  services__srv__IMUData_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} services__srv__IMUData_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/IMUData in the package services.
typedef struct services__srv__IMUData_Response
{
  double heading;
  double acceleration;
  double omega;
} services__srv__IMUData_Response;

// Struct for a sequence of services__srv__IMUData_Response.
typedef struct services__srv__IMUData_Response__Sequence
{
  services__srv__IMUData_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} services__srv__IMUData_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SERVICES__SRV__DETAIL__IMU_DATA__STRUCT_H_
