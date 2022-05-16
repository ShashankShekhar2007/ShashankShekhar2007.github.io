import re

string_a = "Hello, My name is Shashank Shekhar. My E-Mail I'd is golukv39@gmail.com, " \
           "shashank.shekhar.singh.2007@gmail.com "
# matches = re.findall(r'\w+@\S+\w', string_a)
matches = re.findall(r'[0-9a-z-A-Z._+%]+[@][0-9a-z-A-Z._+%]+[.][0-9a-z-A-Z.]+', string_a)
print(matches)
