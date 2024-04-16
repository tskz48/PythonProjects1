

print("Hello")
x=input("Please type in your name.")
y=input("Please type in your birthday in the form dd/mm.")
if y[3:5] == '01':
    z='Aquarius' if int(y[0:2].lstrip('0')) >20 else 'Capricorn'
elif y[3:5]=='02':
    z='Pisces' if int(y[0:2].lstrip('0')) >18 else 'Aquarius'
elif y[3:5]=='03':
    z='Aries' if int(y[0:2].lstrip('0')) >20 else 'Pisces'
elif y[3:5]=='04':
    z='Taurus' if int(y[0:2].lstrip('0')) >19 else 'Aries'
elif y[3:5]=='05':
    z='Gemini' if int(y[0:2].lstrip('0')) >20 else 'Taurus'
elif y[3:5]=='06':
    z='Cancer' if int(y[0:2].lstrip('0')) >20 else 'Gemini'
elif y[3:5]=='07':
    z='Leo' if int(y[0:2].lstrip('0')) >22 else 'Cancer'
elif y[3:5]=='08':
    z='Virgo' if int(y[0:2].lstrip('0')) >22 else 'Leo'
elif y[3:5]=='09':
    z='Libra' if int(y[0:2].lstrip('0')) >22 else 'Virgo'
elif y[3:5]=='10':
    z='Scorpio' if int(y[0:2].lstrip('0')) >20 else 'Libra'
elif y[3:5]=='11':
     z='Sagittarius' if int(y[0:2].lstrip('0')) >21 else 'Scorpio'
elif y[3:5]=='12':
     z='Capricorn' if int(y[0:2].lstrip('0')) >21 else 'Sagittarius'

x.strip(' ')
x= x[0].upper()+x[1:].lower()# This capitalises only the first letter in the name.
f=open('zodiac.txt','a')
print(str(x)+", born on "+str(y)+", has zodiac sign "+str(z),file=f)
f.close()




