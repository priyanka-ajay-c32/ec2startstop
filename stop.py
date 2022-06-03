import boto3

# region EC2 instances are in
region = 'us-east-1'
ec2 = boto3.resource('ec2', region_name=region)

# find all instances that are running
all_instances = [i for i in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])]
# get instances with filter of running + with tag `Name`
instances = [i for i in ec2.instances.filter(
  Filters=[
    {
      'Name': 'instance-state-name', 'Values': ['running']
    }, 
    {
      'Name':'tag:J-M', 'Values':['True']
    },
    {
      'Name': 'tag:TBD-S', 'Values': ['True']
    }
  ]
)]
# Filter from all instances the instance that are not in the filtered list
instances_to_stop = [to_stop for to_stop in all_instances if to_stop.id not in [i.id for i in instances]]

# run over your `instances_to_stop` list and stop each one of them
for instance in instances_to_stop:
  try:
    instance.stop()
    print(f'{instance} stopped')
  except:
    print(f'Error stopping {instance}')
