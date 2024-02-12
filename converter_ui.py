"""Converter_Ui Module for Converter_app"""

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import unittype
from converter import UnitConverter


class ConverterUI(tk.Tk):
    """User Interface for a unit converter.

    The UI displays units and handles user interaction.  It invokes
    a UnitConverter object to perform actual unit conversions.
    """
    def __init__(self, unit_convert: UnitConverter, unit_type):
        """initialize for ConverterUI"""
        super().__init__()
        self.title("Converter")
        self.converter = unit_convert
        self.unit_type = unit_type
        self.unit_name1 = tk.StringVar()
        self.user_int_left = tk.IntVar()
        self.unit_name2 = tk.StringVar()
        self.user_int_right = tk.IntVar()
        self.combobox1 = ttk.Combobox(self, width=10, textvariable=self.unit_name1)
        self.combobox2 = ttk.Combobox(self, width=10, textvariable=self.unit_name2)
        self.input1 = tk.Entry(self, width=20, textvariable=self.user_int_left)
        self.output1 = tk.Entry(self, width=20, textvariable=self.user_int_right)
        self.input1.delete(0, tk.END)
        self.output1.delete(0, tk.END)
        self.unit_calculate_type = unittype.LengthUnit
        self.program = tk.Text(self, height=0.5, width=15)
        self.program.insert("8.8", "Default")
        self.program.config(state="disabled")
        self.converter_button = tk.Button(self, text="convert", command=self.convert_handler)
        self.clear_button = tk.Button(self, text="clear", command=self.clear)
        self.init_components()
        self.load(self.unit_calculate_type)
        self.pylint_fix = None

    def set_unit_calculator(self, unit_type: str):
        """sets the new calculator"""
        self.unit_calculate_type = unittype.unit_type_return(unit_type)
        self.load(self.unit_calculate_type)
        self.program.config(state="normal")
        self.program.delete("1.0", "end")
        self.program.insert("1.0", unit_type)
        self.program.config(state="disabled")

    def init_components(self):
        """Create components and layout the UI."""
        label = tk.Label(self, text="=", font=("Arial", 12))
        label.grid(row=1, column=2, padx=10, pady=5)
        self.program.grid(row=0, column=0, columnspan=7, pady=10, padx=5)
        self.input1.grid(row=1, column=0, padx=10, pady=5)
        self.combobox1.grid(row=1, column=1, padx=5, pady=5)
        self.output1.grid(row=1, column=3, padx=5, pady=5)
        self.combobox2.grid(row=1, column=4, padx=5, pady=5)
        self.converter_button.grid(row=1, column=5, padx=5, pady=5)
        self.clear_button.grid(row=1, column=6, padx=5, pady=5)
        menu = tk.Menu(self)
        self.config(menu=menu)
        unit_selector = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Unit selector", menu=unit_selector)
        temp_list = []
        for unit_str in unittype.UnitType:
            unit_str_temp_a, unit_str_temp_b = unit_str.value
            self.pylint_fix = unit_str_temp_b
            temp_list.append(unit_str_temp_a)
        for j in temp_list:
            unit_selector.add_command(label=j, command=lambda x=j: self.set_unit_calculator(x))
        self.input1.bind('<Return>', lambda event=None: self.convert_handler())
        self.output1.bind('<Return>', lambda event=None: self.convert_handler())
        self.configure(bg="#f0f0f0")
        self.input1.config(bg="white", fg="black", font=("Arial", 10))
        self.output1.config(bg="white", fg="black", font=("Arial", 10))
        self.combobox1.config(font=("Arial", 10))
        self.combobox2.config(font=("Arial", 10))
        self.converter_button.config(font=("Arial", 10))
        self.clear_button.config(font=("Arial", 10))
        label.config(bg="#f0f0f0", fg="black", font=("Arial", 12))
        self.program.config(bg="white", fg="black", font=("Arial", 10), state="disabled")

    def clear(self):
        """clears user input"""
        self.input1.delete(0, tk.END)
        self.output1.delete(0, tk.END)
        self.input1.configure(fg="black")
        self.output1.configure(fg="black")

    def load(self, unit_type):
        """loads units"""
        units = self.converter.return_unit(unit_type)
        self.combobox1['value'] = units
        self.combobox2['value'] = units
        self.combobox1.current(newindex=0)
        self.combobox2.current(newindex=0)

    def convert_handler(self):
        """An event handler for conversion actions.
        You should call the unit converter to perform actual conversion.
        """
        self.input1.configure(fg="black")
        self.output1.configure(fg="black")
        temp_val1 = self.input1.get()
        temp_val2 = self.output1.get()
        if not temp_val1 and not temp_val2:
            tkinter.messagebox.showerror(title="Error Popup", message="Please enter a value.")
            return
        try:
            get_first_unit = self.combobox1.get()
            get_second_unit = self.combobox2.get()
            first_unit = unittype.unit_type_return(get_first_unit)
            second_unit = unittype.unit_type_return(get_second_unit)
            first_value = float(temp_val1) if temp_val1 else 0
            second_value = float(temp_val2) if temp_val2 else 0
            if first_value != 0 and second_value == 0:
                self.converter.input1_set(first_unit)
                self.converter.input2_set(second_unit)
                converted_value = self.converter.calculate_unit(first_value, self.unit_calculate_type)
                self.output1.delete(0, tk.END)
                self.output1.insert(0, str(converted_value))
            elif first_value != 0 and second_value != 0:
                self.converter.input1_set(first_unit)
                self.converter.input2_set(second_unit)
                converted_value = self.converter.calculate_unit(first_value, self.unit_calculate_type)
                self.output1.delete(0, tk.END)
                self.output1.insert(0, str(converted_value))
            elif second_value != 0 and first_value == 0:
                self.converter.input1_set(first_unit)
                self.converter.input2_set(second_unit)
                converted_value = self.converter.calculate_unit(second_value, self.unit_calculate_type)
                self.input1.delete(0, tk.END)
                self.input1.insert(0, str(converted_value))
        except ValueError or TypeError:
            if temp_val1:
                self.input1.configure(fg="red")
            if temp_val2:
                self.output1.configure(fg="red")
            tk.messagebox.showerror(title="Error Popup", message="Invalid input value.")
            return

    def run(self):
        """runs the program"""
        self.mainloop()
