import _datetime

while(True): #this is sometimes referred to as an infinite loop
    city=input("Enter the name of your current city")
    current_time=_datetime.datetime.now()
    hour=current_time.hour
    minute= current_time.minute
    second=current_time.second

    if city=="Hamburg":
        hour=hour+9
        print (hour)
    elif city== "Chicago":
        hour= hour-10
        print (hour)
    elif city=="Kigali":
        hour= hour+1
        print (hour)
    elif city=="exit":
        break

print("The city is yet to be logged into our database")

