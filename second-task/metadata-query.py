import boto3
import json

# Create a client for the EC2 service
session = boto3.Session(profile_name='default')
ec2_client = session.client('ec2',)

# Get the instance ID from the EC2 metadata
response = ec2_client.describe_instances()

# print(type(response))
print(json.dumps(response, indent=4, default=str))
instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']
# print(instance_id)

# Get the instance metadata
response = ec2_client.describe_instances(InstanceIds=[instance_id])
instance = response['Reservations'][0]['Instances'][0]


#print(instance)

# Create a dictionary of the metadata
metadata = {
"instance_id": instance["InstanceId"],
"instance_type": instance['InstanceType'],
"availability_zone": instance['Placement']['AvailabilityZone'],
"ImageId": instance['ImageId'],
"VPC_ID": instance['VpcId'],
"Monitoring": instance["Monitoring"],
"VolumeId" : instance["BlockDeviceMappings"][0]["Ebs"]["VolumeId"]
# "region": instance['Placement']['RegionName']
}

# print(metadata)
# Format the dictionary as JSON
json_metadata = json.dumps(metadata)

# Print the JSON output
print(json_metadata)
