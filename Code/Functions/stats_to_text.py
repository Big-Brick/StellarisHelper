from Code.Functions.SplitStrNumber import SplitNumber


def stats_to_text(stats):
	res = "%s %d:\n" % (stats["name"], stats["ProdGroupID"]) + \
			"%d\n" % stats["type_id"] + \
			"ProdCost: %s" % SplitNumber(stats["ProdCost"]) + \
			" SellCost : %s\n" % SplitNumber(stats["SellCost"]) + \
			"Rating: %s " % SplitNumber(stats["Rating"]) + \
			"Price: %s\n\n\n" % SplitNumber(stats["price"])
	return res