import tkinter as tk

def date_add():
	print("add date")

root = tk.Tk('order')
root.title('order system')

group_cmd = tk.Frame(root)
group_cmd.config(bd=3,relief=tk.RAISED)
# group_cmd.pack(expand=tk.YES,fill=tk.X)
text = tk.Label(root,text="input the name",fg="red")
text.pack(side=tk.LEFT)
b_t = tk.Frame(root)
b_t.pack()

welcome = tk.Label(group_cmd,text="welcome to order system")
welcome.pack(side=tk.TOP)
welcome.config(fg='green')

group_t = tk.Frame(b_t)
group_t.pack(side=tk.LEFT)
t_lable = []
t_lable_name = [" ","AM","PM","EV"]
for n in range(4):
	t_lable.append( tk.Label(group_t,text=t_lable_name[n]) )
	t_lable[n].grid(pady=20)
t_lable[0].grid(pady=5)

group_b = tk.Frame(b_t)
group_b.pack(side=tk.RIGHT)
group = []
for n in range(2):
	group.append( tk.Frame(group_b) )
	group[n].config(bd=1)
	group[n].grid()

group_button = [None]*49
time = ["上午1","上午2","下午1","下午2","晚上1","晚上2"]
daydate = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
for day in range(7):
	group_button[day]=(tk.Label(group[0],text=daydate[day]))
	group_button[day].grid(row=0,column=day,padx=5,pady=1)
	for period in range(6):
		group_button[(day+1)*6+period]=(tk.Button(group[1],text=time[period],command=date_add))
		group_button[(day+1)*6+period].grid(row=period,column=day,padx=5,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)

# white_bord = tk.Text(root)
# white_bord.pack()

root.mainloop()
