class car:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    def start(self):
        self.is_running = True
        print (f"The {self.make} {self.model} engine started")

    def stop(self):
        self.is_running = False
        print (f"The {self.make} {self.model} engine stopped")
    def displayInfo(self):
        print(f"{self.make} {self.model} ({self.year}), running = {self.is_running}")

car1 = car("maruti", "swift", 2014)
car1.displayInfo()
