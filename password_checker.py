"""
name: sanmiao xu
"""
def is_valid_password(text):
    return 8 <= len(text) <= 20


def main():
    new_password = "ssssssssss"
    print(f"{new_password} is a valid password?{is_valid_password(new_password)}")


main()
