import pickle

lst = ['Shashank', 'Captain America', 'Tony Stark', 'Thor Odinson']
file_name = 'Names.pkl'
file_object = open(file_name, 'wb')
# 'wb' format is to write in binary form.
pickle.dump(lst, file_object)
file_object.close()

file_object = open(file_name, 'rb')
# 'rb' format is to read the file written in binary.
de_pickle = pickle.load(file_object)
file_object.close()
print(de_pickle)
# the function 'pickles.loads is used to read the data of byte string.