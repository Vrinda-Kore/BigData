import pika
import os

#Topic Based
routing_key = input("Topic: ")
message = input("msg: ")

#Partitioning the topic
i = int(len(message)/2)
m1=message[0:i]
m2=message[i:len(message)+1]

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#declaring the exchange of topic type
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

#declaring the queue
channel.queue_declare(queue= routing_key,exclusive=False)
channel.queue_bind(exchange='topic_logs', queue=routing_key, routing_key=routing_key)

channel.basic_publish(
    exchange='topic_logs', routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))


os.makedirs(routing_key, exist_ok=True)

partition1=routing_key+"/p1.txt"
partition2=routing_key+"/p2.txt"

file1 = open(partition1, "a")  # append mode
file1.write(m1+"\n")
file1.close()

file2 = open(partition2, "a")  # append mode
file2.write(m2+"\n")
file2.close()
connection.close()
