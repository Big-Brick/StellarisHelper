import pickle, requests, json, threading
from math import floor

regions_file = "Data/regions.pickle"

Lock = threading.Lock()


def get_regions():
	Lock.acquire()
	try:
		regions = pickle.load(open(regions_file, "rb"))
		Lock.release()
		return regions
	except FileNotFoundError:
		pass
	Lock.release()
	region_indexes = json.loads(requests.get("https://esi.evetech.net/latest/universe/regions/?datasource=tranquility").text)
	size = len(region_indexes)
	old_str = ""
	i = 0
	regions = dict()
	for index in region_indexes:
		url = "https://esi.evetech.net/latest/universe/regions/"
		url = url + str(index) + "/?datasource=tranquility&language=en-us"
		region = json.loads(requests.get(url).text)
		regions[region["name"]] = str(index)
		new_str = str(floor(i*100/size)) + "%"
		print("\033[%dD%s" % (len(old_str), new_str), end='', flush=True)
		old_str = new_str
		i += 1
	print("")
	Lock.acquire()
	pickle.dump(regions, open(regions_file, 'xb'))
	Lock.release()
	return regions

