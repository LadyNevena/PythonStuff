class Razlomak():

    def __init__(self, brojilac, imenilac):
        self.brojilac = brojilac
        self.imenilac = imenilac

    def __str__(self):
        return  '%s/%s'%(self.brojilac,self.imenilac)

    def __mul__(self,other):
        return Razlomak(self.brojilac*other.brojilac, self.imenilac*other.imenilac)

    def __add__(self, other):
        noviBrojilac = self.imenilac * other.brojilac + self.brojilac * other.imenilac
        noviImenilac = self.imenilac * other.imenilac

        return Razlomak(noviBrojilac, noviImenilac)


