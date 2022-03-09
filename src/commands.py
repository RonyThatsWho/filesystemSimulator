#import utils

class Folder:
	def __init__ (self, name, path, container = None):
		self.name = name
		self.path = path + name + "/"
		self.container = container
		self.contents = []
		self.folders = []
		self.files = []
		# print ('Folder named ' + name + ' created')

	def __str__(self):
		return self.name + "/"

	def __lt__ (self, other):
		return self.name < other.name

class File:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "." + self.name

	def __lt__ (self, other):
		return self.name < other.name


def ls(folder):
	for f in folder.folders:
		print (f)
	for f in folder.files:
		print (f)

def mkdir (name, folder):
	for archive in folder.contents:
		if archive == name:
			print (name + ": File exists")
			return

	folder.contents.append(name)
	folder.folders.append(Folder(name, folder.path, folder))
	folder.folders.sort()


def touch (name, folder):
	# print ("touch: ")
	for archive in folder.contents:
		if archive == name:
			print (name + ": File exists")
			return

	folder.contents.append(name)
	folder.files.append(File(name))
	folder.files.sort()

def cd (root, source, path):
	if path == "/":
		return root

	current = source
	if path[0] == '/':
		current = root
		path = path[1:]

	splitPath = path.split('/')

	for i in range(len(splitPath)):
		found = False

		if splitPath[i] == ".." and current.container != None:
			current = current.container
			found = True
		elif splitPath[i] == ".." and current.container == None:
			current = root
			found = True

		else:
			for x in current.folders:
				if splitPath[i] == x.name and isinstance(x, Folder):
					current = x
					found = True
					break
 
		if found == False:
			print ("No such file or directory")
			return source 

	return current


def clear(root):
	root.contents.clear()
	root.files.clear()
	root.folders.clear()
	return root
