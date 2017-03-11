#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
try:
	import ujson as json
except ImportError:
	import json
from htmltext import *

def main(argv):
	for arg in argv[1:]:
		with open(arg, "rb") as f:

			opcodes = json.loads(f.read())

			title = u"x86"
			result = [""]
			text = HtmlText()
			text.append(OpenTag("html"))
			text.append(OpenTag("head"))
			text.append(OpenTag("meta", attributes={"charset": "UTF-8"}, self_closes=True))
			text.append(OpenTag("link", attributes={"rel": "stylesheet", "type": "text/css", "href": "style.css"}, self_closes=True))
			text.append(OpenTag("title"))
			text.append(title)
			text.append(CloseTag("title"))
			text.append(CloseTag("head"))
			text.append(OpenTag("body"))

			text.append(OpenTag("table", attributes={"class": "opcodes"}))

			columns = ["Opcode", "Instruction", "Description"]

			text.append(OpenTag("tr"))
			for column in columns:
				text.append(OpenTag("th"))
				text.append(column)
				text.append(CloseTag("th"))
			text.append(CloseTag("tr"))

			for opcode in opcodes:
				text.append(OpenTag("tr"))
				for column in columns:
					value = opcode[column]
					text.append(OpenTag("td"))
					text.append(value)
					text.append(CloseTag("td"))
				text.append(CloseTag("tr"))

			text.append(CloseTag("table"))

			with open("html/_opcodes.html", "wb") as g:
				g.write("<!DOCTYPE html>\n" + text.to_html().encode('ascii', 'xmlcharrefreplace'))


if __name__ == "__main__":
	result = main(sys.argv)
	sys.exit(result)
