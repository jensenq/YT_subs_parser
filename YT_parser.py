###########################################################
#                                                         #
# Directions:                                             #
#	1: go to https://www.youtube.com/subscription_manager #
#	2: scroll to bottom, click Export Subscriptions       #
#	3: save as "subscription_manager.rss" to the same     #
#		folder as this file                               #
#	4: python3 YT_parser.py                               #
#                                                         #
###########################################################

from xml.etree import ElementTree

with open("subscription_manager.rss", "rt") as rss:
	tree = ElementTree.parse(rss)

with open("YT_subs.txt", "w+") as f:

	for node in tree.findall(".//outline"):
		name = node.attrib.get("text")
		url = node.attrib.get("xmlUrl")
	
		if(name and url):
			f.write("%s\n%s\n\n" % (name, url)) 

f.close
rss.close



