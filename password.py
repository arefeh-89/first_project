import re

pattern = r"^[\w|\d|@|#|\$|%]{7,}\d$"
password = input('please enter a password: ')
psw1 = re.compile(password)
check = psw1.search(pattern)
print(check)
