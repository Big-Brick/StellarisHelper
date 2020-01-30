import threading


def parallel_item_action(source_obj, force_update, action, action_arg, lock, errors):
	try:
		action(source_obj, force_update, action_arg, lock, errors)
	except Exception as e:
		lock.acquire()
		errors.append(e)
		lock.release()


def do_parallel_item_actions(objects, force_update, action, action_arg, info=None):
	lock = threading.Lock()
	errors = list()
	threads = list()
	for obj in objects:
		try:
			if info is not None and info.get_item(obj["type_id"], False, True) is not None:
				action(obj, force_update, action_arg, lock, errors)
			else:
				args = (obj, force_update, action, action_arg, lock, errors)
				threads.append(threading.Thread(target=parallel_item_action, args=args))
				threads[-1].start()
		except Exception as e:
			lock.acquire()
			errors.append(e)
			lock.release()
	for thread in threads:
		thread.join()
	if len(errors) is not 0:
		for error in errors:
			print(error)
		return False
	return True
