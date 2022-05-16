# Palindromifying the List
inp = int(input("Enter the list length = "))
lst = []
for i in range(1,inp+1):
    lst.append(int(input(f"{i}. ")))
def func(n):
    n_str = str(n)
    l = []
    for i in n_str:
        l.append(i)
    l2=l[:]
    l2.reverse()
    if l2 == l:
        lst_2.append(n)
    elif l2 != l:
        func(n+1)

lst_2 = []
for i in lst:
    if i>=10:
        func(i)
    else:
        lst_2.append(i)
print("\n**********************************************")
print(f'Your entered list is {lst}')
print("**********************************************")
print(f'Your Palindromified list is {lst_2}')
print("**********************************************\n")
