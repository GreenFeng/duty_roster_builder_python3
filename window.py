import tkinter as tk

def date_add():
	print("add date")

root = tk.Tk('order')
root.title('order system')

group_cmd = tk.Frame(root)
group_cmd.config(bd=3,relief=tk.RAISED)
group_cmd.pack(expand=tk.YES,fill=tk.X)

welcome = tk.Label(group_cmd,text="welcome to order system")
welcome.pack(side=tk.TOP)
welcome.config(fg='green')

group_b = tk.Frame(root)
group_b.pack(side=tk.RIGHT)
group = []
for n in range(3):
	group.append( tk.Frame(group_b).config(bd=10).grid() )
	# group[n].config(bd=10)
	# group[n].grid()

group_t = tk.Frame(root)
group_t.pack(side=tk.LEFT)
t_lable = []
t_lable_name = ["AM","PM","EV"]
for n in range(3):
	t_lable.append( tk.Label(group_t,text=t_lable_name[n]) )
	t_lable[n].pack()

group_button = []
time = ["am1","am2","pm1","pm2","ev1","ev2"]
for day in range(7):
	for period in range(6):
		num = int(period/2)
		group_button.append(tk.Button(group[num],text=time[period],command=date_add))
		group_button[day*6+period].grid(row=period,column=day)

# white_bord = tk.Text(root)
# white_bord.pack(expand=tk.YES,fill=tk.BOTH)

root.mainloop()
