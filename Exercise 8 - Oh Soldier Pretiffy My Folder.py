import os


def soldier1(path, file, format_f):
    os.chdir(path)
    num = 1
    files = os.listdir(path)
    with open(file) as f:
        file_list = f.read()
        filelist = file_list.split("\n")
    for f2 in files:
        if f2 in filelist:
            pass
        if f2 not in filelist:
            os.rename(f2, f2.capitalize())
        if os.path.splitext(f2)[1] == format_f:
            os.rename(f2, f'{num}{format_f}')
            num += 1


soldier1(r'C:\Folder', r'C:\Folder\Do not touch.txt', '.jpg')





# def remover(file_names):
#     file = open(file_names)
#     file_r = file.read()
#     file_name = (file_r.split("\n"))
#     file.close()
#     return file_name
#
#
# def soldier(path, file_names, format_f):
#     os.chdir(path)
#     num = 1
#     file_name = remover(file_names)
#     for f in os.listdir():
#         file_n, file_f = os.path.splitext(f)
#         if file_f == f".{format_f}":
#             new_name = f"{str(num)}{file_f}"
#             num += 1
#             os.rename(f, new_name)
#             pass
#         if file_n not in file_name:
#             tn = file_n.title()
#             n_name = f'{tn}{file_f}'
#
#         else:
#             n_name = f'{file_n}{file_f}'
#         os.rename(f, n_name)
#
#
# soldier(r'C://Folder', 'Do Not Touch.txt', 'jpg')
