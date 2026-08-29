def validate_name(full_name):
    if full_name is None: return False, "Full Name is blank or missing"

    if not isinstance(full_name, str):
        return False, "Type mismatch: Name must be a text string"

    if any(char.isdigit() for char in full_name):
        return False, f"Invalid entry: Name '{full_name}' contains numbers."

    return True, None

def validate_age(age, age_schema):
    if age is None:
        return False, "Age is blank or missing"

    try:
        age = int(age)
    except (ValueError, TypeError):
        return False, f"Type mismatch: 'age' value '{age}' cannot convert to Integer."

    min_age = age_schema.get("min")
    max_age = age_schema.get("max")

    if not ((min_age is None or age >= min_age) and (max_age is None or age <= max_age)):
        return False, f"Out of range: age ({age}) must be between {min_age} and {max_age}."
    else:
        return True, None


def validate_credit(credit, credit_schema):
    if credit is None: return False, "Credit is blank or missing"

    try:
        credit = int(credit)
    except (ValueError, TypeError):
        return False, f"Type mismatch: 'credit' value '{credit}' cannot convert to Integer."

    min_credit = credit_schema.get("min")
    max_credit = credit_schema.get("max")

    if (min_credit is None or credit >= min_credit) and (max_credit is None or credit <= max_credit):
        return True, None
    else:
        return False, f"Out of range: credit ({credit}) must be between {min_credit} and {max_credit}."


def validate_gender(gender, gender_schema):
    if gender is None: return False, "gender is blank or missing"

    if not isinstance(gender, str):
        return False, f"Type mismatch: 'gender' must be a text string, got {type(gender).__name__}."

    gender = gender.upper()

    allowed_options = gender_schema.get("allowed")
    if gender not in allowed_options:
        return False, f"Invalid category: 'gender' value '{gender}' must be one of {allowed_options}."

    return True, None


def validate_income(income, income_schema):
    if income is None:
        return False, "Income is blank or missing"

    try:
        income = int(income)
    except (ValueError, TypeError):
        return False, f"Type mismatch: 'income' value '{income}' cannot convert to Integer."

    min_income = income_schema.get("min")
    max_income = income_schema.get("max")

    if (min_income is None or income >= min_income) and (max_income is None or income <= max_income):
        return True, None
    else:
        return False, f"Out of range: income ({income}) must be between {min_income} and {max_income}."


def validate_record(record, validator_schema):
    errors = []

    for field in validator_schema.keys():
        if field not in record:
            errors.append(f"Missing field: '{field}' is required.")

    # Validates Full Name
    is_letters_only, name_error = validate_name(record.get("full_name"))
    if not is_letters_only: errors.append(name_error)

    # Validates Age
    age_rules = validator_schema.get("age")
    is_age_ok, age_error = validate_age(record.get("age"), age_rules)
    if not is_age_ok: errors.append(age_error)

    # Validates Income
    income_rules = validator_schema.get("income")
    is_income_valid, income_error = validate_income(record.get("income"), income_rules)
    if not is_income_valid: errors.append(income_error)

    # Validates Credit
    credit_rules = validator_schema.get("credit")
    is_credit_valid, credit_errors = validate_credit(record.get("credit"), credit_rules)
    if not is_credit_valid: errors.append(credit_errors)

    # Validate gender
    gender_rules = validator_schema.get("gender")
    is_gender_valid, gender_errors = validate_gender(record.get("gender"), gender_rules)
    if not is_gender_valid: errors.append(gender_errors)

    is_valid = len(errors) == 0

    return is_valid, errors


def validate_dataset(dataset, global_schema):
    passed_list = {}
    failed_list = {}

    for person, record in dataset.items():
        is_valid, error_logs = validate_record(record, global_schema)

        if is_valid:
            passed_list[person] = record
        else:
            failed_list[person] = {
                "record" : record,
                "errors": error_logs
            }

    return passed_list, failed_list


dealership_leads = {
    # Perfect, clean records
    "person1": {"full_name": "Tyrannosaurus", "age": 16, "gender": "M", "income": 50000, "credit": 810},
    "person2": {"full_name": "Ankylosaurus", "age": 34, "gender": "F", "income": 95000, "credit": 820},
    "person3": {"full_name": "Stegosaurus", "age": 45, "gender": "O", "income": 100000, "credit": 980},

    # Messy data but valid format
    "person4": {"full_name": "Rex Doe", "age": "28", "gender": "M", "income": "62000", "credit": 740},
    "person5": {"full_name": "Rex Buck", "age": 19, "gender": "M", "income": 25000.50, "credit": "580"},

    # Invalid age scenarios
    "person6": {"full_name": "Blue Raptor", "age": 4, "gender": "O", "income": 0, "credit": 400},
    "person7": {"full_name": "Charlie Raptor", "age": 250, "gender": "M", "income": 500000, "credit": 850},
    "person8": {"full_name": "Velociraptor", "age": "twenty", "gender": "M", "income": 45000, "credit": 600},

    # Invalid credit scenarios
    "person9": {"full_name": "Carnotaurus", "age": 32, "gender": "M", "income": 9999999, "credit": 250},
    "person10": {"full_name": "Allosaurus", "age": 42, "gender": "M", "income": 8500000, "credit": 900},

    # Invalid Name
    "person11": {"full_name": "Bumpy872334", "age": 32, "gender": "M", "income": 9999999, "credit": 250},

    # Missing fields or Null values
    "person12": {"full_name": "Brachiosaurus", "age": 29, "gender": "F", "income": 70000},
    "person13": {"full_name": "Mosasaurus", "age": 18, "gender": "M", "income": None, "credit": 550},
    "person14": {"full_name": "Spinosaurus", "age": 18, "gender": "M"},
    "person15": {"full_name": "123Bad", "age": 18, "gender": "M"}
}

schema = {
    "full_name": {type: str},
    "age": {type: int, "min": 16, "max": 110},
    "gender": {type: str, "allowed": ["M", "F", "O"]},
    "income": {type: int, "min": 50000, "max": None},
    "credit": {type: int, "min": 770, "max": None},
}

# ----- Mock Test -----
if __name__ == "__main__":
    passed, failed = validate_dataset(dealership_leads, schema)

    print(f"=== PASSED / VERIFIED BUYERS ({len(passed)}) ===")
    for person_id, clear_record in passed.items():
        print(f"✅ {person_id}: {clear_record}")

    print(f"\n=== QUARANTINE LIST / FAILS ({len(failed)}) ===")
    for person_id, failure_payload in failed.items():
        print(f"❌ {person_id}:")

        # 1. Unpack the original data record using the exact key you defined
        print(f"   Record: {failure_payload['record']}")

        print(f"   Errors Found:")

        # 2. Directly loop through the errors you already computed!
        # No more re-running validate_record or ghost errors.
        for single_error in failure_payload["errors"]:
            print(f"     - {single_error}")