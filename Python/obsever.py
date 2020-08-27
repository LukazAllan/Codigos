class Sub:
	"""docstring for Sub"""
	def __init__(self, name):
		self.name = name

	def update(self, msg):
		print(f'{self.name} recebeu msg {msg}')

class Pub:
	"""docstring for Pub"""
	def __init__(self):
		self.subs = set()

	def reg(self, who):
		self.subs.add(who)

	def can(self, who):
		self.subs.discard(who)

	def note(self, msg):
		print(f'Notifying {len(self.subs)} observers')
		for sub in self.subs:
			sub.update(msg)

obj = Pub()

allan = Sub('allan')
daniel = Sub('daniel')

obj.reg(allan)
obj.reg(daniel)

obj.note("Eh sexta-feira, rapaziada")
obj.can(daniel)
obj.note('Só eu nesta poha!')