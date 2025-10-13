# -------------------- UI and sync code begins below --------------------

import tkinter as tk

# make a window
root = tk.Tk()
root.title("Ultrasonic Control")

# label to show if speaker is on or off
status_label = tk.Label(root, text="Speaker is OFF")
status_label.pack()

# button to turn on
on_button = tk.Button(root, text="Turn ON", command=On)
on_button.pack()

# button to turn off
off_button = tk.Button(root, text="Turn OFF", command=Off)
off_button.pack()

# label for frequency
frequency_label = tk.Label(root, text=f"Frequency: {frequency} Hz")
frequency_label.pack()

# slider for frequency
freq_slider = tk.Scale(root, from_=100, to=5000, orient="horizontal",
                       command=Frequency_chan)
freq_slider.set(frequency)
freq_slider.pack()

# label for duty cycle
duty_label = tk.Label(root, text=f"Duty Cycle: {dutyCycle}%")
duty_label.pack()

# slider for duty cycle
duty_slider = tk.Scale(root, from_=0, to=100, orient="horizontal",
                       command=DutyCycleVal)
duty_slider.set(dutyCycle)
duty_slider.pack()

# exit button
exit_button = tk.Button(root, text="Exit",
                        command=lambda: (pwm.stop(), GPIO.cleanup(), root.destroy()))
exit_button.pack()

# keep window open
root.mainloop()
