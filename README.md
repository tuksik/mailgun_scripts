Mailgun Utility scripts for operations

Script #1: download_all_messages.py

This Python script downloads all messages stored in Mailgun (note that mailgun downloads mails for 3 days) and saves it as .eml files in the folder in which script gets executed.

Input parameters:
domain :  Domain name in Mailgun for which stored emails have to be downloaded
api_key : Secret API Key of your mailgun account, this can be found in your dashboard, starts with key-

Usage example:
python download_all_messages.py samples.mailgun.org key-123a1a1abc12a1a1234567a123456a1a
