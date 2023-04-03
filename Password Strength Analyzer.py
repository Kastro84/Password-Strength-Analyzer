import re

def password_strength(password):
    # Calculate the length of the password
    length = len(password)
    
    # Check for uppercase letters
    uppercase = bool(re.search(r'[A-Z]', password))
    
    # Check for lowercase letters
    lowercase = bool(re.search(r'[a-z]', password))
    
    # Check for digits
    digits = bool(re.search(r'\d', password))
    
    # Check for special characters
    special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Calculate the strength score based on the above checks
    score = length + (5 if uppercase else 0) + (5 if lowercase else 0) + (5 if digits else 0) + (5 if special else 0)
    
    # Determine the password strength category based on the score
    if score >= 20:
        return "Very Strong"
    elif score >= 15:
        return "Strong"
    elif score >= 10:
        return "Moderate"
    else:
        return "Weak"
        
        # Example passwords to test the password strength analyzer
passwords = ["aBcDeFgH123!@#", "myp4ssw0rd!", "qwertyuiop", "1234567890", "pa$$word"]

# Test each password with the password strength analyzer
for password in passwords:
    strength = password_strength(password)
    print(f"The strength of the password '{password}' is '{strength}'")