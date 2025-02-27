// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from services:srv/IMUData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "services/srv/imu_data.hpp"


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

class Init_IMUData_Response_heading
{
public:
  Init_IMUData_Response_heading()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::services::srv::IMUData_Response heading(::services::srv::IMUData_Response::_heading_type arg)
  {
    msg_.heading = std::move(arg);
    return std::move(msg_);
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


namespace services
{

namespace srv
{

namespace builder
{

class Init_IMUData_Event_response
{
public:
  explicit Init_IMUData_Event_response(::services::srv::IMUData_Event & msg)
  : msg_(msg)
  {}
  ::services::srv::IMUData_Event response(::services::srv::IMUData_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::services::srv::IMUData_Event msg_;
};

class Init_IMUData_Event_request
{
public:
  explicit Init_IMUData_Event_request(::services::srv::IMUData_Event & msg)
  : msg_(msg)
  {}
  Init_IMUData_Event_response request(::services::srv::IMUData_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_IMUData_Event_response(msg_);
  }

private:
  ::services::srv::IMUData_Event msg_;
};

class Init_IMUData_Event_info
{
public:
  Init_IMUData_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_IMUData_Event_request info(::services::srv::IMUData_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_IMUData_Event_request(msg_);
  }

private:
  ::services::srv::IMUData_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::services::srv::IMUData_Event>()
{
  return services::srv::builder::Init_IMUData_Event_info();
}

}  // namespace services

#endif  // SERVICES__SRV__DETAIL__IMU_DATA__BUILDER_HPP_
