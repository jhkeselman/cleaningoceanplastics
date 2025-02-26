// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from services:srv/IMUData.idl
// generated code does not contain a copyright notice

#include "services/srv/detail/imu_data__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_services
const rosidl_type_hash_t *
services__srv__IMUData__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x06, 0xe5, 0x48, 0x35, 0xe5, 0xda, 0x75, 0xaf,
      0xd8, 0xda, 0xcd, 0xd1, 0x52, 0x9b, 0x24, 0xc3,
      0xb3, 0x54, 0xcb, 0x39, 0xa7, 0x09, 0xa3, 0xb9,
      0xa2, 0x53, 0x69, 0x31, 0x1a, 0x74, 0x7b, 0x82,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_services
const rosidl_type_hash_t *
services__srv__IMUData_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x8d, 0x49, 0xc3, 0xf1, 0xa5, 0x86, 0xa4, 0xfc,
      0xfd, 0xe9, 0x28, 0xe0, 0xd0, 0x6e, 0x9e, 0xfa,
      0x54, 0x4b, 0x37, 0x74, 0x60, 0xf6, 0xc2, 0xb4,
      0x12, 0xe5, 0xb3, 0x62, 0x75, 0xfd, 0x9f, 0xb6,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_services
const rosidl_type_hash_t *
services__srv__IMUData_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x79, 0x15, 0xab, 0xba, 0x8d, 0x22, 0x88, 0xb3,
      0x20, 0xba, 0x1a, 0x99, 0x05, 0x1a, 0x7e, 0x5b,
      0x1e, 0xc8, 0xf0, 0x4f, 0x45, 0x36, 0x5a, 0x3d,
      0x03, 0x63, 0x53, 0xb5, 0xc1, 0x02, 0xc8, 0xde,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_services
const rosidl_type_hash_t *
services__srv__IMUData_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x22, 0x0e, 0xfe, 0x9d, 0xd8, 0x37, 0x0a, 0x4c,
      0x8c, 0x7a, 0x6f, 0xe6, 0x45, 0x7d, 0x97, 0x4f,
      0xe0, 0x55, 0x67, 0x22, 0x01, 0x6d, 0xc3, 0x9b,
      0xd5, 0x46, 0xc9, 0xa8, 0x91, 0x77, 0x45, 0xa9,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "service_msgs/msg/detail/service_event_info__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t service_msgs__msg__ServiceEventInfo__EXPECTED_HASH = {1, {
    0x41, 0xbc, 0xbb, 0xe0, 0x7a, 0x75, 0xc9, 0xb5,
    0x2b, 0xc9, 0x6b, 0xfd, 0x5c, 0x24, 0xd7, 0xf0,
    0xfc, 0x0a, 0x08, 0xc0, 0xcb, 0x79, 0x21, 0xb3,
    0x37, 0x3c, 0x57, 0x32, 0x34, 0x5a, 0x6f, 0x45,
  }};
#endif

static char services__srv__IMUData__TYPE_NAME[] = "services/srv/IMUData";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";
static char services__srv__IMUData_Event__TYPE_NAME[] = "services/srv/IMUData_Event";
static char services__srv__IMUData_Request__TYPE_NAME[] = "services/srv/IMUData_Request";
static char services__srv__IMUData_Response__TYPE_NAME[] = "services/srv/IMUData_Response";

