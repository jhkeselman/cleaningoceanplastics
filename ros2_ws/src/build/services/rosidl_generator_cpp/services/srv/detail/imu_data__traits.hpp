// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from services:srv/IMUData.idl
// generated code does not contain a copyright notice

#ifndef SERVICES__SRV__DETAIL__IMU_DATA__TRAITS_HPP_
#define SERVICES__SRV__DETAIL__IMU_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "services/srv/detail/imu_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace services
{

namespace srv
{

inline void to_flow_style_yaml(
  const IMUData_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const IMUData_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const IMUData_Request & msg, bool use_flow_style = false)
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
  const services::srv::IMUData_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use services::srv::to_yaml() instead")]]
inline std::string to_yaml(const services::srv::IMUData_Request & msg)
{
  return services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<services::srv::IMUData_Request>()
{
  return "services::srv::IMUData_Request";
}

template<>
inline const char * name<services::srv::IMUData_Request>()
{
  return "services/srv/IMUData_Request";
}

template<>
struct has_fixed_size<services::srv::IMUData_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<services::srv::IMUData_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<services::srv::IMUData_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace services
{

namespace srv
{

inline void to_flow_style_yaml(
  const IMUData_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: heading
  {
    out << "heading: ";
    rosidl_generator_traits::value_to_yaml(msg.heading, out);
    out << ", ";
  }

  // member: acceleration
  {
    out << "acceleration: ";
    rosidl_generator_traits::value_to_yaml(msg.acceleration, out);
    out << ", ";
  }

  // member: omega
  {
    out << "omega: ";
    rosidl_generator_traits::value_to_yaml(msg.omega, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const IMUData_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: heading
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "heading: ";
    rosidl_generator_traits::value_to_yaml(msg.heading, out);
    out << "\n";
  }

  // member: acceleration
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acceleration: ";
    rosidl_generator_traits::value_to_yaml(msg.acceleration, out);
    out << "\n";
  }

  // member: omega
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "omega: ";
    rosidl_generator_traits::value_to_yaml(msg.omega, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const IMUData_Response & msg, bool use_flow_style = false)
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
  const services::srv::IMUData_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use services::srv::to_yaml() instead")]]
inline std::string to_yaml(const services::srv::IMUData_Response & msg)
{
  return services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<services::srv::IMUData_Response>()
{
  return "services::srv::IMUData_Response";
}

template<>
inline const char * name<services::srv::IMUData_Response>()
{
  return "services/srv/IMUData_Response";
}

template<>
struct has_fixed_size<services::srv::IMUData_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<services::srv::IMUData_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<services::srv::IMUData_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<services::srv::IMUData>()
{
  return "services::srv::IMUData";
}

template<>
inline const char * name<services::srv::IMUData>()
{
  return "services/srv/IMUData";
}

template<>
struct has_fixed_size<services::srv::IMUData>
  : std::integral_constant<
    bool,
    has_fixed_size<services::srv::IMUData_Request>::value &&
    has_fixed_size<services::srv::IMUData_Response>::value
  >
{
};

template<>
struct has_bounded_size<services::srv::IMUData>
  : std::integral_constant<
    bool,
    has_bounded_size<services::srv::IMUData_Request>::value &&
    has_bounded_size<services::srv::IMUData_Response>::value
  >
{
};

template<>
struct is_service<services::srv::IMUData>
  : std::true_type
{
};

template<>
struct is_service_request<services::srv::IMUData_Request>
  : std::true_type
{
};

template<>
struct is_service_response<services::srv::IMUData_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SERVICES__SRV__DETAIL__IMU_DATA__TRAITS_HPP_
