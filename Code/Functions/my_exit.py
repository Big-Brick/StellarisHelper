import Code.MyThread
from Code.Classes import Database


def my_exit():
	for thread in Code.MyThread.Threads:
		thread.stop()
	all_dead = True
	for Thread in Code.MyThread.Threads:
		if Thread.thread.is_alive():
			all_dead = False
			break
	if all_dead:
		Database.Info.dump()
		exit(0)
