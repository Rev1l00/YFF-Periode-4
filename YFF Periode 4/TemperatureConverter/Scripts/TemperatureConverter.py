import tkinter as tk

frame = tk.Tk()
frame.title("Temperature Converter")

canvas1 = tk.Canvas(frame, width=350, height=75)
canvas1.pack()

text1 = tk.Label(frame, text = "Enter a temperature in Fahrenheit: ")
canvas1.create_window(100, 25, window = text1)

entry1 = tk.Entry(frame) 
canvas1.create_window(255, 25, window = entry1)

def convert_temperature():
    temperature = entry1.get()

    pop_up_screen = tk.Tk()
    pop_up_screen.title("Result")

    canvas2 = tk.Canvas(pop_up_screen, width=300, height=60)
    canvas2.pack()

    label1 = tk.Label(pop_up_screen, text = f"{float(temperature)} Fahrenheit is equal to {((float(temperature) - 30) * 0.5556)} Celsius.")
    canvas2.create_window(150, 25, window = label1)

    pop_up_exit = tk.Button(pop_up_screen, text = "OK", command = quit)
    canvas2.create_window(280, 45, window = pop_up_exit)

convert = tk.Button(frame, text = "Convert", command = convert_temperature)
canvas1.create_window(150, 50, window = convert)

exit_button = tk.Button(frame, text = "Quit", command = quit)
canvas1.create_window(200, 50, window = exit_button)

frame.mainloop()
