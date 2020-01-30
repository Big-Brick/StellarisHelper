import tkinter, threading


class OutputToolbar:
	def __init__(self, __GUI, width, height):
		self.GUI = __GUI
		self.Lock = threading.Lock()
		self.frame = tkinter.Frame(self.GUI.window)
		self.vscrollbar = tkinter.Scrollbar(self.frame)
		self.hscrollbar = tkinter.Scrollbar(self.frame)
		self.vscrollbar.pack(side="right", fill='y')
		self.hscrollbar.pack(side="bottom", fill='x')
		self.output = tkinter.Text(self.frame)
		self.output.configure(yscrollcommand=self.vscrollbar.set)
		self.output.configure(xscrollcommand=self.hscrollbar.set)
		self.output.configure(width=width, height=height, wrap="none")
		self.output.pack(side="left")
		self.vscrollbar.config(command=self.output.yview)
		self.hscrollbar.config(command=self.output.xview, orient='horizontal')

	def open(self, y, x, rowspan, columnspan):
		self.frame.grid(row=y, column=x, rowspan=rowspan, columnspan=columnspan)

	def close(self):
		self.frame.grid_forget()

	def SetNewText(self, text):
		self.Lock.acquire()
		self.output.config(state='normal')
		self.output.delete('0.0', tkinter.END)
		if text is not None:
			self.output.insert(tkinter.END, text)
		self.output.config(state='disabled')
		self.Lock.release()

	def insert(self, text, pos=tkinter.END):
		self.Lock.acquire()
		self.output.config(state='normal')
		self.output.insert(pos, text)
		self.output.config(state='disabled')
		self.Lock.release()

	def insert_line(self, line):
		if self.output.get("1.0", tkinter.END) == "\n":
			self.insert(line)
		else:
			self.insert("\n%s" % (line))
