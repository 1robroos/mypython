import boto3
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
print(ec2_con_re.instances)
# dit geeft een object: ec2.instancesCollectionManager(ec2.ServiceResource(), ec2.Instance)
print(dir(ec2_con_re.instances))
# Dit geeft:
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_collection_cls', '_handler', '_model', '_parent', 'all', 'create_tags', 'filter', 'iterator', 'limit', 'monitor', 'page_size', 'pages', 'reboot', 'start', 'stop', 'terminate', 'unmonitor']
# dus op de object heb je deze submethods.


# all,  en limit en filter gaan we nu naar kijken.

print(ec2_con_re.instances.all())
# dit geeft ec2.instancesCollection(ec2.ServiceResource(), ec2.Instance)
# en dat is een iterator.
# dus dan gebruiken we for loop
for each in ec2_con_re.instances.all():
    print(each)

# dit geeft:
# ec2.Instance(id='i-059335ab0f5edc2c2')
# ec2.Instance(id='i-019baeeba894e973e')

for each in ec2_con_re.instances.limit(1):
    print(each)
    
    # dit geeft 1tje: ec2.Instance(id='i-059335ab0f5edc2c2')

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx FILTERS xxxxxxxxxxxxxxxxxxxxxxxxxxx")
# Nu filters
# stel je wil enkel running instances zien:    
# Syntax: f1={"Name": "", "Values":[]}
f1={"Name": "instance-state-name", "Values":["running"]}
for each in ec2_con_re.instances.filter(Filters=[f1]):
    print(each)
# geeft enkel  running instance aan: ec2.Instance(id='i-059335ab0f5edc2c2')    

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx Show running and stopped instances xxxxxxxxxxxxxxxxxxxxxxxxxxx")
f1={"Name": "instance-state-name", "Values":["running","stopped"]}
for each in ec2_con_re.instances.filter(Filters=[f1]):
    print(each)

# Now 2 filters
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx Show running and stopped instances an instance type xxxxxxxxxxxxxxxxxxxxxxxxxxx")
f1={"Name": "instance-state-name", "Values":["running","stopped"]}
f2={"Name": "instance-type", "Values":["t3a.micro"]}
for each in ec2_con_re.instances.filter(Filters=[f1,f2]):
    print(each)