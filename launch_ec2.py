import boto3


# runnig ec2 instance

def run_ec2():
    # open managment console
    aws_managment_console = boto3.session.Session(profile_name="default")
    # open ec2 console
    ec2_console = aws_managment_console.client("ec2")
    # print(ec2_console)

    response = ec2_console.run_instances(
        ImageId = 'ami-08d8ac128e0a1b91c',
        InstanceType = "t2.micro",
        MaxCount=1,
        MinCount=1
    )
    print("EC2 instance started:")
    print(response)

    return ec2_console
# run_ec2()


def stopInstacnes(ec2_console):

    response = ec2_console.stop_instances(
        InstanceIds=['i-03bd848d9afe3a6d5']
)
    print("EC2 instance stopped:")
    print(response)

# stopInstacnes()


def start_instances(ec2_console):

    response = ec2_console.start_instances(
        InstanceIds=['i-03bd848d9afe3a6d5']
)
    print("EC2 instance started:")
    print(response)



def terminate_instances(ec2_console):

    response = ec2_console.terminate_instances(
        InstanceIds=['i-0aaf6c349c8b94a1f', 'i-0ecf72ca9e431623e']
)
    print("EC2 instance terminated:")
    print(response)

terminate_instances()

# main flow
# ec2_console = run_ec2()
# start_instances(ec2_console)
# stopInstacnes(ec2_console)
# terminate_instances(ec2_console)