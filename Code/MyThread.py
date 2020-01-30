import threading


Counter = int()
Threads = list()


class MyThread:
	def __init__(self, target, args, stop_event, pause_event):
		args = args + (stop_event, pause_event)
		self.thread = threading.Thread(target=target, args=args)
		self.stop_event = stop_event
		Threads.append(self)

	def start(self):
		self.thread.start()

	def stop(self):
		if self.thread.is_alive():
			self.stop_event.set()
