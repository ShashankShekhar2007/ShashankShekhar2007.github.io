# Jumbled Names

from posixpath import split
import random
from colorama import Fore, Back, Style
first_name_list = []
last_name_list = []
final_name_list = []

def splitter(name):
    name = name.split(" ")
    first_name_list.append(name[0])
    last_name_list.append(name[1])

def jumbling_name(list_1, list_2):   
    for name in list_1:
        jumbled_last_name = random.choice(list_2)
        final_name_list.append(f"{name} {jumbled_last_name}")
        list_2.remove(jumbled_last_name)

if __name__=="__main__":

    list = []
    num = int(input(f"{Fore.BLUE}\n************************************************ {Style.BRIGHT}Entries{Style.RESET_ALL} {Fore.BLUE}********************************************\n{Style.BRIGHT}Enter number of people = "))
    for i in range(0,num):
        name = input(f"Enter Name No.{i+1} = ")
        list.append(name)

    for name in list:
        splitter(name)
    
    jumbling_name(first_name_list, last_name_list)
    print(f"{Style.RESET_ALL}{Fore.BLUE}\n******************************************** {Style.BRIGHT}Final Jumbled Names{Style.RESET_ALL} {Fore.BLUE}****************************************\n{Style.BRIGHT}")
    for name in final_name_list:
        print(name)