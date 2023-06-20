import pika
import sys
from pyrabbit.api import Client

#Creating connection and establishing channel
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()



cl = Client('localhost:15672', 'guest', 'guest')
queues = [q['name'] for q in cl.get_queues()]


#exchange type : topic
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

'''result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue'''

#binding the consumer to its respective queue
binding_keys=input("Enter topic name : ")
'''binding_keys=binding_keys.split(" ")'''

#binding_keys = sys.argv[1:]

if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)
    
    
    
if binding_keys not in queues:
    channel.queue_declare(queue=binding_keys, exclusive=False)
    channel.queue_bind(exchange='topic_logs', queue=binding_keys, routing_key=binding_keys)

'''for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)
'''
print(' [*] Waiting for logs. To exit press CTRL+C')

#displaying of messages of the topic subscribed by the consumer

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(queue=binding_keys, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
