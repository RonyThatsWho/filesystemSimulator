#Rony Vargas
#CheckPoint Assessment
#March 2022

"""
Assessment for Checkpoint Customer Support

"""

import src
root = None

def parse(commands, folder):

     #print(root)
	com = commands[0]
	if com == "ls":
		src.ls(folder)
		return folder

	elif com == "touch" and len(commands) == 2:
		src.touch (commands[1], folder)
		return folder

	elif com == "mkdir" and len(commands) == 2:
		src.mkdir(commands[1], folder)
		return folder

	elif com == "cd" and len(commands) == 2:
		return src.cd(root, folder, commands[1])

	elif com == "clear" and len(commands) == 1:
		return src.clear(root)

	elif com == "quit" and len(commands) == 1:
		return None

	else:
		print("invalid command")
		return folder
                

def main():
    global root
    root = src.Folder("root", "/")
    directory = root
    run = True

    while (run):
        print("\n" + "RONY-FS: " + directory.path, end="\n$ ")
        command = input()
        commands = command.split()
        directory = parse(commands, directory)

        if directory == None:
            run = False
            
	

if __name__ == "__main__":
	main()
