// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from services:srv/IMUData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "services/srv/imu_data.hpp"


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

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace services
{

namespace srv
{

inline void to_flow_style_yaml(
  const IMUData_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
        to_flow_style_yaml(item, out);
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
  const IMUData_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const IMUData_Event & msg, bool use_flow_style = false)
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
  const services::srv::IMUData_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use services::srv::to_yaml() instead")]]
inline std::string to_yaml(const services::srv::IMUData_Event & msg)
{
  return services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<services::srv::IMUData_Event>()
{
  return "services::srv::IMUData_Event";
}

template<>
inline const char * name<services::srv::IMUData_Event>()
{
  return "services/srv/IMUData_Event";
}

template<>
struct has_fixed_size<services::srv::IMUData_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<services::srv::IMUData_Event>
  : std::integral_constant<bool, has_bounded_size<service_msgs::msg::ServiceEventInfo>::value && has_bounded_size<services::srv::IMUData_Request>::value && has_bounded_size<services::srv::IMUData_Response>::value> {};

template<>
struct is_message<services::srv::IMUData_Event>
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
