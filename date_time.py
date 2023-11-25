from datetime import datetime

time1 = datetime.now()
time2 = time1.strftime("%d/%m/%y %H:%M:%S")
print(time2)