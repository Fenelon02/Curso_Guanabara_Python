gender=input('Are you a man or a whoman? [M/W]: ')

gender=gender.upper()
gender=gender.strip()

if gender=='M' or gender=='W':
    print('you whrite rigth')

else:
    while gender!='M' or gender!='W':

        gender=input('Are you a man or a whoman? [M/W]: ')
        gender=gender.upper()
        gender=gender.strip()

        if gender=='M' or gender=='W':
            print('You whrite rigth')
            break
        else:
            print('whrite again, the way you whrite is wrong.')


