from Code.GUI import GUI

import tkinter, Code.MyThread

from Code.Functions import my_exit


def main():
	Code.MyThread.Counter = 0
	main_window = tkinter.Tk()
	main_window.geometry("800x600")
	Interface = GUI(main_window)
	main_window.mainloop()


if __name__ == "__main__":
	try:
		main()
		my_exit.my_exit()
	except Exception as e:
		print(e)