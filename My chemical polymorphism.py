# Chemical polymorphism! In this program you'll have fun using chemistry and polymorphism. Add elements and create molecules.

class Atom:
  def __init__(self, label):
    self.label = label
  def __add__(self, other):
    # Return as a chemical composition
    return self.label + other.label
  def __repr__(self):
    return self.label

class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
  def __repr__(self):
    # Return as a list of molecules
    return self.atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")

# Salt chemical composition using label AND using Polymorphism
salt_pol = sodium + chlorine
print(salt_pol)

# Salt Molecule as a list
salt = Molecule([sodium, chlorine])
print(salt.atoms)