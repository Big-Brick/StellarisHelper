from Code.Classes.Database import Info


def get_parsed_stats(key, force_update=False):
	try:
		item = Info.get_item(key, force_update)
	except Exception:
		return None
	stats = dict()
	try:
		stats["name"] = item["name"]
		stats["type_id"] = item["type_id"]
		stats["ProdCost"] = item["ProdCost"]
		stats["SellCost"] = item["SellCost"]
		stats["price"] = item["price"]
		stats["ProdGroupID"] = item["Production"]["group_id"]
		if stats["price"] > 0:
			stats["Rating"] = stats["price"] * (stats["price"] / stats["ProdCost"])
		else:
			stats["Rating"] = 0
	except KeyError:
		print("Key error id - %d" % key)
		if force_update:
			return None
		else:
			return get_parsed_stats(key, force_update=True)
	except ZeroDivisionError:
		stats["Rating"] = stats["price"]
	stats["Mark"] = "id%dm" % key
	return stats
