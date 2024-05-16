number=1
pair=0
odd=0

while number!=0:
    number=float(input('Whrite a number diferent of 0: '))


    if number!=0:
        if number%2==0:
            pair+=1
        else:
            odd+=1

print(f'have {pair} numbers if are pair, and have {odd} numbers odd')