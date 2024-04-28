import math
import calendar

''' Function to print the list elements'''
def printelements(param1):
    for i in param1:
        print("The elements are ",param1)

'''Function call to displa values in a list (homogeneous - same type pf values, they are mutable  -can be changed)'''
hobbies=['Sing','Paint','Play guitar']
Activities=['Sleep','Study']
printelements(hobbies)
printelements(Activities)

'''Dictionary example'''
teldir={'Karthik':9884702242}
print(teldir)
teldir['Imsa']=9500669810
print(teldir)
print(teldir['Karthik'])

for k,v in teldir.items():
    print ("The person ",k,"'s mobile number is ",v)

'''Tuples - Heterogeneous (any type of value)'''
coordinates=(3,4)
'''tuples are immuatble'''
'''coordinates[0]=100'''
''' Will throw error as the values cant be changes (immutable)'''

'''math module import'''
print ("The Ceil function ", math.ceil(1.23))
print ("The Round function ", math.floor(1.23))

''' Caledar module import'''
cal=calendar.month(1979,1)
'''print (cal)'''
