from tkinter import Tk, Button, Entry, StringVar
def button_click(char):
 display.set(display.get() + char)
def button_clear():
 display.set("")
def button_equal():
try:
 result = str(eval(display.get()))
 display.set(result)
except:
display.set("Error")
# Create the main window and display
root = Tk()
root.title("Simple Calculator")
display = StringVar()
# Increase text box size using font parameter
text_box_font = ("Arial", 20) # Set font size
display_entry = Entry(root, width=23, textvariable=display, font=text_box_font)
display_entry.grid(columnspan=4, pady=8)
# Define button functions with lambda for brevity
buttons = {
"7": lambda: button_click("7"),
"8": lambda: button_click("8"),
"9": lambda: button_click("9"),
"/": lambda: button_click("/"),
"4": lambda: button_click("4"),
"5": lambda: button_click("5"),
"6": lambda: button_click("6"),
"*": lambda: button_click("*"),
"1": lambda: button_click("1"),
"2": lambda: button_click("2"),
"3": lambda: button_click("3"),
"-": lambda: button_click("-"),
"0": lambda: button_click("0"),
".": lambda: button_click("."),
"C": button_clear,
"+": lambda: button_click("+"),
"=": button_equal
}
# Increase text box size using font parameter
text_box_width = 35 # Adjust as desired
text_box_font = ("Arial", text_box_width) # Set font size
# Increase button size using font parameter
button_font = ("Arial", 25) # Set font size
# Create buttons using a loop and dictionary
button_row = 1
button_col = 0
for button_text, button_func in buttons.items():
button = Button(root, text=button_text, command=button_func, font=button_font, width=4)
button.grid(row=button_row, column=button_col)
button_col += 1
if button_col > 3:
button_col = 0
button_row += 1
# Start the main event loop
root.mainloop()
