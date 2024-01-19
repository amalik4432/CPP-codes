import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
if '04:00:00'<= timestamp <= '11:59:59':
    print("Good Morning")
elif '12:00:00'<= timestamp <= '15:59:59':
    print("Good Afternoon")
elif '16:00:00 '<= timestamp <= '19:59:59':
    print("Good Evening")
else:  #'20:00:00 '<= timestamp <= '23:59:59'
    print("Good Night")
input("Press Enter to continue...")

    

