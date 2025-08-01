common_passwords = []

def strength_check():
    print("\n======== PASSWORD SECURITY ANALYZER =======\n")
    password = input("Enter password to analyze: ")

    length_check = False
    uppercase_check = False
    lowercase_check = False
    digit_check = False
    special_check = False
    common_check = False

    score = 0

    if len(password) > 7:
        length_check = True
        score += 20
    if password not in common_passwords:
        common_check = True
        score += 20

    for letter in password:
        if uppercase_check and lowercase_check and digit_check and special_check:
            break

        if not uppercase_check:
            if letter.isupper():
                uppercase_check = True
                score += 20
        if not lowercase_check:
            if letter.islower():
                lowercase_check = True
                score += 20
        if not digit_check:
            if letter.isdigit():
                digit_check = True
                score += 20
        if not special_check:
            if letter in "!@#$%^&*":
                special_check = True
                score += 20

    pass_strength = ""
    if score > 100:
        pass_strength = "Excellent"
    elif score > 80:
        pass_strength = "Strong"
    elif score > 60:
        pass_strength = "Good"
    elif score > 40:
        pass_strength = "Fair"
    else:
        pass_strength = "Weak"
    
    suggestions = []
    if not length_check:
        suggestions.append("Try using a password with at least 8 characters")
    if not common_check:
        suggestions.append("Avoid common password patterns")
    if not uppercase_check:
        suggestions.append("Try using a password with at least one uppercase character")
    if not lowercase_check:
        suggestions.append("Try using a password with at least one uppercase character")
    if not digit_check:
        suggestions.append("Try using a password with at least one digit")
    if not special_check:
        suggestions.append("Try using a password with at least a special character(!@#$%^&*)")

    
    print("\n🔒 SECURITY ANALYSIS RESULTS\n")
    print(f"Password: {password}\nScore: {score}/120 ({pass_strength})")

    results = {
        "Length requirement (8+ chars)":length_check, 
        "Contains uppercase letters":uppercase_check, 
        "Contains lowercase letters":lowercase_check, 
        "Contains numbers":digit_check, 
        "Contains special characters":special_check, 
        "Common password detected":common_check
    }
    
    for key, value in results.items():
        prefix = "✅" if value else "❌"
        print(f"\n{prefix} {key}")
    

    print(f"\n\n💡 SUGGESTIONS:\n- {"\n- ".join(suggestions)}")




strength_check()