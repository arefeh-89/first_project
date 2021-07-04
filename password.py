import re

pattern = r"^[\w|\d|@|#|\$|%]{7,}\d$"
password = input('please enter a password: ')
psw = re.compile(password)
check = psw.search(pattern)
print(check)
