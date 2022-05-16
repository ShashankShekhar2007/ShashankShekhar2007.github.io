# The Next Palindrome

inp = int(input('\n**********************************************\n\nEnter a Number = '))

def func(n):
    n_str = str(n)
    l = []
    for i in n_str:
        l.append(i)
    l2=l[:]
    l2.reverse()
    if l2 == l:
        print(f"The number '{n}' is the nearest Palindrome to '{inp}'")
        print("\n**********************************************\n")
    elif l2 != l:
        func(n+1)
    else:
        print('Something is Wrong')
        print("\n**********************************************")
    

func(inp)