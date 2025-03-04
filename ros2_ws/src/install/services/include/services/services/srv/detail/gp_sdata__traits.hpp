// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from services:srv/GPSdata.idl
// generated code does not contain a copyright notice

#ifndef SERVICES__SRV__DETAIL__GP_SDATA__TRAITS_HPP_
#define SERVICES__SRV__DETAIL__GP_SDATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "services/srv/detail/gp_sdata__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace services
{

namespace srv
{

inline void to_flow_style_yaml(
  const GPSdata_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GPSdata_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GPSdata_Request & msg, bool use_flow_style = false)
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
  const services::srv::GPSdata_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use services::srv::to_yaml() instead")]]
inline std::string to_yaml(const services::srv::GPSdata_Request & msg)
{
  return services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<services::srv::GPSdata_Request>()
{
  return "services::srv::GPSdata_Request";
}

template<>
inline const char * name<services::srv::GPSdata_Request>()
{
  return "services/srv/GPSdata_Request";
}

template<>
struct has_fixed_size<services::srv::GPSdata_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<services::srv::GPSdata_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<services::srv::GPSdata_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'fix'
#include "sensor_msgs/msg/detail/nav_sat_fix__traits.hpp"

namespace services
{

namespace srv
{

inline void to_flow_style_yaml(
  const GPSdata_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: fix
  {
    out << "fix: ";
    to_flow_style_yaml(msg.fix, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GPSdata_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: fix
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fix:\n";
    to_block_style_yaml(msg.fix, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GPSdata_Response & msg, bool use_flow_style = false)
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
  const services::srv::GPSdata_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use services::srv::to_yaml() instead")]]
inline std::string to_yaml(const services::srv::GPSdata_Response & msg)
{
  return services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<services::srv::GPSdata_Response>()
{
  return "services::srv::GPSdata_Response";
}

template<>
inline const char * name<services::srv::GPSdata_Response>()
{
  return "services/srv/GPSdata_Response";
}

template<>
struct has_fixed_size<services::srv::GPSdata_Response>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::NavSatFix>::value> {};

template<>
struct has_bounded_size<services::srv::GPSdata_Response>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::NavSatFix>::value> {};

template<>
struct is_message<services::srv::GPSdata_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<services::srv::GPSdata>()
{
  return "services::srv::GPSdata";
}

template<>
inline const char * name<services::srv::GPSdata>()
{
  return "services/srv/GPSdata";
}

template<>
struct has_fixed_size<services::srv::GPSdata>
  : std::integral_constant<
    bool,
    has_fixed_size<services::srv::GPSdata_Request>::value &&
    has_fixed_size<services::srv::GPSdata_Response>::value
  >
{
};

template<>
struct has_bounded_size<services::srv::GPSdata>
  : std::integral_constant<
    bool,
    has_bounded_size<services::srv::GPSdata_Request>::value &&
    has_bounded_size<services::srv::GPSdata_Response>::value
  >
{
};

template<>
struct is_service<services::srv::GPSdata>
  : std::true_type
{
};

template<>
struct is_service_request<services::srv::GPSdata_Request>
  : std::true_type
{
};

template<>
struct is_service_response<services::srv::GPSdata_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SERVICES__SRV__DETAIL__GP_SDATA__TRAITS_HPP_
