import requests

from time import sleep

from Code.Classes.Database import Info


def MyWait(stop_event, pause_event):
	while pause_event.isSet() and not stop_event.isSet():
		sleep(1)
	if stop_event.isSet():
		return "Exit"
	return "Continue"


def parse_page(page, location_id, callback, stop_event, pause_event):
	bot = 100000000
	top = 200000000
	for order in page:
		if MyWait(stop_event, pause_event) == "Exit":
			return None
		price = int(order["price"])
		order_location = order["location_id"]
		if order_location == location_id and\
			bot <= price <= top:
			item = Info.get_item(str(order["type_id"]))
			if item is not None:
				if MyWait(stop_event, pause_event) == "Exit":
					return None
				callback(item["name"] + " " + str(item["type_id"]) + " " + str(order["price"]))


def parallel_market_request(region_id, location_id, callback, stop_event, pause_event):
	request = "https://esi.evetech.net/latest/markets/%s/" \
		"orders/?datasource=tranquility&order_type=sell&page=1" % region_id
	if MyWait(stop_event, pause_event) == "Exit":
		return None
	response = requests.get(request)
	if MyWait(stop_event, pause_event) == "Exit":
		return None
	pages = int(response.headers["x-pages"])
	parse_page(response.json(), location_id, callback, stop_event, pause_event)
	for i in range(2, pages + 1):
		if MyWait(stop_event, pause_event) == "Exit":
			return None
		request = "https://esi.evetech.net/latest/markets/%s/" \
			"orders/?datasource=tranquility&order_type=sell&page=%d" % (region_id, i)
		response = requests.get(request)
		parse_page(response.json(), location_id, callback, stop_event, pause_event)


def parallel_request(request, callback, stop_event, pause_event):
	if MyWait(stop_event, pause_event) == "Exit":
		return None
	response = requests.get(request % 1)
	if MyWait(stop_event, pause_event) == "Exit":
		return None
	if response.status_code is not 200:
		stop_event.set()
		return None
	pages = int(response.headers["x-pages"])
	for Item in response.json():
		if MyWait(stop_event, pause_event) == "Exit":
			return None
		callback(Item)
	for i in range(2, pages + 1):
		if MyWait(stop_event, pause_event) == "Exit":
			return None
		response = requests.get(request % i)
		if response.status_code == 200:
			for Item in response.json():
				if MyWait(stop_event, pause_event) == "Exit":
					return None
				callback(Item)
	print("End")
