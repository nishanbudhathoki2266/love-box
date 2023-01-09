import I2C_LCD_driver
import time
import requests
import textwrap
import RPi.GPIO as GPIO

#Initializing LCD
mylcd = I2C_LCD_driver.lcd()

#Sensor Pins
irSensor = 16
servoPin = 11

#Settin up GPIO modes
GPIO.setmode(GPIO.BOARD)
GPIO.setup(irSensor, GPIO.IN)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.setwarnings(False)
#Servo Configs
servo = GPIO.PWM(servoPin, 50)
servo.start(0)


#State managing variables
messageKey = 1
lidOpened = False
newMessage = False
rotateLove = False
maxMessageKey = 1

while True:
        
        #get request to the API
        r = requests.get("http://lovebox.pythonanywhere.com/")
        response = r.json()

        #Checking the latest message in the API with highest key number
        for key in response.keys():
                if (int(key)) > messageKey:
                        maxMessageKey = int(key)


        #Checking if new message exists i.e. maxMessageKey should be higher than the messageKey
        if maxMessageKey > messageKey:
                newMessage = True
                messageKey = maxMessageKey

    
        if newMessage:
                        message = response[str(messageKey)]['message']
                        messageLength = len(message)
                        
                        while not GPIO.input(irSensor):
                                servo.ChangeDutyCycle(5)
                                time.sleep(0.5)
                                servo.ChangeDutyCycle(12.5)
                                time.sleep(0.5)
                        if GPIO.input(irSensor):
                            servo.ChangeDutyCycle(2.5)
                        while GPIO.input(irSensor):
                                if (messageLength > 40):
                                        messageChunks = textwrap.wrap(message, 40)
                                        while GPIO.input(irSensor):

                                                for message in messageChunks:
                                                        mylcd.lcd_display_string(message, 1)
                                                        print(message)
                                                        time.sleep(2)
                                                        mylcd.lcd_clear()

                                if (messageLength <= 40):

                                        mylcd.lcd_display_string(message, 1)
                                        time.sleep(2)
                                        mylcd.lcd_clear()
                                        print(message)

                                
                        newMessage = False
                        mylcd.lcd_clear()
        time.sleep(2)
