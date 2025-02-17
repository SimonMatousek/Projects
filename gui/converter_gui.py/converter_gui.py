import tkinter as tk
from tkinter import ttk


#class ConverterGUIApp:
window = tk.Tk()
window.title("Converter")
window.geometry("300x350")
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

def convert():
    print(f"output_str={output_str.get()}")
    print(f"entry_int={entry_int.get()}")
    output_str.set(f"{entry_int.get() * 1.61} km")
    print(f"output_str={output_str.get()}")

# Constant text
title_label = ttk.Label(master=window, text="Miles to kilometers", font="Calibri 14 bold")
title_label.pack(pady=10)

input_frame = ttk.Frame(master=window)
input_frame.pack(pady=10)

entry_int = tk.IntVar()
entry_field = ttk.Entry(master=input_frame, textvariable=entry_int)
entry_field.pack(side="left", padx=10)

convert_button = ttk.Button(master=input_frame, text="Convert", command=convert)
convert_button.pack(side="left")

output_str = tk.StringVar()
output_label = ttk.Label(master=window, text="first output", front="Calibri 10", textvariable=output_str)
output_label.pack(pady=10)

#def run():
#   self.window.mainloop()
window.mainloop()

if __name__ == "__main__":
    #app = ConverterGUIApp()
    #app.run() 
    convert()
    