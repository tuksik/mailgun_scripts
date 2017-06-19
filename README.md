# Mailgun Utility scripts for operations

### Script #1: download_all_messages.py

This Python script downloads all messages stored in Mailgun (note that mailgun stores mails for 3 days) and saves it as .eml files in the folder in which script gets executed.

#### Input parameters:

**domain** :  Domain name in Mailgun for which stored emails have to be downloaded

**api_key** : Secret API Key of your mailgun account, this can be found in your dashboard, starts with **key-**

#### Hardcoded parameters

**events_type** : this applies filter on which event types should be fetched, change it to your needs, documentation on various event types availabe at https://documentation.mailgun.com/en/latest/api-events.html#event-types

**delta_days** : this controls how many days of stored emails you would like to download, default value set as 3 as mailgun stores 3 days of mails as a default



#### Usage example:
`python download_all_messages.py samples.mailgun.org key-123a1a1abc12a1a1234567a123456a1a`
