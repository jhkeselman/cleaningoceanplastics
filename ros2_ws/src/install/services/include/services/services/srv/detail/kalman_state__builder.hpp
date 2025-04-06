// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from services:srv/KalmanState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "services/srv/kalman_state.hpp"


#ifndef SERVICES__SRV__DETAIL__KALMAN_STATE__BUILDER_HPP_
#define SERVICES__SRV__DETAIL__KALMAN_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "services/srv/detail/kalman_state__struct.hpp"
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
auto build<::services::srv::KalmanState_Request>()
{
  return ::services::srv::KalmanState_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace services


namespace services
{

namespace srv
{

namespace builder
{

class Init_KalmanState_Response_state
{
public:
  Init_KalmanState_Response_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::services::srv::KalmanState_Response state(::services::srv::KalmanState_Response::_state_type arg)
  {
    msg_.state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::services::srv::KalmanState_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::services::srv::KalmanState_Response>()
{
  return services::srv::builder::Init_KalmanState_Response_state();
}

}  // namespace services


namespace services
{

namespace srv
{

namespace builder
{

class Init_KalmanState_Event_response
{
public:
  explicit Init_KalmanState_Event_response(::services::srv::KalmanState_Event & msg)
  : msg_(msg)
  {}
  ::services::srv::KalmanState_Event response(::services::srv::KalmanState_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::services::srv::KalmanState_Event msg_;
};

class Init_KalmanState_Event_request
{
public:
  explicit Init_KalmanState_Event_request(::services::srv::KalmanState_Event & msg)
  : msg_(msg)
  {}
  Init_KalmanState_Event_response request(::services::srv::KalmanState_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_KalmanState_Event_response(msg_);
  }

private:
  ::services::srv::KalmanState_Event msg_;
};

class Init_KalmanState_Event_info
{
public:
  Init_KalmanState_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_KalmanState_Event_request info(::services::srv::KalmanState_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_KalmanState_Event_request(msg_);
  }

private:
  ::services::srv::KalmanState_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::services::srv::KalmanState_Event>()
{
  return services::srv::builder::Init_KalmanState_Event_info();
}

}  // namespace services

#endif  // SERVICES__SRV__DETAIL__KALMAN_STATE__BUILDER_HPP_
