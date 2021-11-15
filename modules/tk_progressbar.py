
################################################################################
#                                 TkProgressBar                                #
################################################################################

"""Provide a Tkinter ProgressBar widget without Ttk"""


################################################################################
#                                    IMPORTS                                   #
################################################################################

from tkinter import Canvas


################################################################################
#                                   FUNCTIONS                                  #
################################################################################

# No function for this module


################################################################################
#                                     CLASS                                    #
################################################################################

class Tkprogressbar(Canvas):
    """<class 'Tkprogressbar'> widget to show progression status."""
    # ******************************************************

    def __init__(self, master, **kw):
        """Construct a ProgressBar widget with the parent MASTER.

        Valids arguments names: length, bg, color, fg, value, maximum, showtxt"""
        # ------------------------------
        # Configurable Properties 'kwargs'
        self.sprwdth = 100                 # SuperWidth           'length'
        self.sprcolor = '#E4E4E4'          # SuperColor           'bg'
        self.barcolor = '#808080'          # BarColor             'color'
        self.txtcolor = '#1B1B1B'          # TextColor            'fg'
        self.value = 0                     # ProgressBarValue     'value'
        self.maximum = 100                 # ProgressBarMaximum   'maximum'
        self.shwtxt = True                 # ShowTextOption       'showtxt'

        # Calculable Properties
        self.barposx = 0                   # BarPositionX
        self.txtstr = "0%"                 # TextString
        self.txtposx = 50                  # TextPositionX

        # Constant Properties
        self.sprhght = 20                  # SuperHeight
        self.barposy = 20                  # BarPositionY
        self.txtposy = 10                  # TextPositionY

        # Set properties from kwargs
        self.set_all(**kw)

        # Create parent canvas (Initialisation)
        super().__init__(master, width=self.sprwdth, height=self.sprhght, bg=self.sprcolor,
                         bd=0, highlightthickness=0, state='disabled')

        # Create bar primitive (Initialisation)
        self.bar = super().create_rectangle(0, 0, self.barposx, self.barposy, fill=self.barcolor,
                                            width=0, state='disabled')

        # Create text primitive (Initialisation)
        self.txt = super().create_text(self.txtposx, self.txtposy, text=self.txtstr, fill=self.txtcolor,
                                       font=('Courier New', 16, 'bold'), anchor='center', state='disabled')
        # ------------------------------

    def set_all(self, **kw):
        """Set configurable properties from kwargs and re-calculate all"""
        # ------------------------------
        if 'length' in kw:
            self.sprwdth = kw['length']
            self.txtposx = self.sprwdth // 2

        if 'bg' in kw:
            self.sprcolor = kw['bg']

        if 'color' in kw:
            self.barcolor = kw['color']

        if 'fg' in kw:
            self.txtcolor = kw['fg']

        if 'value' in kw:
            self.value = kw['value']

        if 'maximum' in kw:
            self.maximum = kw['maximum']

        if 'showtxt' in kw:
            self.shwtxt = kw['showtxt']
            self.txtstr = ""

        self.set_bar()
        # ------------------------------

    def set_bar(self):
        """Set progress bar properties only"""
        # ------------------------------
        if self.value > self.maximum:
            self.value = self.maximum

        if self.value < 0:
            self.value = 0

        self.barposx = int(self.value / self.maximum * self.sprwdth)

        if self.shwtxt:
            self.txtstr = f"{int(self.value / self.maximum * 100)}%"
        # ------------------------------

    def update_all(self):
        """Update parent canvas and primitives"""
        # ------------------------------
        # Update parent canvas
        super().config(width=self.sprwdth, bg=self.sprcolor)

        # Update bar primitive
        super().coords(self.bar, 0, 0, self.barposx, self.barposy)
        super().itemconfig(self.bar, fill=self.barcolor)

        # Update text primitive
        super().coords(self.txt, self.txtposx, self.txtposy)
        super().itemconfig(self.txt, text=self.txtstr, fill=self.txtcolor)

        # Update display
        super().update()
        # ------------------------------

    def update_bar(self):
        """Update primitives only"""
        # ------------------------------
        # Update bar primitive
        super().coords(self.bar, 0, 0, self.barposx, self.barposy)

        # Update text primitive
        if self.shwtxt:
            super().itemconfig(self.txt, text=self.txtstr)

        # Update display
        super().update()
        # ------------------------------

    def config(self, **kw):
        """Set widget configuration from kwargs"""
        # ------------------------------
        self.set_all(**kw)
        self.update_all()
        # ------------------------------

    def set_value(self, value):
        """Set progress bar current value"""
        # ------------------------------
        self.value = value
        self.set_bar()
        self.update_bar()
        # ------------------------------

    def set_maximum(self, value):
        """Set progress bar maximum value"""
        # ------------------------------
        self.maximum = value
        self.set_bar()
        self.update_bar()
        # ------------------------------

    def showinfo(self):
        """Display progress bar properties"""
        # ------------------------------
        print("---------------- Configurable Properties")
        print("length:", self.sprwdth)
        print("bg:", self.sprcolor)
        print("color:", self.barcolor)
        print("fg:", self.txtcolor)
        print("value:", self.value)
        print("maximum:", self.maximum)
        print("showtxt:", self.shwtxt)

        print("------------------ Calculable Properties")
        print("BarPositionX:", self.barposx)
        print("TextString:", self.txtstr)
        print("TextPositionX:", self.txtposx)

        print("-------------------- Constant Properties")
        print("SuperHeight:", self.sprhght)
        print("BarPositionY:", self.barposy)
        print("TextPositionY:", self.txtposy)
        # ------------------------------


################################################################################
#                                      EOF                                     #
################################################################################
