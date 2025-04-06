// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from services:srv/KalmanState.idl
// generated code does not contain a copyright notice

#include "services/srv/detail/kalman_state__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_services
const rosidl_type_hash_t *
services__srv__KalmanState__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xb5, 0x1a, 0x00, 0x6a, 0xe7, 0xcc, 0x38, 0x84,
      0x03, 0xe8, 0x90, 0xcd, 0x10, 0x60, 0xe6, 0x53,
      0x72, 0xec, 0x21, 0x0c, 0xfe, 0xa8, 0x5a, 0xe5,
      0xd0, 0xa3, 0x36, 0xbf, 0xef, 0x45, 0xee, 0xc2,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_services
const rosidl_type_hash_t *
services__srv__KalmanState_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xd5, 0x4c, 0x26, 0xed, 0xf8, 0x8f, 0xf9, 0x42,
      0x3f, 0xff, 0x42, 0xf3, 0xab, 0xe1, 0x6f, 0x19,
      0xdf, 0x0c, 0x07, 0x53, 0x8b, 0x12, 0x68, 0xe7,
      0x35, 0x66, 0xdf, 0x8f, 0xd9, 0xd9, 0x30, 0x50,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_services
const rosidl_type_hash_t *
services__srv__KalmanState_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x9c, 0xb3, 0xb8, 0x69, 0xa4, 0x27, 0x50, 0xdc,
      0x7d, 0xcd, 0x4e, 0x46, 0xab, 0xd4, 0xe1, 0x5f,
      0xf1, 0x66, 0x07, 0xb0, 0x5f, 0x52, 0xf1, 0xb1,
      0xc0, 0x5d, 0xd2, 0x7a, 0x36, 0x02, 0xde, 0xcc,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_services
const rosidl_type_hash_t *
services__srv__KalmanState_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xc0, 0xdd, 0x77, 0x62, 0x08, 0x8b, 0x59, 0x2d,
      0x90, 0x4b, 0x29, 0xd2, 0x4c, 0xb4, 0xfd, 0x49,
      0x69, 0x2d, 0xff, 0x8c, 0x79, 0xec, 0x5a, 0x53,
      0x77, 0x33, 0x7c, 0x29, 0x7e, 0x47, 0x60, 0x92,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "service_msgs/msg/detail/service_event_info__functions.h"
#include "std_msgs/msg/detail/float32_multi_array__functions.h"
#include "std_msgs/msg/detail/multi_array_dimension__functions.h"
#include "std_msgs/msg/detail/multi_array_layout__functions.h"

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
static const rosidl_type_hash_t std_msgs__msg__Float32MultiArray__EXPECTED_HASH = {1, {
    0x05, 0x99, 0xf6, 0xf8, 0x5b, 0x4b, 0xfc, 0xa3,
    0x79, 0x87, 0x3a, 0x0b, 0x43, 0x75, 0xa0, 0xac,
    0xa0, 0x22, 0x15, 0x6b, 0xd2, 0xd7, 0x02, 0x12,
    0x75, 0xd1, 0x16, 0xed, 0x1f, 0xa8, 0xbf, 0xe0,
  }};
static const rosidl_type_hash_t std_msgs__msg__MultiArrayDimension__EXPECTED_HASH = {1, {
    0x5e, 0x77, 0x3a, 0x60, 0xa4, 0xc7, 0xfc, 0x8a,
    0x54, 0x98, 0x5f, 0x30, 0x7c, 0x78, 0x37, 0xaa,
    0x29, 0x94, 0x25, 0x2a, 0x12, 0x6c, 0x30, 0x19,
    0x57, 0xa2, 0x4e, 0x31, 0x28, 0x2c, 0x9c, 0xbe,
  }};
static const rosidl_type_hash_t std_msgs__msg__MultiArrayLayout__EXPECTED_HASH = {1, {
    0x4c, 0x66, 0xe6, 0xf7, 0x8e, 0x74, 0x0a, 0xc1,
    0x03, 0xa9, 0x4c, 0xf6, 0x32, 0x59, 0xf9, 0x68,
    0xe4, 0x8c, 0x61, 0x7e, 0x76, 0x99, 0xe8, 0x29,
    0xb6, 0x3c, 0x21, 0xa5, 0xcb, 0x50, 0xda, 0xc6,
  }};
#endif

