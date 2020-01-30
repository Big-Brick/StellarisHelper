import pickle
import os

from .globals import DatabaseLock, database_file

def parse_file(file, data):
	stack = list()

def update(self):
	self.data = dict()
	DatabaseLock.acquire()
	self.data["TheForge"] = tmp1
	DatabaseLock.release()
	try:
		DatabaseLock.acquire()
		pickle.dump(self.data, open(database_file, "xb"))
		DatabaseLock.release()
	except FileExistsError:
		pickle.dump(self.data, open(database_file, "wb"))
		DatabaseLock.release()
	except Exception as e:
		DatabaseLock.release()
		raise e
