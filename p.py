import socket

from datetime import datetime

import random, time
HOST = "127.0.0.1"

PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:       
    s.bind((HOST, PORT))
    s.listen()  
    conn, addr = s.accept()
    print("A connection from " + str(addr) + " has been established.")
    j = 0
    while j < 5:    
        i = 0
        while i < 1:
                i = i+1
                data = conn.recv(1024).decode()
                if not data:
                    time.sleep(9)
                print("The client says: " + str(data))
                data = input('Reply: -> ')
                conn.send(data.encode())  
                
                logical_clock = datetime.now() #P`s clock remains true (does not drift.) by using the .now() which gives the current time.  
                print("Your current clock time is: "+ str(logical_clock))
                i=0
                while i < 1:
                    i = i +1
                    new_data = conn.recv(1024).decode()
                    print("Q`s current time from it`s logical clock: " + (new_data))

                    # convert logical clock to a string for comparison with data which is a string.
                    logical_clock = str(logical_clock)
                    
                    if logical_clock < new_data: 
                        print("Q`s clock has drifted.Sending update...")
                        text = str(logical_clock) # send P`s logical clock to Q
                        print("Q`s clock has been updated to: " + str(logical_clock))
                        text = str(logical_clock)
                        conn.send(text.encode())
                    j = j + 1
                    sleep_time = random.randint(5, 9)
                    
                    print("Sleeping for:" + str(sleep_time) + " Seconds")
                    print("###########################################")
                    print("###########################################")
                    time.sleep(sleep_time)
    conn.close() 


