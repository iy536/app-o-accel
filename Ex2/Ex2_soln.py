Z = input("Enter the number of protons (charge):")
A = input("Enter the atomic mass (in u):")

class NeutronFinder:
    def __init__(self, Z, A):
        self.Z = Z
        self.A = A

    def calculateN(self):
        N = int(self.A) - int(self.Z)
        print("The number of neutrons is %d." % N)
        
Example = NeutronFinder(Z,A)
Example.calculateN()