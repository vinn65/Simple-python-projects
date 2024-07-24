class Coder():
    def __init__(self):
        self.name = input("Name >")
        self.language = input("Language >")
    def show_details(self):
        print(str(self.name))
        print(str(self.language))

class pythoner():
    def __init__(self):
        self.co_profile = Coder()
    def profile(self):
        self.co_profile.show_details()

jake = pythoner()
jake.profile()
        