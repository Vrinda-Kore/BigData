import subprocess
import sys
from pyrabbit.api import Client
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

def producers_area():
    no_prod = int(input("producers: "))

    while no_prod > 0:
        print("Producer ", no_prod)
        subprocess.run(["python", "send_cmd.py", ])
        no_prod = no_prod - 1


def main():
    flag = True
    while flag:
        print("Choices:\n1.View all queues\n2.Delete queue\n3.Start Producer")
        choice = int(input("Enter choice:"))
        if choice == 1:
            '''proc = subprocess.Popen("C:/Program Files/RabbitMQ Server/rabbitmq_server-3.11.3/sbin/rabbitmqctl list_queues", shell=True, stdout=subprocess.PIPE)
            stdout_value = proc.communicate()[0]
            print(stdout_value)'''
            cl = Client('localhost:15672', 'guest', 'guest')
            queues = [q['name'] for q in cl.get_queues()]
            print(queues)
        elif choice == 2:
            name = input("Name to be deleted: ")
            channel.queue_delete(queue=name)
            print("Deleted the queue ", name)
        elif choice == 3:
            producers_area()
        else:
            sys.exit(0)


main()
