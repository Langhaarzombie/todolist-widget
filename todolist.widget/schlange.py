#!/usr/local/bin/python3

import json
import sys
import datetime
from pprint import pprint

#User specific configurations
path_to_todos	=	"/Users/USER/.todos.json"
line_spacing 	= 	"10px"
color_id 		= 	"#d75e56"
color_due 		= 	"#f0d847"
color_subject 	= 	"#f2f3fa"
color_project	=	"#9dd6d8"

def formatDate ( date ):
	return datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%b %d')

def printLineStart ():
	return "<div style=\"padding-top: "+line_spacing+";\">"

def printLineEnd ():
	return "</div>"

def printID ( id ):
	out = "<div style=\"display: inline; color: "+color_id+";\">"+str(id)
	if( id/10 < 1 ):
		out += "&nbsp;&nbsp;</div>"
	elif( id/10 < 10 ):
		out += "&nbsp;</div>"
	else:
		out += "</div>"
	return out

def printDue ( due ):
	if( str(i['due']) != "" ):
		out = "<div style=\"display: inline; color: "+color_due+";\">"+formatDate(i['due'])+"&nbsp;&nbsp;</div>"
	else:
		out = "<div style=\"display: inline;\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>"
	return out

def printSubject ( subject, projects ):
	out = subject
	for i in projects:
		out = out.replace("+"+i, "<div style=\"display: inline; color: "+color_project+";\">"+"+"+i+"</div>")
	out = "<div style=\"display: inline; color: "+color_subject+"\">"+out+"</div>"
	return out

with open( path_to_todos, "r", encoding="utf-8" ) as file:
	data = json.load(file)

out = "<div>"

for i in data:
	if ( not(i['completed'] or i['archived']) ):
		out += printLineStart() + printID( i['id'] ) + printDue( i['due'] ) + printSubject( i['subject'], i['projects'] ) + printLineEnd()

out += "</div>"

sys.stdout.buffer.write( out.encode("utf8") )