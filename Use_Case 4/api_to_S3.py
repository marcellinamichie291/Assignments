import boto3
import pandas as pd
from configparser import ConfigParser
	
file='api_config.ini'
config=ConfigParser()
config.read(file)
	
s3=boto3.resource(service_name=config['S3']['serviceName'],
	    	  region_name=config['S3']['regionname'],
	    	  aws_access_key_id=config['S3']['aws_access_keyid'],
	    	  aws_secret_access_key=config['S3']['aws_access_key'])
	
# printing all the buckets name present in S3
for bucket in s3.buckets.all():
	print(bucket.name)
	
s3.Bucket(config['S3']['bucket_name']).upload_file(Filename='population.csv', Key='population.csv')
