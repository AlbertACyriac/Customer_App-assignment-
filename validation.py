def is_valid_email(email):
    return "@" in email and "." in email

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10