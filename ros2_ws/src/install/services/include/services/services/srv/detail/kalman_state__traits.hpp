// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from services:srv/KalmanState.idl
// generated code does not contain a copyright notice

#ifndef SERVICES__SRV__DETAIL__KALMAN_STATE__TRAITS_HPP_
#define SERVICES__SRV__DETAIL__KALMAN_STATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "services/srv/detail/kalman_state__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace services
{

namespace srv
{

inline void to_flow_style_yaml(
  const KalmanState_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const KalmanState_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const KalmanState_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace services

namespace rosidl_generator_traits
{

[[deprecated("use services::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const services::srv::KalmanState_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use services::srv::to_yaml() instead")]]
inline std::string to_yaml(const services::srv::KalmanState_Request & msg)
{
  return services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<services::srv::KalmanState_Request>()
{
  return "services::srv::KalmanState_Request";
}

template<>
inline const char * name<services::srv::KalmanState_Request>()
{
  return "services/srv/KalmanState_Request";
}

template<>
struct has_fixed_size<services::srv::KalmanState_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<services::srv::KalmanState_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<services::srv::KalmanState_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace services
{

namespace srv
{

inline void to_flow_style_yaml(
  const KalmanState_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: state
  {
    if (msg.state.size() == 0) {
      out << "state: []";
    } else {
      out << "state: [";
      size_t pending_items = msg.state.size();
      for (auto item : msg.state) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const KalmanState_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.state.size() == 0) {
      out << "state: []\n";
    } else {
      out << "state:\n";
      for (auto item : msg.state) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const KalmanState_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace services

namespace rosidl_generator_traits
{

[[deprecated("use services::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const services::srv::KalmanState_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use services::srv::to_yaml() instead")]]
inline std::string to_yaml(const services::srv::KalmanState_Response & msg)
{
  return services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<services::srv::KalmanState_Response>()
{
  return "services::srv::KalmanState_Response";
}

template<>
inline const char * name<services::srv::KalmanState_Response>()
{
  return "services/srv/KalmanState_Response";
}

template<>
struct has_fixed_size<services::srv::KalmanState_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<services::srv::KalmanState_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<services::srv::KalmanState_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<services::srv::KalmanState>()
{
  return "services::srv::KalmanState";
}

template<>
inline const char * name<services::srv::KalmanState>()
{
  return "services/srv/KalmanState";
}

template<>
struct has_fixed_size<services::srv::KalmanState>
  : std::integral_constant<
    bool,
    has_fixed_size<services::srv::KalmanState_Request>::value &&
    has_fixed_size<services::srv::KalmanState_Response>::value
  >
{
};

template<>
struct has_bounded_size<services::srv::KalmanState>
  : std::integral_constant<
    bool,
    has_bounded_size<services::srv::KalmanState_Request>::value &&
    has_bounded_size<services::srv::KalmanState_Response>::value
  >
{
};

template<>
struct is_service<services::srv::KalmanState>
  : std::true_type
{
};

template<>
struct is_service_request<services::srv::KalmanState_Request>
  : std::true_type
{
};

template<>
struct is_service_response<services::srv::KalmanState_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SERVICES__SRV__DETAIL__KALMAN_STATE__TRAITS_HPP_
