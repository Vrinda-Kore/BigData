import sys
import requests
import base64
import schedule
from tabulate import tabulate

# credentials
user = "guest"
password = "guest"
req_headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}



def take_credentials():
    # Since RabbitMQ API uses HTTP Basic authentication
    # we encode username and password into base64 strings
    # and then add it to request header
    credentials = f"{user}:{password}"
    credentials_bytes = credentials.encode("ascii")
    base64_credentials = base64.b64encode(credentials_bytes)
    base64_credentials_string = base64_credentials.decode("ascii")
    req_headers["Authorization"] = f"Basic {base64_credentials_string}"


# monitoring
def monitor():
    print("Monitoring the queues:")
    # send api request to get queue details
    res = requests.get(
        url="http://localhost:15672/api/queues/%2F",
        headers=req_headers)
    # convert res to json
    queues = res.json()

    table_headers = ['name', 'state', 'ready', 'unacknowledged', 'total']
    rows = []

    for queue in queues:
        # Overview
        name = queue['name']
        state = 'idle' if 'idle_since' in list(queue.keys()) else 'running'

        # Messages
        ready = queue['messages_ready']
        unacknowledged = queue['messages_unacknowledged']
        total = queue['messages']

        '''# Message rates
        if 'message_stats' in list(queue.keys()):
            if 'publish_details' in list(queue['message_stats'].keys()):
                incoming = queue['message_stats']['publish_details']['rate']
        else:
            incoming = 0.0'''

        # create a row for a queue
        rows.append([name, state, ready, unacknowledged, total])

    # print queue details
    table = tabulate(rows, headers=table_headers, tablefmt='orgtbl')
    print(table)


def main():
    # take credentials from user
    take_credentials()

    # call monitor every 5 seconds
    schedule.every(5).seconds.do(monitor)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
