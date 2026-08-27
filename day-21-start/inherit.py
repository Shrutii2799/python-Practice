class Animal:
    def __init__(self):
        self.eyes=2

    def breathe(self):
        print("inhale,exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()# sirf niche wali line and ye line nahi toh override hojata
        print("doing this under water")

    def swim(self):
        print("move in the water")


nemo=Fish()
nemo.breathe()
