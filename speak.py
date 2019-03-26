def text_talk(text):
    import os
    import time
    try:
        f=open('text_talk.vbs','r')
        f.close()
    except:
        pass
    AAA=text.split()

    f=open('text_talk.vbs','w')
    f.write('Set Speak = CreateObject("sapi.spvoice")\n')
    f.write('Speak.Speak "'+str(text)+'"')
    f.close()

    os.system('start text_talk.vbs')

    #print('Set Speak "'+str(text)+'"')
    #time.sleep(len(AAA)/3.5)
    time.sleep(3)
    os.remove("text_talk.vbs")
import time
while True:

    text_talk(input("input-"))
