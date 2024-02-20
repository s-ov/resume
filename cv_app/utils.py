import re


def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    pattern = re.compile(email_regex)

    if re.match(pattern, email):
        return True
    else:
        return False

if __name__ == '__main__':
    email = "example@example.com"
    if validate_email(email):
        print("Valid email address")
    else:
        print("Invalid email address")
