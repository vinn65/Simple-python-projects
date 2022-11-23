import socket

import time
from datetime import datetime, timedelta
import random

HOST = "127.0.0.1"  

PORT = 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s = socket.socket()  
    s.connect((HOST, PORT)) 
    i = 0
    while i < 5:
         
        i = 0
        while i < 5:
            i = i+1
            message = input("Message: -> ")
            s.sendall(message.encode())
            data = s.recv(1024).decode()
            print("The message received from server is:  " + data)

            logical_clock = datetime.now()
            logical_clock = logical_clock + timedelta(minutes=random.randint(0, 59)) 
            
            print("Your logical clock: " + str(logical_clock))
            text = str(logical_clock)    
            s.sendall(text.encode())
            data = s.recv(1024).decode()
            
            i=0
            if i < 1:
                #convert data from a string to datetime type for comparison.
                clock = datetime.strptime(data, '%Y-%m-%d %H:%M:%S.%f') 
                diff = logical_clock - clock
                print("###########################################")
                print("Your clock has drifted by: " + str(diff) + " minutes")
                print("###########################################")
                print("Your Clock has been updated from: " + str(logical_clock) + " to: " + data)
                logical_clock = data # assign logical clock to the new value.
                print("New Updated Clock:" + str(logical_clock))
        

            else:
                print("Your clock is okay") 

            i = i + 1
            sleep_time = random.randint(0, 4)
            
            print("Sleeping for:" + str(sleep_time) + " Seconds")
            print("###########################################")
            print("###########################################")
            time.sleep(sleep_time)
    s.close()
    


