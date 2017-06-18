import os  
import sys
import requests
import datetime

if len(sys.argv) != 3:  
    print "Usage: python retrieve.py domain api_key"
    sys.exit(1)

# map input variables to parameters
domain = sys.argv[1] 
api_key = sys.argv[2] 

# mailgun events retrieval url, CHANGE IT if Mailgun changes there API endpoint
events_url = "https://api.mailgun.net/v3/" + domain +"/events"

print("------------- fetching first page (upto 100 emails) -----------")

while True:

	mglogs = requests.get(
        	events_url,
        	auth=("api", api_key),
        	params={"event" : "delivered"})

	for items_list in mglogs.json()["items"]:

		file_name = items_list["recipient"] + "-" + str(datetime.datetime.fromtimestamp(items_list["timestamp"]).strftime('%Y-%m-%d-%H%M%S')) + ".eml"
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

