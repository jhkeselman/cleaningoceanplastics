// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from services:srv/IMUData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "services/srv/imu_data.hpp"


#ifndef SERVICES__SRV__DETAIL__IMU_DATA__STRUCT_HPP_
#define SERVICES__SRV__DETAIL__IMU_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__services__srv__IMUData_Request __attribute__((deprecated))
#else
# define DEPRECATED__services__srv__IMUData_Request __declspec(deprecated)
#endif

namespace services
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct IMUData_Request_
{
  using Type = IMUData_Request_<ContainerAllocator>;

  explicit IMUData_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit IMUData_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    services::srv::IMUData_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const services::srv::IMUData_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<services::srv::IMUData_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<services::srv::IMUData_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      services::srv::IMUData_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<services::srv::IMUData_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      services::srv::IMUData_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<services::srv::IMUData_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<services::srv::IMUData_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<services::srv::IMUData_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__services__srv__IMUData_Request
    std::shared_ptr<services::srv::IMUData_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__services__srv__IMUData_Request
    std::shared_ptr<services::srv::IMUData_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const IMUData_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const IMUData_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct IMUData_Request_

// alias to use template instance with default allocator
using IMUData_Request =
  services::srv::IMUData_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace services


#ifndef _WIN32
# define DEPRECATED__services__srv__IMUData_Response __attribute__((deprecated))
#else
# define DEPRECATED__services__srv__IMUData_Response __declspec(deprecated)
#endif

namespace services
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct IMUData_Response_
{
  using Type = IMUData_Response_<ContainerAllocator>;

  explicit IMUData_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->heading = 0.0;
    }
  }

  explicit IMUData_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->heading = 0.0;
    }
  }

  // field types and members
  using _heading_type =
    double;
  _heading_type heading;

  // setters for named parameter idiom
  Type & set__heading(
    const double & _arg)
  {
    this->heading = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    services::srv::IMUData_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const services::srv::IMUData_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<services::srv::IMUData_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<services::srv::IMUData_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      services::srv::IMUData_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<services::srv::IMUData_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      services::srv::IMUData_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<services::srv::IMUData_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<services::srv::IMUData_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<services::srv::IMUData_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__services__srv__IMUData_Response
    std::shared_ptr<services::srv::IMUData_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__services__srv__IMUData_Response
    std::shared_ptr<services::srv::IMUData_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const IMUData_Response_ & other) const
  {
    if (this->heading != other.heading) {
      return false;
    }
    return true;
  }
  bool operator!=(const IMUData_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct IMUData_Response_

// alias to use template instance with default allocator
using IMUData_Response =
  services::srv::IMUData_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace services


// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__services__srv__IMUData_Event __attribute__((deprecated))
#else
# define DEPRECATED__services__srv__IMUData_Event __declspec(deprecated)
#endif

namespace services
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct IMUData_Event_
{
  using Type = IMUData_Event_<ContainerAllocator>;

  explicit IMUData_Event_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_init)
  {
    (void)_init;
  }

  explicit IMUData_Event_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _info_type =
    service_msgs::msg::ServiceEventInfo_<ContainerAllocator>;
  _info_type info;
  using _request_type =
    rosidl_runtime_cpp::BoundedVector<services::srv::IMUData_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<services::srv::IMUData_Request_<ContainerAllocator>>>;
  _request_type request;
  using _response_type =
    rosidl_runtime_cpp::BoundedVector<services::srv::IMUData_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<services::srv::IMUData_Response_<ContainerAllocator>>>;
  _response_type response;

  // setters for named parameter idiom
  Type & set__info(
    const service_msgs::msg::ServiceEventInfo_<ContainerAllocator> & _arg)
  {
    this->info = _arg;
    return *this;
  }
  Type & set__request(
    const rosidl_runtime_cpp::BoundedVector<services::srv::IMUData_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<services::srv::IMUData_Request_<ContainerAllocator>>> & _arg)
  {
    this->request = _arg;
    return *this;
  }
  Type & set__response(
    const rosidl_runtime_cpp::BoundedVector<services::srv::IMUData_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<services::srv::IMUData_Response_<ContainerAllocator>>> & _arg)
  {
    this->response = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    services::srv::IMUData_Event_<ContainerAllocator> *;
  using ConstRawPtr =
    const services::srv::IMUData_Event_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<services::srv::IMUData_Event_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<services::srv::IMUData_Event_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      services::srv::IMUData_Event_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<services::srv::IMUData_Event_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      services::srv::IMUData_Event_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<services::srv::IMUData_Event_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<services::srv::IMUData_Event_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<services::srv::IMUData_Event_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__services__srv__IMUData_Event
    std::shared_ptr<services::srv::IMUData_Event_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__services__srv__IMUData_Event
    std::shared_ptr<services::srv::IMUData_Event_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const IMUData_Event_ & other) const
  {
    if (this->info != other.info) {
      return false;
    }
    if (this->request != other.request) {
      return false;
    }
    if (this->response != other.response) {
      return false;
    }
    return true;
  }
  bool operator!=(const IMUData_Event_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct IMUData_Event_

// alias to use template instance with default allocator
using IMUData_Event =
  services::srv::IMUData_Event_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace services

namespace services
{

namespace srv
{

struct IMUData
{
  using Request = services::srv::IMUData_Request;
  using Response = services::srv::IMUData_Response;
  using Event = services::srv::IMUData_Event;
};

}  // namespace srv

}  // namespace services

#endif  // SERVICES__SRV__DETAIL__IMU_DATA__STRUCT_HPP_
