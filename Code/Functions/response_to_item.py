def response_to_item(jsn, blueprint=None):
	item = dict()
	item["name"] = jsn["name"]
	item["type_id"] = jsn["type_id"]
	item["group_id"] = jsn["group_id"]
	if blueprint is not None:
		item["ProdCost"] = blueprint["ProdCost"]
		item["SellCost"] = blueprint["SellCost"]
		item["price"] = blueprint["price"]
		item["Production"] = blueprint["Production"]
		item["JitaOrdersAm"] = blueprint["JitaOrdersAm"]
		item["ManufacturingTime"] = blueprint["ManufacturingTime"]
	return item
