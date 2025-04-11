def check_password_strength():
    password= input("Enter your password: ") 
    has_upper =any (char.isupper() for char in password) 
    has_lower =any (char.islower() for char in password) 
    has_digit =any (char.isdigit() for char in password) 
    is_long_enough = len(password) >= 8 
    print("\nPassword Strength Check:") 
    if has_upper and has_lower and has_digit and is_long_enough:
        print(" Password is strong.") 
    else:
        print("X Password is weak. Please ensure it has:") 
        if not has_upper: 
            print("- At least one uppercase letter") 
        if not has_lower: 
            print("- At least one lowercase letter") 
        if not has_digit: 
            print("- At least one digit") 
        if not is_long_enough: 
            print("- Minimum 8 characters") 
check_password_strength()
