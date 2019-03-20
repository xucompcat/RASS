# RASS v. 1.0
# Author: W. C. McKee

import math, random

class Atom:

    def __init__(self, symbol, valency=99):
        self.symbol = symbol
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.CovR1 = 0.0
        self.CovR3 = 0.0
        self.valency = valency

    def getSymbol(self):
        return self.symbol

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getCovR1(self):
        return self.CovR1

    def getCovR3(self):
        return self.CovR3

    def getValency(self):
        return self.valency

    def setCovR1(self):
        covr1_dictionary = {"H":0.32, "He":0.46, "Li":1.33, "Be":1.02, "B":0.85, "C":0.75, "N":0.71,
        "O":0.63, "F":0.64, "Ne":0.96, "Na":1.60, "Mg":1.39, "Al":1.26, "Si":1.16, "P":1.11, "S":1.03,
        "Cl":0.99, "Ar":1.07, "K":1.96, "Ca":1.71, "Sc":1.48, "Ti":1.36, "V":1.34, "Cr":1.22, "Mn":1.19,
        "Fe":1.16, "Co":1.11, "Ni":1.10, "Cu":1.20, "Zn":1.20, "Ga":1.24, "Ge":1.21, "As":1.21,
        "Se":1.16, "Br":1.14, "Kr":1.21, "Rb":2.1, "Sr":1.85, "Y":1.63, "Zr":1.54, "Nb":1.47,
        "Mo":1.38, "Tc":1.28, "Ru":1.25, "Rh":1.25, "Pd":1.20, "Ag":1.39, "Cd":1.44, "In":1.46,
        "Sn":1.40, "Sb":1.40, "Te":1.36, "I":1.33, "Xe":1.35, "Cs":2.32, "Ba":1.96, "Hf":1.52,
        "Ta":1.46, "W":1.37, "Re":1.31, "Os":1.29, "Ir":1.22, "Pt":1.23, "Au":1.24, "Hg":1.42,
        "Tl":1.50, "Pb":1.44, "Bi":1.51, "Po":1.45, "At":1.47, "Rn":1.45, "Fr":2.23, "Ra":2.01,
        "Rf":1.57, "Db":1.49, "Sg":1.43, "Bh":1.41, "Hs":1.34, "Mt":1.29, "Ds":1.28, "Rg":1.21,
        "La":1.8, "Ce":1.63, "Pr":1.76, "Nd":1.74, "Pm":1.73, "Sm":1.72, "Eu":1.68, "Gd":1.69,
        "Tb":1.68, "Dy":1.67, "Ho":1.66, "Er":1.65, "Tm":1.64, "Yb":1.7, "Lu":1.62, "Ac":1.86,
        "Th":1.75, "Pa":1.69, "U":1.7, "Np":1.71, "Pu":1.72, "Am":1.66, "Cm":1.66, "Bk":1.68,
        "Cf":1.68, "Es":1.65, "Fm":1.67, "Md":1.73, "No":1.76, "Lr":1.61}

        if covr1_dictionary.has_key(self.symbol):
            self.CovR1 = covr1_dictionary[self.symbol]
        else:
            print "No single bond covalent radius found for atom " + self.symbol + ". Terminating Kick-R."
            exit()

    def setCovR3(self):
        covr3_dictionary = {"H":0.32, "He":0.46, "Li":1.24, "Be":0.85, "B":0.73, "C":0.60, "N":0.54,
        "O":0.53, "F":0.53, "Ne":0.67, "Na":1.55, "Mg":1.27, "Al":1.11, "Si":1.02, "P":0.94, "S":0.95,
        "Cl":0.93, "Ar":0.96, "K":1.93, "Ca":1.33, "Sc":1.14, "Ti":1.08, "V":1.06, "Cr":1.03, "Mn":1.03,
        "Fe":1.02, "Co":0.96, "Ni":1.01, "Cu":1.12, "Zn":1.18, "Ga":1.17, "Ge":1.11, "As":1.06,
        "Se":1.07, "Br":1.09, "Kr":1.08, "Rb":2.02, "Sr":1.39, "Y":1.24, "Zr":1.21, "Nb":1.16,
        "Mo":1.13, "Tc":1.1, "Ru":1.03, "Rh":1.06, "Pd":1.12, "Ag":1.28, "Cd":1.36, "In":1.36,
        "Sn":1.3, "Sb":1.27, "Te":1.21, "I":1.25, "Xe":1.22, "Cs":2.09, "Ba":1.49, "Hf":1.22,
        "Ta":1.19, "W":1.15, "Re":1.1, "Os":1.09, "Ir":1.07, "Pt":1.1, "Au":1.21, "Hg":1.33,
        "Tl":1.42, "Pb":1.35, "Bi":1.35, "Po":1.29, "At":1.38, "Rn":1.33, "Fr":2.18, "Ra":1.59,
        "Rf":1.31, "Db":1.26, "Sg":1.21, "Bh":1.19, "Hs":1.18, "Mt":1.13, "Ds":1.12, "Rg":1.18,
        "La":1.39, "Ce":1.31, "Pr":1.28, "Nd":1.37, "Pm":1.35, "Sm":1.34, "Eu":1.34, "Gd":1.32,
        "Tb":1.35, "Dy":1.33, "Ho":1.33, "Er":1.33, "Tm":1.31, "Yb":1.29, "Lu":1.31, "Ac":1.40,
        "Th":1.36, "Pa":1.29, "U":1.18, "Np":1.16, "Pu":1.35, "Am":1.35, "Cm":1.36, "Bk":1.39,
        "Cf":1.4, "Es":1.4, "Fm":1.67, "Md":1.39, "No":1.76, "Lr":1.41}

        if covr3_dictionary.has_key(self.symbol):
            self.CovR3 = covr3_dictionary[self.symbol]
        else:
            print "No triple bond covalent radius found for atom " + self.symbol + ". Terminating Kick-R."
            exit()

    def setX(self, value):
        self.x = float(value)

    def setY(self, value):
        self.y = float(value)

    def setZ(self, value):
        self.z = float(value)

    def setValency(self, value):
        self.valency = value

