import speech_recognition as sr
import smtplib

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Clearing background noise")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("Waiting for your message")
    recordedAudio = recognizer.listen(source)
    print("Done recording")
    try:
        print("Printing the message")
        text = recognizer.recognize_google(recordedAudio,language='en-US')
        print(f"your message is :{text}")
    except Exception as e:
        print(e)

reciever = 'sidharthver@gmail.com'
message = text
sender = 'sidhantsreshtha2003@gmail.com'
subject = "Automated email testing"
password = 'nnrdnqusdmuwtvko'
server = smtplib.SMTP('smtp.gmail.com',587) 
server.starttls()
server.login(sender,password)
server.sendmail(sender,reciever,message)



# import speech_recognition as sr
# import smtplib

# recognizer = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Clearing Background Noise")
#     recognizer.adjust_for_ambient_noise(source,duration=1)
#     print("Waiting for your message")
#     recordedAudio =  recognizer.listen(source)
#     print("Done recording")
#     try:
#         print("Printing the message")
#         text = recognizer.recognize_google(recordedAudio,language =' en-US')
#         print(f"Your message is: {text}")
#     except Exception as e:
#         print(e)

# receiver = 'bt23cse346@shivalikcollege.edu.in'
# message = text
# sender = 'sidhantsreshtha2003@gmail.com'
# subject = "Automated emai testing"
# password = 'nnrdnqusdmuwtvko'
# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login(sender,password)
# server.sendmail(sender,receiver,message)