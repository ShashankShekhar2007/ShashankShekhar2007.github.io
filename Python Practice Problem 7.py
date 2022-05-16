# Python Practice Problem 7:- Search Engine

lst = ["if you're visiting this page", "you're likely here because you're searching for a random sentence.", "sometimes a random word just isn't enough","and that is where the random sentence generator comes into play.",
       "by inputting the desired number","you can make a list of as many random sentences as you want or need.", "producing random sentences can be helpful in a number of different ways."]


inp = input("Enter a Querry: ")
output = []
for sentence in lst:
    words = sentence.split(' ')
    if inp.lower() in words:
        output.append(sentence)
    else:
        pass
print('************************************************************************')

print(f'Search Results: "{len(output)} Result(s) found."\n')
num = 0
for sentence in output:
    print(f'{num+1}.{sentence}')
    num = num+1

print('************************************************************************')
