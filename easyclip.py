fimport pyperclip
import time
import threading
import os
from tkinter import *
from tkinter import messagebox

# Clipboard Array
copy_array = []
# position of copy_array
counter = 0

# copy_array GUI location for increment and decrement
array_current_position = 0

thread_kill = True

# root for Tkinter
root = Tk(className="CopyMan")
# Text box to print copy_array value
T = Text(root, height=7, width=32, borderwidth=0)

# Text box to print position of clip
N = Text(root, height=1, width=2, borderwidth=0)

# Value of copy_array at a certain point
Fact = ""


def gui():
    """
    function for GUI.
    Handles grid and positioning.
    """

    global array_current_position
    global T
    global N
    global root
    global Fact

    root.wait_visibility(root)
    # root.wm_attributes('-alpha', 0.9)
    # root.configure(bg='#293134')

    img = PhotoImage(file='/home/devarshi/copyman/copyman.png')
    root.tk.call('wm', 'iconphoto', root._w, img)

    # T.config(font=("Courier", 10))
    T.grid(row=0, columnspan=30, sticky='nesw')
    # T.configure(bg='#293134', fg="#e0e2e4", bd=-2)
    N.grid(row=1, columnspan=2)
    # N.configure(bg='#293134', fg="#e0e2e4")
    l = Label(root, text="w=Next s=Previous c=Copy q=minimize")

    # Create label
    l.config(font=("Courier", 10))
    l.grid(row=2, columnspan=2)

    Fact = copy_array[array_current_position]

    # Create button for next text. 
    b1 = Button(root, text="Previous", command=increment, borderwidth=0)
    b1.grid(row=3, column=0, sticky='nesw')

    # Create an Exit button.
    # b2 = Button(root, text="Exit", command=on_closing)
    b2 = Button(root, text="Exit", command=exit1, borderwidth=0)
    b2.grid(row=4, column=1, sticky='nesw')

    b3 = Button(root, text="Next", command=decrement, borderwidth=0)
    b3.grid(row=3, column=1, sticky='nesw')

    b4 = Button(root, text="Copy", command=copy_from_gui_value, borderwidth=0)
    b4.grid(row=4, column=0, sticky='nesw')

    # Insert The Fact. 
    T.insert(END, Fact)
    N.insert(END, array_current_position+1)
    T.config(state=DISABLED)

    mainloop()


def exit1():
    """
    exit function.
    """
    global thread_kill
    global root
    root.destroy()
    thread_kill = False


def update_on_new_copy():
    """
    Update GUI on each new copy
    """
    global array_current_position
    global Fact
    array_current_position = len(copy_array) - 1
    T.config(state=NORMAL)
    T.delete(1.0, END)
    Fact = copy_array[array_current_position]
    N.delete(1.0, END)
    N.insert(1.0, len(copy_array) - array_current_position)
    T.insert(END, Fact)
    T.config(state=DISABLED)


def decrement():
    """
    Update GUI on button click
    """
    global array_current_position
    global Fact
    if array_current_position == len(copy_array) - 1:
        return
    T.config(state=NORMAL)
    T.delete(1.0, END)
    array_current_position = array_current_position + 1
    Fact = copy_array[array_current_position]
    T.insert(END, Fact)
    N.delete(1.0, END)
    N.insert(1.0, len(copy_array) - array_current_position)
    T.config(state=DISABLED)


def increment():
    """
    Update GUI on button click
    """
    global array_current_position
    global Fact
    if array_current_position <= 0:
        return
    T.config(state=NORMAL)
    T.delete(1.0, END)
    array_current_position = array_current_position - 1
    Fact = copy_array[array_current_position]
    T.insert(END, Fact)
    N.delete(1.0, END)
    N.insert(1.0, len(copy_array) - array_current_position)
    T.config(state=DISABLED)


def update_clipboard():
    """
    Function to keep watching for clipboard update.
    Sleep time 0.5 second by default.
    Updates only when current and last clip do not match.
    """
    global counter
    global thread_kill
    copy_array.append(pyperclip.paste())
    while thread_kill:
        # print("loop") # Debug
        # print(counter) # Debug
        time.sleep(0.3)
        if copy_array[counter] != pyperclip.paste():
            counter += 1
            copy_array.append(pyperclip.paste())
            update_on_new_copy()
            # print("changed") # Debug
            # print("changed") # Debug
            # print("changed") # Debug
            # print(*copy_array, sep=", ") # Debug
            # print("############################################") # Debug


def copy_from_gui_value():
    """
    copy value from the GUI value
    """
    # print(Fact) # Debug
    pyperclip.copy(Fact)


def key_increment(event):
    """
    keypress event W
    """
    increment()


root.bind('<w>', key_increment)


def key_decrement(event):
    """
    Keypress event S
    """
    decrement()


root.bind('<s>', key_decrement)


def func_gui(event):
    """
    Keypress event Q
    Minimize the window
    """
    root.wm_state('iconic')


root.bind('<q>', func_gui)


def copy_from_gui(event):
    """
    keypress event C
    """
    copy_from_gui_value()
    root.wm_state('iconic')


root.bind('<c>', copy_from_gui)


def on_closing():
    """
    Ask before closing the window
    """
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        exit1()


# root.protocol("WM_DELETE_WINDOW", on_closing)
root.protocol("WM_DELETE_WINDOW", exit1)


def main():
    """
    Call everything here
    """

    # Thread for making the clipboard update process in the background
    download_thread = threading.Thread(target=update_clipboard)
    download_thread.start()

    gui()


"""
Process and Error Handling
"""
# Detach from terminal
if os.fork():
    sys.exit()

"""
class DevNull:
    def write(self, msg):
        pass


sys.stderr = DevNull()
"""

main()
