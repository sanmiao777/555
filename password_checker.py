"""
name: sanmiao xu
"""
def is_valid_password(text):
    return 8 <= len(text) <= 20 and "#" in text


def main():
    new_password = "s#sssssssss"
    print(f"{new_password} is a valid password?{is_valid_password(new_password)}")


main()