// Define type names, field names, and default values
static char services__srv__IMUData__FIELD_NAME__request_message[] = "request_message";
static char services__srv__IMUData__FIELD_NAME__response_message[] = "response_message";
static char services__srv__IMUData__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field services__srv__IMUData__FIELDS[] = {
  {
    {services__srv__IMUData__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {services__srv__IMUData_Request__TYPE_NAME, 28, 28},
    },
    {NULL, 0, 0},
  },
  {
    {services__srv__IMUData__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {services__srv__IMUData_Response__TYPE_NAME, 29, 29},
    },
    {NULL, 0, 0},
  },
  {
    {services__srv__IMUData__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {services__srv__IMUData_Event__TYPE_NAME, 26, 26},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription services__srv__IMUData__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {services__srv__IMUData_Event__TYPE_NAME, 26, 26},
    {NULL, 0, 0},
  },
  {
    {services__srv__IMUData_Request__TYPE_NAME, 28, 28},
    {NULL, 0, 0},
  },
  {
    {services__srv__IMUData_Response__TYPE_NAME, 29, 29},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
services__srv__IMUData__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {services__srv__IMUData__TYPE_NAME, 20, 20},
      {services__srv__IMUData__FIELDS, 3, 3},
    },
    {services__srv__IMUData__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = services__srv__IMUData_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = services__srv__IMUData_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[4].fields = services__srv__IMUData_Response__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char services__srv__IMUData_Request__FIELD_NAME__structure_needs_at_least_one_member[] = "structure_needs_at_least_one_member";

static rosidl_runtime_c__type_description__Field services__srv__IMUData_Request__FIELDS[] = {
  {
    {services__srv__IMUData_Request__FIELD_NAME__structure_needs_at_least_one_member, 35, 35},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
services__srv__IMUData_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {services__srv__IMUData_Request__TYPE_NAME, 28, 28},
      {services__srv__IMUData_Request__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char services__srv__IMUData_Response__FIELD_NAME__heading[] = "heading";

static rosidl_runtime_c__type_description__Field services__srv__IMUData_Response__FIELDS[] = {
  {
    {services__srv__IMUData_Response__FIELD_NAME__heading, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
services__srv__IMUData_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {services__srv__IMUData_Response__TYPE_NAME, 29, 29},
      {services__srv__IMUData_Response__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char services__srv__IMUData_Event__FIELD_NAME__info[] = "info";
static char services__srv__IMUData_Event__FIELD_NAME__request[] = "request";
static char services__srv__IMUData_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field services__srv__IMUData_Event__FIELDS[] = {
  {
    {services__srv__IMUData_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {services__srv__IMUData_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {services__srv__IMUData_Request__TYPE_NAME, 28, 28},
    },
    {NULL, 0, 0},
  },
  {
    {services__srv__IMUData_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {services__srv__IMUData_Response__TYPE_NAME, 29, 29},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription services__srv__IMUData_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {services__srv__IMUData_Request__TYPE_NAME, 28, 28},
    {NULL, 0, 0},
  },
  {
    {services__srv__IMUData_Response__TYPE_NAME, 29, 29},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
services__srv__IMUData_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {services__srv__IMUData_Event__TYPE_NAME, 26, 26},
      {services__srv__IMUData_Event__FIELDS, 3, 3},
    },
    {services__srv__IMUData_Event__REFERENCED_TYPE_DESCRIPTIONS, 4, 4},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = services__srv__IMUData_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = services__srv__IMUData_Response__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "#IMU_data.srv\n"
  "---\n"
  "float64 heading";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
services__srv__IMUData__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {services__srv__IMUData__TYPE_NAME, 20, 20},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 34, 34},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
services__srv__IMUData_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {services__srv__IMUData_Request__TYPE_NAME, 28, 28},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
services__srv__IMUData_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {services__srv__IMUData_Response__TYPE_NAME, 29, 29},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
services__srv__IMUData_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {services__srv__IMUData_Event__TYPE_NAME, 26, 26},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
services__srv__IMUData__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *services__srv__IMUData__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[3] = *services__srv__IMUData_Event__get_individual_type_description_source(NULL);
    sources[4] = *services__srv__IMUData_Request__get_individual_type_description_source(NULL);
    sources[5] = *services__srv__IMUData_Response__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
services__srv__IMUData_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *services__srv__IMUData_Request__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
services__srv__IMUData_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *services__srv__IMUData_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
services__srv__IMUData_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[5];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 5, 5};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *services__srv__IMUData_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[3] = *services__srv__IMUData_Request__get_individual_type_description_source(NULL);
    sources[4] = *services__srv__IMUData_Response__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
