// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from services:srv/IMUData.idl
// generated code does not contain a copyright notice

#ifndef SERVICES__SRV__DETAIL__IMU_DATA__BUILDER_HPP_
#define SERVICES__SRV__DETAIL__IMU_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "services/srv/detail/imu_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace services
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::services::srv::IMUData_Request>()
{
  return ::services::srv::IMUData_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace services


namespace services
{

namespace srv
{

namespace builder
{

class Init_IMUData_Response_omega
{
public:
  explicit Init_IMUData_Response_omega(::services::srv::IMUData_Response & msg)
  : msg_(msg)
  {}
  ::services::srv::IMUData_Response omega(::services::srv::IMUData_Response::_omega_type arg)
  {
    msg_.omega = std::move(arg);
    return std::move(msg_);
  }

private:
  ::services::srv::IMUData_Response msg_;
};

class Init_IMUData_Response_acceleration
{
public:
  explicit Init_IMUData_Response_acceleration(::services::srv::IMUData_Response & msg)
  : msg_(msg)
  {}
  Init_IMUData_Response_omega acceleration(::services::srv::IMUData_Response::_acceleration_type arg)
  {
    msg_.acceleration = std::move(arg);
    return Init_IMUData_Response_omega(msg_);
  }

private:
  ::services::srv::IMUData_Response msg_;
};

class Init_IMUData_Response_heading
{
public:
  Init_IMUData_Response_heading()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_IMUData_Response_acceleration heading(::services::srv::IMUData_Response::_heading_type arg)
  {
    msg_.heading = std::move(arg);
    return Init_IMUData_Response_acceleration(msg_);
  }

private:
  ::services::srv::IMUData_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::services::srv::IMUData_Response>()
{
  return services::srv::builder::Init_IMUData_Response_heading();
}

}  // namespace services

#endif  // SERVICES__SRV__DETAIL__IMU_DATA__BUILDER_HPP_
