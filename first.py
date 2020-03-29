name=input('Please enter you name... ')
if len(name)<3:
    name=input('Name can not be less than 3 character, Please enter name again')
elif len(name)>50:
    name=input('Name can not be more than 50 character, Please enter name again... ')
elif len(name)>3 and len(name)<=50:
    print('Thank you '+name+'! Your details have been submitted')