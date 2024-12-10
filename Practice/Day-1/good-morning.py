import time
current_time = time.strftime("%d-%m-%Y %H:%M:%S")
today = time.strftime("%H")
today=int(today)
if(today >= 12 and today<=17):
    print("Good Afternoon,Time is: ",current_time)
elif(today>17 and today<=21):
    print("Good Evening,Time is: ",current_time)
elif(today>21 and today<0):
    print("Good Night,Time is: ",current_time)
else:
    print("Good Morning,Time is: ",current_time)