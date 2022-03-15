#!/usr/bin/python3

# enable debugging
import cgi, cgitb
import json
import requests
import responses
cgitb.enable()

class Expense:
     def __init__(self, exp_name,exp_date,exp_amount,exp_type):
         self.name = exp_name
         self.date = exp_date
         self.amount = exp_amount
         self.type = exp_type

form = cgi.FieldStorage()
exp_name = form.getvalue('exp_name')
exp_date  = form.getvalue('exp_date')
exp_amount = form.getvalue('exp_amount')
exp_type  = form.getvalue('exp_type')

expense = Expense(exp_name,exp_date,exp_amount,exp_type)

jsonString = json.dumps(expense.__dict__)
jsonFile = open("/var/www/html/data.json", "a+")
jsonFile.write(jsonString)
jsonFile.close()


print('Content-Type: text/plain')
print('')
print('sucessful')
print('<br>')
print(jsonString)


