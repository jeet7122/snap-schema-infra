from utils.validators.duplicate_index_validator import (
    validate_duplicate_indexes
)

from utils.validators.foreign_key_validator import (
    validate_foreign_key_indexes
)

from utils.validators.timestamp_validator import (
    validate_timestamps
)

from utils.validators.enum_validator import (
    validate_enum_modeling
)

from utils.validators.composite_index_validator import (
    validate_composite_indexes
)


def run_validators(schema):

    warnings = []

    warnings.extend(
        validate_duplicate_indexes(schema)
    )

    warnings.extend(
        validate_foreign_key_indexes(schema)
    )

    warnings.extend(
        validate_timestamps(schema)
    )

    warnings.extend(
        validate_enum_modeling(schema)
    )

    warnings.extend(
        validate_composite_indexes(schema)
    )

    return warnings