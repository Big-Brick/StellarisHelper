from Code.Views.InfoView import InfoView
from Code.Toolbars.MainMenuToolbar import MainMenuToolbar


class GUI:

	def __init__(self, window):
		self.window = window
		self.InfoView = InfoView(self)
		self.MainMenuToolbar = MainMenuToolbar(self)
		self.CurrView = self.InfoView
		self.CurrView.open()
