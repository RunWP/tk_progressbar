# **TkProgressBar v1.0.0**

### *Python (educational project)*

Provide a Tkinter ProgressBar widget without Ttk

## **Usages**
```py
from modules.tk_progressbar import Tkprogressbar
```

#### *Create progress bar*
```py
bar = Tkprogressbar(master, **options)
```

#### ***options*
| Args      | Description            | Default |
|-----------|------------------------|---------|
| length    | Bar length             | 100     |
| bg        | Background color       | #E4E4E4 |
| color     | Progress color         | #808080 |
| fg        | Text color             | #1B1B1B |
| value     | Current progress value | 0       |
| maximum   | Maximum progress value | 100     |
| showtxt   | Text string visible    | True    |

#### *Set progress bar configuration*
```py
bar.config(**options):
```

#### *Set progress bar current value*
```py
bar.set_value(value):
```

#### *Set progress bar maximum value*
```py
bar.set_maximum(value):
```

#### *Show progress bar*
```py
bar.pack()
# or
bar.grid()
```

#### *Hide progress bar*
```py
bar.pack_forget()
# or
bar.grid_forget()
```

## **Project files**

| Path                               | Description              |
|------------------------------------|--------------------------|
| ./modules/tk_progressbar.py        | Progressbar Class Module |
| ./Docs/Tkprogressbar Class Doc.txt | Class description        |
| ./TkProgressBar_Usages.pyw         | Usage exemple            |
| ./README.md                        | This file                |
