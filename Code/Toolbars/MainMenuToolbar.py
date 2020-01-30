import tkinter

from Code.Functions.my_exit import my_exit


class MainMenuToolbar:
	def __init__(self, __GUI):
		self.GUI = __GUI
		self.frame = tkinter.Frame(self.GUI.window)

		self.info_button = tkinter.Button(self.frame, command=self.GUI.InfoView.open, text="Info")
		self.info_button.grid(row=0, column=1)

		self.exit_button = tkinter.Button(self.frame, command=my_exit, text="Exit")
		self.exit_button.grid(row=0, column=2)

	def open(self, y, x, rowspan, columnspan):
		self.frame.grid(row=y, column=x, rowspan=rowspan, columnspan=columnspan)

	def close(self):
		self.frame.grid_forget()

