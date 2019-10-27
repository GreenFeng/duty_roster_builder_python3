import tkinter as tk
from tkinter import messagebox
class Windom(object):
	DAY = []
	PERIOD = []
	NAME = []

	def __init__(self):
		self.root = tk.Tk('order')
		self.root.title('order system')
		self.init_cmd()
		self.init_b_t()
		self.t_config()
		self.b_config()
		self.root.mainloop()

	def init_cmd(self):
		self.group_cmd = tk.Frame(self.root,bd=3,relief=tk.RAISED)
		self.group_cmd.pack(expand=tk.YES,fill=tk.X)
		self.Name = tk.StringVar()
		self.Name.set("请输入被排课员工姓名")
		tk.Label(self.group_cmd,text="welcome to order system",fg='green').pack()
		tk.Label(self.group_cmd,text="input the name",fg="red").pack(side=tk.LEFT)
		tk.Entry(self.group_cmd,width=40,textvariable=self.Name).pack(side=tk.LEFT)
		tk.Button(self.group_cmd,command=self.name_get,text="verify").pack(side=tk.LEFT)
		self.State = False
		# tk.Label(self.group_cmd,text="input the name",fg="red").grid(row=1,column=0)
		# tk.Entry(self.group_cmd).grid(row=1,column=1,padx=0,pady=0)
		
	def init_b_t(self):
		self.b_t = tk.Frame(self.root)
		self.b_t.pack()
		self.group_t = tk.Frame(self.b_t)
		self.group_t.pack(side=tk.LEFT)
		self.group_b = tk.Frame(self.b_t)
		self.group_b.pack(side=tk.RIGHT)
		self.group = []
		for n in range(2):
			self.group.append(tk.Frame(self.group_b))
			self.group[n].grid()

	def t_config(self):
		t_lable_name = ["AM","PM","EV"]
		for n in range(3):
			tk.Label(self.group_t,text=t_lable_name[n]).grid(pady=20)

	def b_config(self):
		time = ["上午1","上午2","下午1","下午2","晚上1","晚上2"]
		daydate = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
		self.Bottoms = [None]*49
		for day in range(7):
			self.Bottoms[day*7] = tk.Label(self.group[0],text=daydate[day])
			self.Bottoms[day*7].grid(row=0,column=day,padx=5,pady=1)
			for period in range(1,7):
				com = lambda arg=(day*7+period):self.date_add(arg)
				self.Bottoms[day*7+period] = tk.Button(self.group[1],text=time[period-1],command=com)
				self.Bottoms[day*7+period].grid(row=period+1,column=day,padx=5,pady=2)

	def date_add(self,arg):
		if not self.State:
			messagebox.showinfo(title="f**k",message="the name! input the name!")
		else:
			self.Bottoms[arg].config(bg='red')
			self.DAY.append(int(arg/7)+1)
			self.PERIOD.append(int(arg%7))
			print(self.Name.get())

	def name_get(self):
		self.NAME.append(self.Name.get())
		self.State = True