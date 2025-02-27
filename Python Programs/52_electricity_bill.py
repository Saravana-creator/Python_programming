units=int(input("Enter the amount of units :"))
if(units<=100):
     tot_units=(units*5)
     print("The value is :",tot_units)
elif(units<=200):
     tot_units=(units*5)+(units-100)*7 
     print("The value is :",tot_units)
elif(units>=300):
     tot_units=(units*5)+(units*7)+(units-200)*10
     print("The value is :",tot_units)             