
################################################################################
#                             Tk Progress Bar Usage                            #
################################################################################

# Usage of TkProgressBar class


################################################################################
#                                    IMPORTS                                   #
################################################################################

from tkinter import *
from modules.tk_progressbar import Tkprogressbar
import time


################################################################################
#                                   FUNCTIONS                                  #
################################################################################

def animate():
    # Animate progress bar
    # ******************************************************
    for val in range(0, 101, 1):
        bar.set_value(val)
        time.sleep(0.02)


################################################################################
def button1_click():
    # Show progress bar demo
    # ******************************************************
    button1.config(state="disabled")  # Disable Button

    bar.pack()  # Show Widget

    bar.config(showtxt=True, color='#408040')
    animate()

    bar.config(showtxt=False, color='#404080')
    animate()

    bar.pack_forget()  # Hide Widget

    button1.config(state="normal")  # Enable Button


################################################################################
#                                     MAIN                                     #
################################################################################

# Create UserForm (Tkinter Window)
userform = Tk()
userform.title("Tk Progress Bar Usage")
userform.geometry("740x150")
userform.resizable(width=False, height=False)
userform.config(background='#404040')

# Create Button in UserForm
button1 = Button(userform, text="Start demo", font=("Arial", 20), bg='#808080', fg='#101010', command=button1_click)
button1.pack(pady=20)

# Create ProgressBar in UserForm (Pack only when used)
bar = Tkprogressbar(userform, length=640, bg='#202020', color='#408040', fg="#B0B0B0",
                    value=0, maximum=100, showtxt=True)
# bar.pack()

# Display UserForm
userform.mainloop()


################################################################################
#                                      EOF                                     #
################################################################################
