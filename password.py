import re

pattern = r"^[\w|\d|@|#|\$|%]{7,}\d$"
password = input('please enter a password: ')
psw12 = re.compile(password)
check = psw12.search(pattern)
print(check)
