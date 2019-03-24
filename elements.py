class Atom:
    """ Base class from which al elements must inherit """
    def __init__(self, symbol, protons, mass):
        self.symbol = symbol
        self.protons = protons
        self.mass = mass


class Molecule:
    """ Base class from which all Molecules must inherit """
    def __init__(self, composition = [(None, 0)]):
        self.composition = composition

    def generate_symbol(self):
        """ return chemical symbol based on substance composition 
            TODO: sort using Hill system / prevent printing 1 for single elements """

        return "".join(["".join("{}{}".format(element.symbol, number)
                                ) for element, number in self.composition])

class IsotopeMixin():

    is_isotope = True

    def __init__(self, extra_neutrons=0):
        super().__init__()
        self._neutrons = (self.mass - self.protons) + extra_neutrons  

    @property
    def neutrons(self):
        return self._neutrons

    @neutrons.setter
    def neutrons(self, value):
        self._neutrons = value


class Hidrogen(Atom):
    """ Hidrogen element """
    def __init__(self):
        super().__init__("H", 1, 1)


class Deuterium(IsotopeMixin, Hidrogen):
    """ Deuterium element """
    def __init__(self):
        super().__init__(1)
  
class Oxygen(Atom):
    """ Oxygen element """
    def __init__(self):
        super().__init__("O", 1, 16)

class Water(Molecule):
    """ Water Molecule """
    def __init__(self):
        self.composition = [(Hidrogen(), 2),
                            (Oxygen(), 1)]  


#   Example run
#   o = Oxygen()
#   w = Water()
#   d = Deuterium()

#   >>> print(o.mass)
#   16
#   >>> print(w.generate_symbol())
#   H2O1
#   >>> print(d.neutrons)
#   1
