from pip._vendor import requests
import pickle

# r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# r2 = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names")
#
# open('Text.txt', 'wb').write(r.content)
# open('Text2.txt', 'wb').write(r2.content)

rd = open('Text.txt')
rd = rd.read()
rd_lst = rd.split('\n')
file_obj = open('Text.pkl', 'wb')
pickle.dump(rd_lst, file_obj)
file_obj.close()

rd2 = open('Text2.txt')
rd2 = rd2.read()
rd_lst2 = rd2.split('\n')
file_obj2 = open('Text2.pkl', 'wb')
pickle.dump(rd_lst2, file_obj2)
file_obj2.close()

file_obj = open('Text.pkl', 'rb')
de_pickle = pickle.load(file_obj)
file_obj.close()
print(de_pickle)

file_obj2 = open('Text2.pkl', 'rb')
de_pickle2 = pickle.load(file_obj2)
file_obj2.close()
print(de_pickle2)
