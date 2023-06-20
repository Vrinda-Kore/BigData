# BD1_513_588_591_604

Project Title: Yet another Kafka (YaK)

Implemented through : Rabbitmq

# Functionality :
 
 - Our project Yet Another Kafka involves mimicing the kafka architecture using RabbitMQ.

 - Exchange Type : Topic 

 - The publisher(multiple) emits/publishes topics to the broker and the consumer(multiple) consumes the emitted messages from the broker based on specified topics.

 - The queues aka brokers gets monitored for every 5 seconds.

# Files present :
  
  1.Sub_prod.py
  
            - Create subprocess for the number of producers dynamically specified by user.
            
            - View and Delete existing queues.
            
   2.send_cmd.py
   
            - Receives topic and corresponding message from the user
            
            - Creates Topic-based exchange and queues.
            
            - Publishes the content with routing_key as topic name to the broker(exchange+queue).The messages are partitioned and stored in log files of that directory with directory name as topic.
            
            -The exchange and queues are bound and routed based on binding key.
  
   3.receive_cmd.py
   
            - Receives topic to be subscribed from the user.
            
            - Subscribes(matches topic name with the binding key) and displays the content with routing_key as topic name to the broker(exchange+queue).

   4.rabbit_monitoring.py
   
            - Monitors the status(idle/running),ready(number of messages in queue not yet been subscribed),unacknowledged(number of messages subscribed but not acknowledged).
            
# Modules Used :

   1.Pika
   
   2.sys
   
   3.pyrabbit.api
   
   4.os
   
   5.subprocess
   
   6.requests

   7.base64

   8.schedule

   9.tabulate

# Commands to execute

            - python sub_proc.py #To view and delete queues and to call multiple producers
            - python receive_cmd.py #Can run this everytime for each new topic in the terminal
            - python rabbit_monitoring.py #To monitor queues wherein both username and password are guest 
