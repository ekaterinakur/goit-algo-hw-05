class HashTable:
	def __init__(self, size):
		self.size = size
		self.table = [[] for _ in range(self.size)]
		
	def hash_function(self, key):
		return hash(key) % self.size
		
	def insert(self, key, value):
		key_hash = self.hash_function(key)
		key_value = [key, value]
		
		if self.table[key_hash] is None:
			self.table[key_hash] = list([key_value])
			return True
		else:
			for pair in self.table[key_hash]:
				if pair[0] == key:
					pair[1] = value
					return True
			self.table[key_hash].append(key_value)
			return True
			
	def get(self, key):
		key_hash = self.hash_function(key)
		if self.table[key_hash] is not None:
			for pair in self.table[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None

	def delete(self, key):
		key_hash = self.hash_function(key)
		if self.table[key_hash] is not None:
			for i, pair in enumerate(self.table[key_hash]):
				if pair[0] == key:
					del self.table[key_hash][i]
					return True
		return False

H = HashTable(5)
H.insert("Artem", 6)
H.insert("Misha", 3)
H.insert("Konstyantyn", 2.5)

print(H.get("Artem"))
print(H.get("Misha"))
print(H.get("Konstyantyn"))

H.delete("Konstyantyn")

print(H.get("Konstyantyn"))
