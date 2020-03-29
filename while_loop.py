i=1
while i<=3:
    i = i + 1
    choice = int(input('Please Guess the number... '))
    if choice==8:
        print('You Win!')
        break
    elif i==1 or i==2:
        print('Try Again')

else:
    print('You lost')