def CovRad1Sum(molecule):
    sum = 0.0
    for atoms in molecule:
        sum = sum + atoms.getCovR1()
    return sum

def InteratomicDistance(atom1, atom2):
    distance = math.sqrt((atom1.getX()-atom2.getX())**2+(atom1.getY()-atom2.getY())**2+(atom1.getZ()-atom2.getZ())**2)
    return distance

def CovR3Sum(atom1, atom2):
    sum = atom1.getCovR3() + atom2.getCovR3()
    return sum

def CovR1Sum(atom1, atom2):
    sum = atom1.getCovR1() + atom2.getCovR1()
    return sum

def DistanceTest(structure_list):
    passed, i = True, 0

    while i <= len(structure_list) - 2:
        if InteratomicDistance(structure_list[i], structure_list[-1]) < 0.9*CovR3Sum(structure_list[i], structure_list[-1]):
            passed = False
            break
        i = i + 1

    return passed

def ReadInput(input):
    for i in input:
        if "atoms:" in str(i):
            atoms = input[input.index(i)].split()
            del atoms[0]

        if "atom_numbers:" in str(i):
            atom_numbers = input[input.index(i)].split()
            del atom_numbers[0]

        if "atom_valencies:" in str(i):
            atoms_valencies = input[input.index(i)].split()
            del atoms_valencies[0]

        if "structures:" in str(i):
            numb_of_structures = int(input[input.index(i)].split()[1])


    return atoms, atom_numbers, numb_of_structures

def InitializeAtoms(atoms, atom_numbers):
    atom_list = []
    for i in range(len(atoms)):
        j = 1
        while j <= int(atom_numbers[i]):
            atom_list.append(Atom(atoms[i]))
            j = j + 1

    for i in atom_list:
        i.setCovR1()
        i.setCovR3()

    return atom_list

def RandomUnitVector():
    x = random.triangular(-1.0, 1.0)
    y = random.triangular(-1.0, 1.0)
    z = random.triangular(-1.0, 1.0)

    magnitude = math.sqrt(x**2 + y**2 + z**2)

    x = x/magnitude
    y = y/magnitude
    z = z/magnitude

    random_unit_vector = [x, y, z]
    return random_unit_vector

def SetBond(atom1, atom2):
    bond = RandomUnitVector()
    scale = random.triangular(0.9*CovR3Sum(atom1, atom2),1.1*CovR1Sum(atom1,atom2))
    for i in range(len(bond)):
        bond[i] = bond[i]*scale
    return bond

def SetCoordinates(structure_list, atom_list):
    if len(structure_list) == 0:
        random_int = random.randint(0, len(atom_list) - 1)
        structure_list.append(atom_list[random_int])
        del atom_list[random_int]

    if len(structure_list) == 1:
        random_int = random.randint(0, len(atom_list) - 1)
        structure_list.append(atom_list[random_int])
        del atom_list[random_int]

        bond = SetBond(structure_list[0], structure_list[1])
        structure_list[1].setX(bond[0])
        structure_list[1].setY(bond[1])
        structure_list[1].setZ(bond[2])

    if len(structure_list) > 1:
        random_int1 = random.randint(0, len(atom_list) - 1)
        structure_list.append(atom_list[random_int1])
        del atom_list[random_int1]


        while DistanceTest(structure_list) is not True:

            random_int2 = random.randint(0, len(structure_list) - 2)
            bond = SetBond(structure_list[random_int2], structure_list[-1])
            structure_list[-1].setX(bond[0] + structure_list[random_int2].getX())
            structure_list[-1].setY(bond[1] + structure_list[random_int2].getY())
            structure_list[-1].setZ(bond[2] + structure_list[random_int2].getZ())


    return structure_list



def main():

    read_in = open('RASS.in', 'r')
    input = read_in.readlines()
    atoms, atom_numbers, numb_of_structures = ReadInput(input)
    structures_written = 0

    while structures_written < numb_of_structures:
        structure_list = []
        atom_list = InitializeAtoms(atoms, atom_numbers)
        while len(atom_list) != 0:
            structure_list= SetCoordinates(structure_list, atom_list)

	output = open(str(structures_written + 1) + '.RASS', 'w')
        output.write("%mem=4gb\n")
        output.write("# RB3LYP/LANL2DZ Opt=maxcycles=50\n")
        output.write("\nTitle\n\n")
        output.write("0 1\n")
        for i in structure_list:
            output.write(str(i.getSymbol()) + " " + str(i.getX()) + " " + str(i.getY()) + " " + str(i.getZ()) + "\n") 
        output.write("\nEND")
        output.close()

        structures_written = structures_written + 1


main()
