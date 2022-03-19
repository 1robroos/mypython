import boto3
import sys
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
while True:
    print("This script performs the following actions on EC2 instance")
    print("""
          1. start
          2. stop
          3. terminate
          4. exit
          """)
    opt=int(input("Enter your option: "))
    if opt==1:
        instance_id=input("enter your ec2 instance id: ")
        print(instance_id)
        my_req_instance_object=ec2_con_re.Instance(instance_id)
        print(dir((my_req_instance_object)))
        print("Starting EC2 instance ....")
        my_req_instance_object.start()
    elif opt==2:
        instance_id=input("enter your ec2 instance id: ")
        my_req_instance_object=ec2_con_re.Instance(instance_id)
        print("Stopping EC2 instance ....")
        my_req_instance_object.stop()
    elif opt==3:
        instance_id=input("enter your ec2 instance id: ")
        my_req_instance_object=ec2_con_re.Instance(instance_id)
        print("Terminating EC2 instance ....")
        my_req_instance_object.terminate()
    elif opt==4:
        print("Thank you for using this script ")
        sys.exit()
    else:
        print("Your option is invalid, please try again")