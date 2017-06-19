import os  
import sys
import requests
import datetime
from datetime import datetime, timedelta 

if len(sys.argv) != 3:  
    print "Usage: python download_messages.py domain api_key"
    sys.exit(1)

# map input variables to parameters
domain = sys.argv[1] 
api_key = sys.argv[2] 

# mailgun events retrieval url, CHANGE IT if Mailgun changes there API endpoint
events_url = "https://api.mailgun.net/v3/" + domain +"/events"

# seting default events to load as delivered, change it if you need more event type to download stored emails from, refer https://documentation.mailgun.com/en/latest/api-events.html#event-types for full list of events, you can use OR to specify more than one event type. e.g,. "delivered OR failed OR stored"
events_type = "delivered"

# mailgun stores 3 days delta by default, change this parameter if you need a different range
delta_days = 3
delta_date = (datetime.today() - timedelta(delta_days))


print("------------- fetching first page (upto 100 emails) starting " + delta_date.strftime('%a, %d %b %Y %X -0000') + " -----------")

while True:

	mglogs = requests.get(
        	events_url,
        	auth=("api", api_key),
        	params={"event" : "delivered"
        			, "ascending"   : "yes"
        			# DateTime has to be in this format : "Fri, 15 June 2017 22:00:00 -0000",
        			, "begin"       : delta_date.strftime('%a, %d %b %Y %X -0000')
        			})

	for items_list in mglogs.json()["items"]:

		file_name = items_list["recipient"] + "-" + str(datetime.fromtimestamp(items_list["timestamp"]).strftime('%Y-%m-%d-%H%M%S')) + ".eml"
		print("creating : " + file_name)
		# set headers and download content from api
        	headers = {"Accept": "message/rfc2822"}
		r = requests.get(items_list["storage"]["url"], auth=("api", api_key), headers=headers)
		if r.status_code == 200:
    			# dump the body to a file
    			with open(file_name, "w") as message:
        			message.write(r.json()["body-mime"])
        			print("ok")
		else:  
    			print "Oops! Something went wrong: %s" % r.content
	
	events_url = mglogs.json()["paging"]["next"]
	
	print("------------- fetching next page (upto 100 emails) -----------")

