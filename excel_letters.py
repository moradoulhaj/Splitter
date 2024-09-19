import string

# Generate single-letter column names
single_letters = list(string.ascii_uppercase)

# Generate double-letter column names
double_letters = [
    a + b for a in string.ascii_uppercase for b in string.ascii_uppercase
]

# Combine single and double-letter column names
excel_letters = single_letters + double_letters

# Limit to column AZ
index_az = excel_letters.index("ZZ") + 1
excel_letters = excel_letters[:index_az]
