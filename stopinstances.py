import boto3

def check_instance_exists(client, my_instance):
    # to check 
    response = client.describe_instances()
    reservations = response.get("Reservations")
    instances = reservations[0].get("Instances")
    
    for instance in instances:
        instance_id = instance.get("InstanceId")
        if instance_id == my_instance:
            return True
    else:
        return False    
        
def instance_state(client, my_instance):
    # to find the state 
    response = client.describe_instance_status(InstanceIds=[my_instance], IncludeAllInstances=True)
    status = response.get("InstanceStatuses")
    state = status[0].get("InstanceState").get("Name")
    return state

def stop_instance(client, my_instance_id):
    # to stop instance
    response = client.stop_instances(InstanceIds=[my_instance_id])
    stop = response.get("StoppingInstances")
    current_state = stop[0].get("CurrentState").get("Name")
    return current_state

def handle_instance():
    # to handle running instance
    INSTANCE_ID = "i-0b390fedb01d888c6"
    client = boto3.client('ec2')
    check = check_instance_exists(client, INSTANCE_ID)
    if check == False:
        print("No such Instance found")
        exit()
    
    instance_status = instance_state(client, INSTANCE_ID)
    
    if instance_status != 'stopped' and instance_status != 'terminated':
        instance_stop =  stop_instance(client ,INSTANCE_ID)
        print(instance_stop)
    else:
        print("Instance already stopped")

if __name__ == "__main__":
    handle_instance()
