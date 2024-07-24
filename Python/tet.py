class Guest:
    registrations = {
        "John": "A011",
        "Kyle": "A009",
        "Jake": "BQ02",
        "Tamra": "A015",
        "Josh": "BQ03"
    }
    keys = ['A010', 'A012', 'A014', 'BQ01']
    
    def __init__(self, name):
        self.name = name
        self.key = None
    
    def is_regd(self):
        return 'Registered' if self.name in Guest.registrations else 'Not Registered'
    
    def get_key(self):
        if self.key:
            print(f"Key : {self.key}")
        else:
            print("Guest not registered.")
    
    def reg(self):
        if self.name not in Guest.registrations:
            if Guest.keys:
                self.key = Guest.keys.pop(0)  # Assign and remove the first available key
                Guest.registrations[self.name] = self.key
                # Print the key immediately after assigning it
                self.get_key()
            else:
                print("Sorry, no vacant rooms available")
        else:
            self.key = Guest.registrations[self.name]  # Fetch the existing key if already registered
            self.get_key()

# List of guests
guest_names = ["Josh", "Hans", "Evan", "Kyle", "Ted", "Karl", "Sam"]

# Process each guest
for guest_name in guest_names:
    guest = Guest(guest_name)
    
    # Print guest details
    print(f"\nGuest: {guest.name}")
    print(guest.is_regd())  # Check if registered
    
    # Print key or register and then print key
    if guest.is_regd() == 'Registered':
        guest.get_key()
    else:
        guest.reg()
