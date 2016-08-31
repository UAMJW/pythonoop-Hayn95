#Primer clase de Python
class Consola:
	
	def __init__(self, marca):
		self.marca=marca
		self.encendida=False
		
	def encenderC(self):
		if(self.encendida==False):
			self.encendida=True
		else:
			print "La consola ya estaba encendida"
		
	def apagarC(self):
		if(self.encendida==True):
			self.encendida=False
		else:
			print "La consola ya estaba apagada"
	
	def saberMarca(self):
		print self.marca
		
cons = Consola("Sony")
cons.encenderC()
cons.apagarC()
cons.apagarC()
cons.saberMarca()
raw_input()
