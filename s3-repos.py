'''
Created on Feb 3, 2016

@author: farazr
'''

import boto3

s3 = boto3.resource('s3')


for bucket in s3.buckets.all():
    print (bucket.name)
    
    # Comment from Eclipse Project

# silvax



