import tkinter as tk

def color_change():
	bey.config(bg='white')
	change_bg.config(bg='#ffffff',fg='#ffffff')

root = tk.Tk('order')
root.title('order system')

group_cmd = tk.Frame(root)
group_cmd.config(bd=10,relief=tk.RAISED)
group_cmd.pack()

welcome = tk.Label(group_cmd,text="welcome to order system")
welcome.pack(side=tk.TOP)
welcome.config(fg='green',bg='white')

bey = tk.Label(root,text="if you'd like to leve")
bey.pack()
bey.config(fg='#f00101',bg='#20f0f0')

change_bg = tk.Button(root,text='chang color',command=color_change)
# change_bg.grid(row=3,column=3)
change_bg.pack(side=tk.LEFT)
change_bg.config(bg='#506070',fg='#ffffff')

white_bord = tk.Text(root)
white_bord.pack(expand=tk.YES,fill=tk.BOTH)

root.mainloop()
