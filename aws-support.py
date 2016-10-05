
import boto3
import json
import pprint


print "AWS Support API Demo"

# s3client = boto3.client('s3')

# This is where we create the JSON as a string
# json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

# This is where we parse the JSON files
#parsed_json = json.loads(json_string)
#print(parsed_json['first_name'])
#print(parsed_json['last_name'])

#my_buckets = s3client.list_buckets()
#print my_buckets

#print (my_buckets['Buckets'])
#print json.dumps(my_buckets, sort_keys=True, indent=4)

# Real stuff begins here...

client = boto3.client('support')

# Create a test case

codes = client.describe_severity_levels(
    language='en'
)


#print (codes.keys())
levels = codes['severityLevels']
print type(levels)

for i in range(len(levels)):
    line = levels[i]
    print line['name']
	
	
	# print line['code']
#     print line['name']
    	


services = client.describe_services()

#pp = pprint.PrettyPrinter()
#pp.pprint(services)



# response = client.create_case(
#     subject='Test case - Please Ignore',
#     serviceCode='other',
#     severityCode='low',
#     categoryCode='',
#     communicationBody='string',
#     ccEmailAddresses=[
#         'string',
#     ],
#     language='string',
#     issueType='string',
#     attachmentSetId='string'
# )




#response = client.describe_trusted_advisor_checks (language='en')
# json.dumps(response)

