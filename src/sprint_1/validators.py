import re


def extract_emails(text):

    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|br)\b'

    emails = re.findall(pattern, text)

    full_emails = re.finditer(
        r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(?:com|org|net|br)\b',
        text
    )

    return [email.group() for email in full_emails]


def validate_employee_ids(employee_ids):

    valid_pattern = r'^[A-Z]{3}-\d{4}$'

    valid_ids = []
    invalid_ids = []

    for employee_id in employee_ids:

        if re.match(valid_pattern, employee_id):
            valid_ids.append(employee_id)
        else:
            invalid_ids.append(employee_id)

    return valid_ids, invalid_ids