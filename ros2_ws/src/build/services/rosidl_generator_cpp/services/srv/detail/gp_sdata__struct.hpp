// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from services:srv/GPSdata.idl
// generated code does not contain a copyright notice

#ifndef SERVICES__SRV__DETAIL__GP_SDATA__STRUCT_HPP_
#define SERVICES__SRV__DETAIL__GP_SDATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__services__srv__GPSdata_Request __attribute__((deprecated))
#else
# define DEPRECATED__services__srv__GPSdata_Request __declspec(deprecated)
#endif

namespace services
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GPSdata_Request_
{
  using Type = GPSdata_Request_<ContainerAllocator>;

  explicit GPSdata_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit GPSdata_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    services::srv::GPSdata_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const services::srv::GPSdata_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<services::srv::GPSdata_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<services::srv::GPSdata_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      services::srv::GPSdata_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<services::srv::GPSdata_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      services::srv::GPSdata_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<services::srv::GPSdata_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<services::srv::GPSdata_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<services::srv::GPSdata_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__services__srv__GPSdata_Request
    std::shared_ptr<services::srv::GPSdata_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__services__srv__GPSdata_Request
    std::shared_ptr<services::srv::GPSdata_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GPSdata_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const GPSdata_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GPSdata_Request_

// alias to use template instance with default allocator
using GPSdata_Request =
  services::srv::GPSdata_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace services


// Include directives for member types
// Member 'fix'
#include "sensor_msgs/msg/detail/nav_sat_fix__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__services__srv__GPSdata_Response __attribute__((deprecated))
#else
# define DEPRECATED__services__srv__GPSdata_Response __declspec(deprecated)
#endif

namespace services
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GPSdata_Response_
{
  using Type = GPSdata_Response_<ContainerAllocator>;

  explicit GPSdata_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : fix(_init)
  {
    (void)_init;
  }

  explicit GPSdata_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : fix(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _fix_type =
    sensor_msgs::msg::NavSatFix_<ContainerAllocator>;
  _fix_type fix;

  // setters for named parameter idiom
  Type & set__fix(
    const sensor_msgs::msg::NavSatFix_<ContainerAllocator> & _arg)
  {
    this->fix = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    services::srv::GPSdata_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const services::srv::GPSdata_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<services::srv::GPSdata_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<services::srv::GPSdata_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      services::srv::GPSdata_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<services::srv::GPSdata_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      services::srv::GPSdata_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<services::srv::GPSdata_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<services::srv::GPSdata_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<services::srv::GPSdata_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__services__srv__GPSdata_Response
    std::shared_ptr<services::srv::GPSdata_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__services__srv__GPSdata_Response
    std::shared_ptr<services::srv::GPSdata_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GPSdata_Response_ & other) const
  {
    if (this->fix != other.fix) {
      return false;
    }
    return true;
  }
  bool operator!=(const GPSdata_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GPSdata_Response_

// alias to use template instance with default allocator
using GPSdata_Response =
  services::srv::GPSdata_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace services

namespace services
{

namespace srv
{

struct GPSdata
{
  using Request = services::srv::GPSdata_Request;
  using Response = services::srv::GPSdata_Response;
};

}  // namespace srv

}  // namespace services

#endif  // SERVICES__SRV__DETAIL__GP_SDATA__STRUCT_HPP_
