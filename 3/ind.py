import tkinter



window = tkinter.Tk()

p = [1, -34, 8, 14, -5, 1] 
count = 0 
for i in range(len(p) - 1): 
    if (p[i] > 0 and p[i + 1] < 0) or (p[i] < 0 and p[i + 1] > 0):         
        count += 1 
    print(count)

button = tk.Button(
    text="е",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

button.pack()
window.mainloop()
