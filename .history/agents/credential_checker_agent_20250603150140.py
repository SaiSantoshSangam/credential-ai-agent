import re

def find_credentials(text):
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\b\d{10}\b', text)
    password = re.findall(r'password\s*[:=]\s*(\S+)', text, re.IGNORECASE)
    return email, phone, password
