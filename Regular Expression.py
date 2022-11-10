import re

expression = re.compile("\\w*(\\.\\w*)?@\\w*\\.[a-z]+(\\.[a-z]+)?", re.I) # re.I == re.IGNORECASE
# expression = re.compile("\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}")

s = expression.match("C@b.D")

print(s)
