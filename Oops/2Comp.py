#  self is used to refer to the current instance of the class

class Computer:

    # constructor method to initialize object properties
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"CPU: {self.cpu}, RAM: {self.ram}")

    def compare(self, other):
        if self.ram == other.ram and self.cpu == other.cpu:
            return True
        else:
            return False


comp1 = Computer("i5", "16GB")
comp2 = Computer("Ryzen 5", "32GB")

print(comp1.cpu)

comp1.cpu = "i7"  # modifying the cpu property of comp1 object

comp1.config()
comp2.config()

print("Are both computers the same?", comp1.compare(comp2))
