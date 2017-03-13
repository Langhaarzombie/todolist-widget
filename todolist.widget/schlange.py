#!/usr/local/bin/python3

import json
import sys
from pprint import pprint

#User specific configurations
path_to_todos	=	"/Users/max/.todos.json"
line_spacing 	= 	"10px"
color_id 		= 	"#d75e56"
color_due 		= 	"#f0d847"
color_subject 	= 	"#f2f3fa"

with open( path_to_todos, "r", encoding="utf-8" ) as file:
	data = json.load(file)

out = "<div>"

for i in data:
	if ( not(i['completed'] or i['archived']) ):

		out += "<div style=\"padding-top: "+line_spacing+";\">"

		out += "<div style=\"display: inline; color: "+color_id+";\">"+str(i['id'])

		eyed = int(i['id'])
		if( eyed/10 < 1 ):
			out += "&nbsp;&nbsp;</div>"
		elif( eyed/10 < 10 ):
			out += "&nbsp;</div>"
		else:
			out += "</div>"

		if( str(i['due']) != "" ):
			out += "<div style=\"display: inline; color: "+color_due+";\">"+str(i['due'])+"&nbsp;&nbsp;</div>"
		else:
			out += "<div style=\"display: inline;\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>"

		out += "<div style=\"display: inline; color: "+color_subject+"\">"+i['subject']+"</div>"

		out += "</div>"

out += "</div>"

sys.stdout.buffer.write( out.encode("utf8") )