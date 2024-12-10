import time
from datetime import datetime
input_time = int(input("Enter Your time: "))
#strp time is used to convert
time_obj = datetime.strptime(str(input_time),"%H")
your_time = time_obj.strftime("%H")
# convert back to int
your_time = int(your_time)
if(your_time >= 12 and your_time<=17):
    print(f"Your entered time {your_time} corresponds to Afternoon")
elif(your_time>17 and your_time<=21):
    print(f"Your entered time {your_time} corresponds to Evening")
elif(your_time>21 and your_time<0):
    print(f"Your entered time {your_time} corresponds to Night ")
else:
    print(f"Your entered time {your_time} corresponds to Morning ")