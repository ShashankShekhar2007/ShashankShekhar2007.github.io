lst = [2, 4, 5, 6, 67, 54]
lst_reversed = lst[:]

for i in range(len(lst)//2):
    lst_reversed[i], lst_reversed[len(lst)-i-1] = lst_reversed[len(lst)-i-1], lst_reversed[i]
    
print(lst)
print(lst_reversed)