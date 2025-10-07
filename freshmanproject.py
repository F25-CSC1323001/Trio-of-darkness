import tkinter as tk
from tkinter import ttk
import RPi.GPIO as GPIO


#GPIO set up
speakerPin = #figure out which pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(speakerPin, GPIO.OUT)

frequency = # Figure out frequency when device is here
dutyCycle = # This value is a percentage of how often it'll run. Figure out by testing

pwm = GPIO.PWM(speakerPin, frequency)
PWM_act = False

def On():
    global pwm_act
    if not pwm_act:
        pwm.start(dutyCycle)
        pwm_act = True
        status_label.config(text='Speaker is Activated')

def Off():
    global pwm_act
    if pwm_act:
        pwn.stop()
        pwm_act = False
        status_label.config(text='Speaker is Deactivated')

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
    


    
