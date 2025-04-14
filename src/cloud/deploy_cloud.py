# Exemple de script pour déployer une application sur AWS avec Boto3

import boto3

def deploy_to_aws():
    ec2 = boto3.client('ec2', region_name='us-west-1')
    instances = ec2.run_instances(
        ImageId='ami-0c55b159cbfafe1f0', 
        InstanceType='t2.micro', 
        MinCount=1, 
        MaxCount=1
    )
    print("Instance EC2 lancée avec succès :", instances)

if __name__ == "__main__":
    deploy_to_aws()
