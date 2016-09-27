import serial, time, datetime, os

ser = serial.Serial('/dev/ttyACM0',9600)
status = 0
powerOutNotice = 0
currentTime = time.time()
triggerTime = currentTime + 60
while True:
        payload = ser.readline()
        try:
                payload = int(ser.readline())
                if payload == 0:
                        if powerOutNotice == 0:
                                print "Power outage detected"
                                powerOutNotice = 1
                        if time.time() > triggerTime:
                                emails = ["email@address.com"]
                                for account in emails:
                                        string = "echo 'Power loss detected at <LOCATION> %s' | mailx -s '<LOCATION>: POWER LOSS' %s" % (datetime.date$
                                        os.system(string)
                                        print "Notification sent to %s" % account
                                #Wait 5 minutes before sending another message
                                triggerTime = time.time() + 300
                else:
                        print payload
                        powerOutNotice = 0;
        except:
                print "Oh no... something's wrong"
