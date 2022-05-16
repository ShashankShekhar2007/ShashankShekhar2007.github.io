import re
"""
Meta Characters
[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group
Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

\d Returns a match where the string contains digits (numbers from 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string
"""

str_0 = '''PyCharm 2020.3.3 (Community Edition) Build #PC-203.7148.72, built on January 27, 2021 Runtime version: 
11.0.9.1 11-1145.77 amd64  VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o. Windows 10 10.0 GC: ParNew, 
ConcurrentMarkSweep Memory: 733M Cores: 2'''

# pattern = re.compile(r"20")
# pattern = re.compile(r".JDK")
# pattern = re.compile(r"^Py")
# pattern = re.compile(r"2$")
# pattern = re.compile(r"Com*")
# pattern = re.compile(r"Com+")
# pattern = re.compile(r"73{2}")
# pattern = re.compile(r"(20){2}")
# pattern = re.compile(r"20|21")

# Special Sequences
# pattern = re.compile(r"\APy")
# pattern = re.compile(r"\bOp")
# pattern = re.compile(r"res\b")
pattern = re.compile(r"\d{2}-\d{4}.\d{2}")
matches = pattern.finditer(str_0)
for match in matches:
    print(match)

phone = '''+91 9867236485, +91 7838492057, +91 9074639264'''
pattern_2 = re.compile(r'\d{2} \d{10}')
matches_2 = pattern_2.finditer(phone)
for match in matches_2:
    print(match)
