import serial, time, datetime, os

ser = serial.Serial('/dev/ttyACM0',9600)
status = 0;
currentTime = time.time()
triggerTime = currentTime + 60

while True:
        payload = ser.readline()
        try:
                payload = int(ser.readline())
                if payload == 0:
                        print "Power is out"
                        if time.time() > triggerTime:
                                print "Sending email"
                                string = "MESSAGE HERE %s' | mailx -s 'SUBJECT HERE' email@address.com" % datet$
                                os.system(string)
                                #Sets the next email to be sent after 5 minutes.
                                triggerTime = time.time() + 300
                else:
                        print payload
        except:
                pass
