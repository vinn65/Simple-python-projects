"""
In a hotel, there are guests coming who may be registered or not. You'll find the list of registered guests along with their keys in the registrations.txt (you can copy the same in your solution).



Create a Guest class and store the registrations in it.
While initializing, pass the guest name and store it as name.

Then create a method is_regd() to print 'Registered' or 'Not Registered' when the guest is registered or not respectively.

Create a method get_key() to print the key of the guest.

Create another method, reg() to register the guest and assign a key to that guest from the below list of Keys (same can be found in the registrations.txt)

kys = [ 'A010','A012','A014','BQ01']

Also, print a message 'Sorry, no vacant rooms available' if there are no keys or the kys list becomes empty (when registering).



After creating the Guest class, receive the following guests (i.e. create objects for them):

Josh

Hans

Evan

Kyle

Ted

Karl

Sam

For each guest, you've to

print the name of the guest,

their registration condition,

print the Key if registered else register and then print the key like

Guest1                 # guest name using print(guest.name)
Not registered         # Using the guest.is_regd()
Key : A000             # Using guest.get_key()
"""



class Guest():

    def __init__(self, regs):
        self.dict = regs
    
    def showDict(self):
        print(self.dict)
    def is_regd(self, name):
        if name in self.dict:
            print("Registered")
        else:
            print("Not Registered")

    def get_key(self, name):
        for guest_name in self.dict:
            if guest_name == name:
                print(f"Key : {self.dict[guest_name].strip()}")
                return
        # print("Not Registered")

    def reg(self, name, keys):
        if keys:
            assigned_key = keys.pop(0)
            self.dict[name] = assigned_key
            # print(f"{assigned_key} was assigned")
        else:
            print("Sorry, no vacant rooms available.")
    
    def print_details(self):
        print(f"Guest: {self.name}")
        print(self.is_regd())
        print(self.get_key() if self.is_regd() == "Registered" else self.reg())

registrations = {
"John":"A011",
"Kyle":"A009",
"Jake":"BQ02",
"Tamra":"A015",
"Josh":"BQ03 ",
}

kys = [ 'A010','A012','A014','BQ01']
guests = ["Josh", "Hans", "Evan", "Kyle", "Ted", "Karl", "Sam"]

for guest_name in guests:
   guest = Guest(registrations)
   print(f"Guest\n{guest_name}")
   if guest_name not in registrations:
       guest.reg(guest_name, kys)
   guest.is_regd(guest_name)
   guest.get_key(guest_name)


   


