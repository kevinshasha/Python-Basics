
integer = False
while not integer:
    try:
        x = int(input ('enter an integer: '))
        integer = True
    except:
        print ('An integer is a whole number dickweed')
if x%2==0: 
    print('even')
else: 
    print('odd')

