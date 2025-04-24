email = input("Enter your Email:")

# Initialize flags
k, j, d = 0, 0, 0

if len(email) >= 6:
    # Check if the first character is an alphabet
    if email[0].isalpha():
        # Check one "@" in the email
        if "@" in email and email.count("@") == 1:
            # Check for valid domain ending
            if email[-4] == "." or email[-3] == ".":
                for i in email:
                    # Check for spaces
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        # Check for uppercase letters
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in "_@.":
                        continue
                    else:
                        d = 1

                # Check flags and print appropriate message
                if k == 1 or j == 1 or d == 1:
                    print("Invalid email (contains invalid characters)")
                else:
                    print("Valid email")
            else:
                print("Invalid email (domain ending is incorrect)")
        else:
            print("Invalid email (must contain one '@')")
    else:
        print("Invalid email (first character must be an alphabet)")
else:
    print("Invalid email (length must be at least 6 characters)")
