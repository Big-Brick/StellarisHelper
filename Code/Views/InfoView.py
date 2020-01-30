import tkinter

from Code.Classes.Database import Info
from Code.Functions.dict_to_table import dict_to_table
from Code.Toolbars.OutputToolbar import OutputToolbar


class InfoView:
	def __init__(self, __gui):
		self.GUI = __gui
		self.OutputToolbar = OutputToolbar(self.GUI, 30, 10)
		self.OutputToolbar.SetNewText(dict_to_table(Info.data))
		self.update_button = tkinter.Button(self.GUI.window, command=self.update_info, text="Update Info")

	def open(self):
		self.GUI.CurrView.close()
		self.GUI.MainMenuToolbar.open(0, 0, 1, 1)
		self.OutputToolbar.open(1, 0, 1, 1)
		self.update_button.grid(row=2, column=0)
		self.GUI.CurrView = self

	def close(self):
		self.GUI.MainMenuToolbar.close()
		self.OutputToolbar.close()
		self.update_button.grid_forget()

	def update_info(self):
		Info.update()
		self.OutputToolbar.SetNewText(dict_to_table(Info.data))
