import pickle
from contextlib import contextmanager

@contextmanager
def openFile(path, mode):
	file = open(path, mode)
	yield file
	file.close()

class Podsjetnik():

    def __init__(self, *args):
    	if(len(args) != 3):
		pass
	else:
        	self.datum = args[0]
        	self.vrijeme = args[1]
        	self.poruka = args[2]

   
    def toString(self):

        return 'Datum: %s\nVrijeme: %s\nPoruka: %s'%(self.datum, self.vrijeme, self.poruka)
    
	
    def menu(self):

		while True:

			objekti = []

			print 'Meni:'
			print '1) Dodavanje nove stavke'
			print '2) Lista stavki po datumu'
			print '3) Lista svih stavki'
			print '4) Kraj'
			print '-'*24
			opcija = input('Odaberite opciju:')

			if opcija == 1:

				self.datum = raw_input('Unesite datum: ')
				self.vrijeme = raw_input('Unesite vrijeme: ')
				self.poruka = raw_input('Unesite poruku: ')
				print'\n'

				object = Podsjetnik(self.datum, self.vrijeme, self.poruka)

				with  openFile('podsjetnik.p', 'ab') as file:
					pickle.dump(object, file, pickle.HIGHEST_PROTOCOL)

			elif opcija == 2:

				datum = raw_input('Unesite datum koji pretrazujete: ')
				print'\n'

				with  openFile('podsjetnik.p', 'rb') as file:
					while 1:
						try:
							o = pickle.load(file)
						except EOFError:
							break
						objekti.append(o)

				print 'Ispis podsjetnika za datum ',datum,':'

				for object in objekti:
					if object.datum ==  datum:
						print object.toString()
						print '-'*24
					else:
						continue

			elif opcija == 3:

				print 'Ispis svih posjetnika:\n'
				with  openFile('podsjetnik.p', 'rb') as file:
					while True:
						try:
							o = pickle.load(file)
						except EOFError:
							break
						objekti.append(o)

				for object in objekti:
					print object.toString()
					print '-'*24

			elif opcija == 4:
				break


a = Podsjetnik()
a.menu()
