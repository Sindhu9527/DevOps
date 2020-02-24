# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:35:13 2020

@author: sindh
"""
import boto3
rek = boto3.client('rekognition')
key = boto3.client('s3')
bucketname = 'BUCKET NAME'
response = key.list_objects_v2(Bucket=bucketname)
for user in response['Contents']:
        s3key=user['Key']
        imagerekognition=rek.detect_labels(
    Image={
        'S3Object': {
            'Bucket' : bucketname,
            'Name' : s3key
            }
               }
            )
        print(imagerekognition)

