alphas_price = 100
betas_price = 80
gammas_price = 50
deltas_price = 25
eps_price = 15
embryo_price = 10
oxigen_flask_price = 5

alphas_oxigen = 8
betas_oxigen = 5
gammas_oxigen = 3
deltas_oxigen = 2
eps_oxigen = 1

player_fords = 0
player_embryos = 10
player_oxigen_flasks = 6

class Embryo():
	sold = False
	def __init__(name, orden, intel, fuerza, lider, arm, lifetime, decant_time):
		self.orden = orden
		self.intel = intel
		self.fuerza = fuerza
		self.lider = lider
		self.arm = arm
		self.lifetime = lifetime
		self.decant_time = decant_time	
		self.name = name

	def update(self):
		if self.decant_time < 1:
			self.lifetime -= 1
			if not self.sold:
				self.sold = True
				return self.pays
			else:
				return None
		else:
			self.decant_time -= 1
			return None

	def __repr__(self):
		return "%s. Turnos restantes: %s Tiempo decantacion: %s" % (self.name, self.lifetime,
																	self.decant_time)


class Alpha(Embryo):
	def __init__(self):
		self.name = "Alfa"
		self.orden = 10
		self.intel = 50
		self.fuerza= 0
		self.lider = 30
		self.arm = -5
		self.lifetime = 10
		self.decant_time = 6
		self.pays = 100

class Beta(Embryo):
	def __init__(self):
		self.name = "Beta"
		self.orden = 20
		self.intel = 30
		self.fuerza= 0
		self.lider = 20
		self.arm = 0
		self.lifetime = 8
		self.decant_time = 4
		self.pays = 80

class Gamma(Embryo):
	def __init__(self):
		self.name = "Gamma"
		self.orden = 30
		self.intel = 10
		self.fuerza= 10
		self.lider = 10
		self.arm = 10
		self.lifetime = 6
		self.decant_time = 3
		self.pays = 50

class Delta(Embryo):
	def __init__(self):
		self.name = "Delta"
		self.orden = 0
		self.intel = 0
		self.fuerza= 30
		self.lider = 0
		self.arm = 30
		self.lifetime = 6
		self.decant_time = 3
		self.pays = 25

class Epsilon(Embryo):
	def __init__(self):
		self.name = "Epsilon"
		self.orden = 0
		self.intel = -5
		self.fuerza= 50
		self.lider = 0
		self.arm = 50
		self.lifetime = 4
		self.decant_time = 2
		self.pays = 15

turno = 0
subjects = []

armony_goal = 300
leader_goal = 100
strenght_goal = 400
int_goal = 150
order_goal = 100

player_armony = 0
player_leader = 0
player_strenght = 0
player_int = 0
player_order = 0

goals_completed = False

while not goals_completed:
	entrada = raw_input("Opcion:")

	if entrada == "alpha":

		subjects.append(Alpha())
		player_embryos -= 1
		player_oxigen_flasks -= 8

	elif entrada == "beta":

		subjects.append(Beta())
		player_embryos -= 1
		player_oxigen_flasks -= 5

	elif entrada == "gamma":

		subjects.append(Gamma())
		player_embryos -= 1
		player_oxigen_flasks -= 3

	elif entrada == "delta":

		subjects.append(Delta())
		player_embryos -= 1
		player_oxigen_flasks -= 2

	elif entrada == "eps":

		subjects.append(Epsilon())
		player_embryos -= 1
		player_oxigen_flasks -= 1

	elif entrada == "embriones":
		player_fords -= 100
		player_embryos += 10

	elif entrada == "oxigeno":
		player_fords -= 50
		player_oxigen_flasks += 10

	elif entrada == "turno":
		for subject in subjects:
			pay = subject.update()
			if pay:
				player_fords += pay
			if subject.lifetime < 1:
				subjects.remove(subject)

	player_armony = 0
	player_leader = 0
	player_strenght = 0
	player_int = 0
	player_order = 0
	
	for subject in subjects:
		if subject.decant_time < 1:
			player_armony += subject.arm
			player_leader += subject.lider
			player_strenght += subject.fuerza
			player_int += subject.intel
			player_order += subject.orden

	print "******METAS*****"
	print "ARMONIA: ", armony_goal
	print "LIDERAZGO: ", leader_goal
	print "FUERZA: ", strenght_goal
	print "INTELIGENCIA: ", int_goal
	print "ORDEN: ", order_goal
	print "******RECURSOS*****"
	print "FORDS: ", player_fords
	print "EMBRIONES: ", player_embryos
	print "FRASCOS DE OXIGENO", player_oxigen_flasks
	print "******PUNTUACIONES*****"
	print "ARMONIA: ", player_armony
	print "LIDERAZGO: ", player_leader
	print "FUERZA: ", player_strenght
	print "INTELIGENCIA: ", player_int
	print "ORDEN: ", player_order
	print "*****SOCIEDAD*****"
	for subject in subjects:
		print subject
	print "***********************"
	print "======================="
	print "***********************"

	if entrada == "s":

		goals_completed = True



