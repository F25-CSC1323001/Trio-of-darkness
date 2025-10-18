import tkinter as tk
from tkinter import ttk
import RPi.GPIO as GPIO
from gpiozero import LED


                                                                #Ultrasonic Speaker code begins below

#GPIO set up
speakerPin = 18 #figure out which pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(speakerPin, GPIO.OUT)

frequency = 40000 # Figure out frequency when device is here
dutyCycle =  50 # This value is a percentage of how often it'll run. Figure out by testing

pwm = GPIO.PWM(speakerPin, frequency)
PWM_act = False

def system_on():
    global pwm_act
    if not pwm_act:
        pwm.start(dutyCycle)
        GPIO.output(LED_PIN, GPIO.HIGH)
        pwm_act = True
        status_label.config(text='System: ON (Speaker + Light)')

def system_off():
    global pwm_act
    if pwm_act:
        pwn.stop()
        GPIO.output(LED_PIN, GPIO.LOW)
        pwm_act = False
        status_label.config(text='System: OFF')

def Frequency_chan(): # function to be able to lower or increase the frequency without hard coding
    global frequency
    frequency = int(value)
    if pwm_act:
        pwm.frequencyChange(frequency)
    frequency_label.config(text=f"Frequency: {frequency} Hz") # shows the changed frequency
    
def DutyCycleVal(value): # function to be able to lower or increase the run time without hard coding
    global dutyCycle
    dutyCycle = int(value)
    if pwm_act:
        pwm.DutyChange(dutyCycle)
    duty_label.config(text=f"Duty Cycle: {dutyCycle}%") # showing what the new cycle is after changing it


                                                                    # Ultrasonic light code begins below

      
      
GPIO.setmode(GPIO.BCM)
LED_PIN = 23   # whatever pin we choose
GPIO.setup(LED_PIN, GPIO.OUT)

# light control for the gui
light_label = ttk.Label(root, text='Ultrasonic Light Control', font=('Arial', 14))
light_label.pack(pady=10)

light_on_button = ttk.Button(root, text='Turn ON Light', command=light_on)
light_on_button.pack(pady=2)

light_off_button = ttk.Button(root, text='Turn OFF Light', command=light_off)
light_off_button.pack(pady=2)

light_status_label = ttk.Label(root, text='Light is OFF')
light_status_label.pack(pady=2)



                                                                    # UI and sync code begins below

# create the window
root = tk.Tk()
root.title("Ultrasonic Control")
root.geometry("300x200")

# make buttons big and easy to tap
on_button = tk.Button(root, text="ON", command=On,
                      font=("Arial", 18), width=10, height=2, bg="lightgreen")
on_button.pack(pady=10)

off_button = tk.Button(root, text="OFF", command=Off,
                       font=("Arial", 18), width=10, height=2, bg="tomato")
off_button.pack(pady=10)

# keep the window open
root.mainloop()
=======
GPIO.setmode(GPIO.BCM)
LED_PIN =   # whatever pin we choose
GPIO.setup(LED_PIN, GPIO.OUT)

# light control for the gui
light_label = ttk.Label(root, text='Ultrasonic Light Control', font=('Arial', 14))
light_label.pack(pady=10)

light_on_button = ttk.Button(root, text='Turn ON Light', command=light_on)
light_on_button.pack(pady=2)

light_off_button = ttk.Button(root, text='Turn OFF Light', command=light_off)
light_off_button.pack(pady=2)

light_status_label = ttk.Label(root, text='Light is OFF')
light_status_label.pack(pady=2)


