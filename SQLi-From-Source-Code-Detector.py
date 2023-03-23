import re

# Read the web application source code from a text file
with open('web_app_source_code.txt', 'r') as f:
    source_code = f.read()

# Regular expression pattern to match potential SQL injection attacks
sql_injection_pattern = r"(?i)\b(SELECT|UPDATE|DELETE|INSERT|DROP|UNION|AND|OR)\b"

# Search for matches of the pattern in the source code
matches = re.findall(sql_injection_pattern, source_code)

if matches:
    print("Potential SQL injection vulnerabilities found:")
    for match in set(matches):
        print("- " + match)
else:
    print("No potential SQL injection vulnerabilities found.")
