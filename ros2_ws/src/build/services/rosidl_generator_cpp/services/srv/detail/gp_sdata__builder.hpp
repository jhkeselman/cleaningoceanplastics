// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from services:srv/GPSdata.idl
// generated code does not contain a copyright notice

#ifndef SERVICES__SRV__DETAIL__GP_SDATA__BUILDER_HPP_
#define SERVICES__SRV__DETAIL__GP_SDATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "services/srv/detail/gp_sdata__struct.hpp"
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
auto build<::services::srv::GPSdata_Request>()
{
  return ::services::srv::GPSdata_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace services


namespace services
{

namespace srv
{

namespace builder
{

class Init_GPSdata_Response_fix
{
public:
  Init_GPSdata_Response_fix()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::services::srv::GPSdata_Response fix(::services::srv::GPSdata_Response::_fix_type arg)
  {
    msg_.fix = std::move(arg);
    return std::move(msg_);
  }

private:
  ::services::srv::GPSdata_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::services::srv::GPSdata_Response>()
{
  return services::srv::builder::Init_GPSdata_Response_fix();
}

}  // namespace services

#endif  // SERVICES__SRV__DETAIL__GP_SDATA__BUILDER_HPP_
