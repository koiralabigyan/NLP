import re
text = "Contact us at info@example.com or call +9779812345678. The meeting is scheduled on 12/08/2024."

# 1. Extract Email Addresses
Email = re.findall(r'\b[\w.-]+@[\w.-]+\.[\w]{2,}', text)
print("Email:", Email)

# 2. Extract Phone Numbers
Phone = re.findall(r'\+?\d{2,4}[-\s]?\d{6,10}', text)
print("Phone number:", Phone)
  
# 3. Extract Dates
Date = re.findall(r'\b\d{1,2}/\d{1,2}/\d{4}\b', text)
print("Dates found:", Date)