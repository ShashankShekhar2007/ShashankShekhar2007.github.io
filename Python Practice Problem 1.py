current_year = int(input("Enter Current Year = "))

if current_year>1900:
    age = int(input("Enter your 'Age' or 'Year of Birth = "))
    if age>1900:
        birth_year = age

    elif age<150:
        birth_year = current_year-age
    
    while True:
        q = input("\n1.Know when you'll become 100 years old\n2.Know your age in a particular year\nEnter question number to continue or 'q' to quit = ")

        if q == '1':
            print('\n**********************************************')
            print(f"You'll turn 100 in '{birth_year+100}'")
            print('**********************************************')

        elif q == '2':
            print('\n**********************************************')
            q2 = input('Enter the Year = ')
            try:
                if int(q2)<=birth_year:
                    print('You are not yet born...')
                elif int(q2)>birth_year and int(q2)>150:
                    print(f"You'll turn '{int(q2)-birth_year}' in '{int(q2)}'")
                    print('**********************************************')
                else:
                    print('Wrong Input!!!!')
                    print('**********************************************')
            except Exception as e:
                print('**********************************************')
                print('Wrong Input!!!')
                print('**********************************************')
        elif q.lower() == 'q':
            quit()
            
        else:
            print('Wrong Input!!!')
            print('**********************************************')
else:
    print('Plese enter a correct Year!!!')       
