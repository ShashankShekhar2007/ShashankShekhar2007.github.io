# Divide the apples
try:
    print('****************************************************************')
    n = int(input('Enter the number of apples: '))
    mn = int(input('Enter the minimum number of apples: '))
    mx = int(input('Enter the maximum number of apples: '))
    print('****************************************************************')

    if mn>mx:
        print('\n*************************** ERROR *****************************')
        print("Minimum value is greater than the Maximim value.[You're a fool]")
        print('****************************************************************')
    elif mn!=mx:
        print('\n****************************************************************')
        for i in range(mn, mx+1):
            if n%i==0:
                print(f'{i} is divisor of {n} [-<*PASS*>-]')
            else:
                print(f'{i} is not divisor of {n}')
        print('****************************************************************')
    else:
        print('\n*************************** ERROR *****************************')
        print(f'{mn} & {mx} is not a range.')
        print('****************************************************************')

except ValueError:
    print('\n*************************** ERROR *****************************')
    print('Enter a natural number please.')
    print('****************************************************************')
