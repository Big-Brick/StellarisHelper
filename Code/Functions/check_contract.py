total_profit_threshold = 150000000
total_eff_threshold = 1.5


def check_contract(contract, reason=False):
	res = str()
	total_price = contract["price"]
	total_value = contract["reward"]
	total_am = 0
	for Item in contract["Items"]["Offer"]:
		if Item["JitaOrdersAm"] < 30:
			continue
		value = Item["price"]
		try:
			runs = Item["runs"]
			if value <= 0:
				continue
			try:
				value = Item["SellCost"]
				isk_per_sec = Item["price"]/Item["ManufacturingTime"]
				eff = Item["SellCost"]/Item["ProdCost"]
				cont = True
#				if isk_per_sec > 15000:
#					cont = False
				if Item["price"] > 50000000:
					if reason:
						res += "%s: price %f\n" % (Item["name"], Item["price"])
					cont = False
				if eff > 1.4 and Item["SellCost"] > 2000000:
					if reason:
						res += "%s: eff %f, SellCots %f\n" % (Item["name"], eff, Item["SellCost"])
					cont = False
				if cont:
					continue
				am = Item["quantity"]*runs
				total_price += Item["ProdCost"]*Item["quantity"]*runs
			except KeyError:
				try:
					print("check_contract: WTF %d" % (contract["contract_id"]))
					continue
				except Exception as e:
					print(e)
					print("check_contract: WTF WTF")
					continue
		except KeyError:
			if value < 5000000:
				continue
			am = Item["quantity"]
			runs = 1
		if value > 0:
			if reason:
				res += "%s value %f\n" % (Item["name"], value*Item["quantity"]*runs)
			total_value += value*Item["quantity"]*runs
			total_am += am
	for Item in contract["Items"]["Demand"]:
		price = Item["price"]
		if price > 0:
			total_price += price * Item["quantity"]
	if total_price == 0:
		if reason:
			res += "False\n"
			return res
		return False
	eff = total_value / total_price
	if eff > total_eff_threshold:
		if reason:
			res += "total_value: %f, total_price: %f, total_value/total_price %f\n" % \
				(total_value, total_price, total_value/total_price)
			return res
		return True
	if total_am > 0 and eff > 1.1 and (total_value - total_price) > 20000000 and (eff - 1) / total_am > 0.17:
		if reason:
			res += "(eff - 1) / total_am = %f\n" % ((eff - 1) / total_am)
			return res
		return True
#	if (total_value - total_price) > total_profit_threshold:
#		if reason:
#			res += "total_value: %f, total_price: %f, total_value - total_price %f\n" % \
#				(total_value, total_price, total_value - total_price)
#			return res
#		return True
	if reason:
		res += "False\n"
		return res
	return False
