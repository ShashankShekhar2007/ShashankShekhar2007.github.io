# == : is used to check value equality.
# is : is used to check refrence refer to an object equality.

a = [34, 43, 3]
b = a
print(a==b)
print(a is b)
# Now try to make a copy of list 'a' as 'c' and try to check the refrence equality of that.
c = a[:]
print(c == a)
print(c is a)
# Now you can see that the value is 'False'.
# This is because 'c' is a copy or actually looks like list 'a' , but they are not same value i.e list 'a'.


# Now, lst's get another example:
print("***********Result of another example*************")
a_var = [12, 'hello', 148]
b_var = [12, 'hello', 148]
print(a_var == b_var)
print(a_var is b_var)
# You can see that the value of 'a_var' is equal to 'b_var' but both objects are not same they are different.
# You can often make them refrence same by not creating a new list of 'b_var', and just add a '=' sign as we done in our first example.
