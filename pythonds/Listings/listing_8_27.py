def merge(self):
	for i in self.children:
		if i:
			if i.count > 0:
				self.oTree.leafList.remove(i)
				self.oTree.numLeaves -= 1
			else:
				print("Recursively Merging non-leaf...")
				i.merge()
			self.count += i.count
			self.red += i.red
			self.green += i.green
			self.blue += i.blue
	for i in range(8):
		self.children[i] = None	   