static char services__srv__KalmanState__TYPE_NAME[] = "services/srv/KalmanState";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";
static char services__srv__KalmanState_Event__TYPE_NAME[] = "services/srv/KalmanState_Event";
static char services__srv__KalmanState_Request__TYPE_NAME[] = "services/srv/KalmanState_Request";
static char services__srv__KalmanState_Response__TYPE_NAME[] = "services/srv/KalmanState_Response";
static char std_msgs__msg__Float32MultiArray__TYPE_NAME[] = "std_msgs/msg/Float32MultiArray";
static char std_msgs__msg__MultiArrayDimension__TYPE_NAME[] = "std_msgs/msg/MultiArrayDimension";
static char std_msgs__msg__MultiArrayLayout__TYPE_NAME[] = "std_msgs/msg/MultiArrayLayout";

// Define type names, field names, and default values
static char services__srv__KalmanState__FIELD_NAME__request_message[] = "request_message";
static char services__srv__KalmanState__FIELD_NAME__response_message[] = "response_message";
static char services__srv__KalmanState__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field services__srv__KalmanState__FIELDS[] = {
  {
    {services__srv__KalmanState__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {services__srv__KalmanState_Request__TYPE_NAME, 32, 32},
    },
    {NULL, 0, 0},
  },
  {
    {services__srv__KalmanState__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {services__srv__KalmanState_Response__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {services__srv__KalmanState__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {services__srv__KalmanState_Event__TYPE_NAME, 30, 30},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription services__srv__KalmanState__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {services__srv__KalmanState_Event__TYPE_NAME, 30, 30},
    {NULL, 0, 0},
  },
  {
    {services__srv__KalmanState_Request__TYPE_NAME, 32, 32},
    {NULL, 0, 0},
  },
  {
    {services__srv__KalmanState_Response__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__Float32MultiArray__TYPE_NAME, 30, 30},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__MultiArrayDimension__TYPE_NAME, 32, 32},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__MultiArrayLayout__TYPE_NAME, 29, 29},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
services__srv__KalmanState__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {services__srv__KalmanState__TYPE_NAME, 24, 24},
      {services__srv__KalmanState__FIELDS, 3, 3},
    },
    {services__srv__KalmanState__REFERENCED_TYPE_DESCRIPTIONS, 8, 8},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = services__srv__KalmanState_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = services__srv__KalmanState_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[4].fields = services__srv__KalmanState_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__Float32MultiArray__EXPECTED_HASH, std_msgs__msg__Float32MultiArray__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[5].fields = std_msgs__msg__Float32MultiArray__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__MultiArrayDimension__EXPECTED_HASH, std_msgs__msg__MultiArrayDimension__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[6].fields = std_msgs__msg__MultiArrayDimension__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__MultiArrayLayout__EXPECTED_HASH, std_msgs__msg__MultiArrayLayout__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[7].fields = std_msgs__msg__MultiArrayLayout__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char services__srv__KalmanState_Request__FIELD_NAME__structure_needs_at_least_one_member[] = "structure_needs_at_least_one_member";

static rosidl_runtime_c__type_description__Field services__srv__KalmanState_Request__FIELDS[] = {
  {
    {services__srv__KalmanState_Request__FIELD_NAME__structure_needs_at_least_one_member, 35, 35},
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
services__srv__KalmanState_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {services__srv__KalmanState_Request__TYPE_NAME, 32, 32},
      {services__srv__KalmanState_Request__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char services__srv__KalmanState_Response__FIELD_NAME__state[] = "state";

static rosidl_runtime_c__type_description__Field services__srv__KalmanState_Response__FIELDS[] = {
  {
    {services__srv__KalmanState_Response__FIELD_NAME__state, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {std_msgs__msg__Float32MultiArray__TYPE_NAME, 30, 30},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription services__srv__KalmanState_Response__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {std_msgs__msg__Float32MultiArray__TYPE_NAME, 30, 30},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__MultiArrayDimension__TYPE_NAME, 32, 32},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__MultiArrayLayout__TYPE_NAME, 29, 29},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
services__srv__KalmanState_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {services__srv__KalmanState_Response__TYPE_NAME, 33, 33},
      {services__srv__KalmanState_Response__FIELDS, 1, 1},
    },
    {services__srv__KalmanState_Response__REFERENCED_TYPE_DESCRIPTIONS, 3, 3},
  };
  if (!constructed) {
    assert(0 == memcmp(&std_msgs__msg__Float32MultiArray__EXPECTED_HASH, std_msgs__msg__Float32MultiArray__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = std_msgs__msg__Float32MultiArray__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__MultiArrayDimension__EXPECTED_HASH, std_msgs__msg__MultiArrayDimension__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = std_msgs__msg__MultiArrayDimension__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__MultiArrayLayout__EXPECTED_HASH, std_msgs__msg__MultiArrayLayout__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = std_msgs__msg__MultiArrayLayout__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char services__srv__KalmanState_Event__FIELD_NAME__info[] = "info";
static char services__srv__KalmanState_Event__FIELD_NAME__request[] = "request";
static char services__srv__KalmanState_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field services__srv__KalmanState_Event__FIELDS[] = {
  {
    {services__srv__KalmanState_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {services__srv__KalmanState_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {services__srv__KalmanState_Request__TYPE_NAME, 32, 32},
    },
    {NULL, 0, 0},
  },
  {
    {services__srv__KalmanState_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {services__srv__KalmanState_Response__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription services__srv__KalmanState_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {services__srv__KalmanState_Request__TYPE_NAME, 32, 32},
    {NULL, 0, 0},
  },
  {
    {services__srv__KalmanState_Response__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__Float32MultiArray__TYPE_NAME, 30, 30},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__MultiArrayDimension__TYPE_NAME, 32, 32},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__MultiArrayLayout__TYPE_NAME, 29, 29},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
services__srv__KalmanState_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {services__srv__KalmanState_Event__TYPE_NAME, 30, 30},
      {services__srv__KalmanState_Event__FIELDS, 3, 3},
    },
    {services__srv__KalmanState_Event__REFERENCED_TYPE_DESCRIPTIONS, 7, 7},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = services__srv__KalmanState_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = services__srv__KalmanState_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__Float32MultiArray__EXPECTED_HASH, std_msgs__msg__Float32MultiArray__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = std_msgs__msg__Float32MultiArray__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__MultiArrayDimension__EXPECTED_HASH, std_msgs__msg__MultiArrayDimension__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[5].fields = std_msgs__msg__MultiArrayDimension__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__MultiArrayLayout__EXPECTED_HASH, std_msgs__msg__MultiArrayLayout__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[6].fields = std_msgs__msg__MultiArrayLayout__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "#Kalman_State.srv\n"
  "---\n"
  "std_msgs/Float32MultiArray state";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
services__srv__KalmanState__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {services__srv__KalmanState__TYPE_NAME, 24, 24},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 54, 54},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
services__srv__KalmanState_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {services__srv__KalmanState_Request__TYPE_NAME, 32, 32},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
services__srv__KalmanState_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {services__srv__KalmanState_Response__TYPE_NAME, 33, 33},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
services__srv__KalmanState_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {services__srv__KalmanState_Event__TYPE_NAME, 30, 30},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
services__srv__KalmanState__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[9];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 9, 9};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *services__srv__KalmanState__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[3] = *services__srv__KalmanState_Event__get_individual_type_description_source(NULL);
    sources[4] = *services__srv__KalmanState_Request__get_individual_type_description_source(NULL);
    sources[5] = *services__srv__KalmanState_Response__get_individual_type_description_source(NULL);
    sources[6] = *std_msgs__msg__Float32MultiArray__get_individual_type_description_source(NULL);
    sources[7] = *std_msgs__msg__MultiArrayDimension__get_individual_type_description_source(NULL);
    sources[8] = *std_msgs__msg__MultiArrayLayout__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
services__srv__KalmanState_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *services__srv__KalmanState_Request__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
services__srv__KalmanState_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[4];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 4, 4};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *services__srv__KalmanState_Response__get_individual_type_description_source(NULL),
    sources[1] = *std_msgs__msg__Float32MultiArray__get_individual_type_description_source(NULL);
    sources[2] = *std_msgs__msg__MultiArrayDimension__get_individual_type_description_source(NULL);
    sources[3] = *std_msgs__msg__MultiArrayLayout__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
services__srv__KalmanState_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[8];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 8, 8};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *services__srv__KalmanState_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[3] = *services__srv__KalmanState_Request__get_individual_type_description_source(NULL);
    sources[4] = *services__srv__KalmanState_Response__get_individual_type_description_source(NULL);
    sources[5] = *std_msgs__msg__Float32MultiArray__get_individual_type_description_source(NULL);
    sources[6] = *std_msgs__msg__MultiArrayDimension__get_individual_type_description_source(NULL);
    sources[7] = *std_msgs__msg__MultiArrayLayout__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
