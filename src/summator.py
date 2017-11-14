#!/usr/bin/env python3
#coding: utf-8
"""
Traffic Summator ver 0.2.0.

Summator trafic from many hosts, store, and redirect to one host

AVedensky 2017
avedensky@gmail.com
"""
import sys
import socket
from argparse import ArgumentParser
from time import sleep
from multiprocessing import Process, Queue

CLIENTS_LIMIT = 30 # limit client connections
DATA_BUFFER = 4096 # size data buffer (bytes)

def get_client_connection(host, port):
    """
    Connect to redirect host as client, repeat while do not SUCCESSFULLY
    """
    connection = socket.socket()    
    while True:
        try:
            connection.connect((host, port))            
            print('SUCCESSFULLY! Connection has been established. ip: {0}, port: {1}'.format(host, port))
            return connection

        except ConnectionRefusedError:            
            print('WARNING! Can\'t connect ip: {0}, port: {1}, Wait connection...'.format(host, port))
            print('Try repeat connect every second... ')
            sleep(1)          


def woker_data_sender(queue_data, host, port):
    """
    Send data if not empty queue
    """
    connection = None
    while True:  
        try:
            connection = get_client_connection (host, port)
            while True: 
                if not queue_data.empty():
                    data = queue_data.get()
                    connection.send(data)
                    print('Data redirected to: {0}:{1}; data: {2}'.format(host, port, data))

        except BrokenPipeError:
            print('WARNING! Connection is broken to: {0}:{1}'.format(host,port))            

        except KeyboardInterrupt:
            return

        finally:    
            if connection != None:                
                connection.close()

def worker_data_reciver(connection, queue_data):
    """
    Recive data and store to queue
    """
    try:    
        data = b''
        while True:
            data = connection.recv (DATA_BUFFER)                        
            sys.stdout.flush()
            if len(data)==0:
                print('INFO: No data, may be client disconnected...')
                return
            else:
                queue_data.put(data)                
    except KeyboardInterrupt:
        return


def run_server(listen_ip, listen_port, redirect_ip, redirect_port):    
    """    
    1. Create process woker_data_sender for send data from Queue to 'redirect host'
    2. Create process 'worker_data_reciver' for listen port
    """
    queue_data = Queue()

    #start client
    process = Process(target=woker_data_sender,
        args=(queue_data, redirect_ip, redirect_port,))
    process.start()

    #Start listen server    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((listen_ip, listen_port))
    server.listen(CLIENTS_LIMIT)
    print('SUCCESSFULLY! Listen server - started!')    

    try:
        while True:
            conn, dest_addr = server.accept() 

            print('SUCCESSFULLY! Client connected from {0}'.format(dest_addr))
            sys.stdout.flush()

            process = Process(target=worker_data_reciver, 
                args=(conn, queue_data,))

            process.start()
    except KeyboardInterrupt:
        server.close()
    finally:
        server.close()


if __name__=='__main__':
    parser = ArgumentParser(description=
        'The traffic summation tool and redirection to a single host')

    parser.add_argument('-l', action='store', dest='listen_port', 
        type=int, help='Listen port')

    parser.add_argument('-a', action='store', dest='redirect_ip', 
        type=str, help='IP Address of HOST to redirect traffic')

    parser.add_argument('-p', action='store', dest='redirect_port', 
        type=int, help="Port of HOST to redirect traffic")

    args = parser.parse_args()    

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    print('Listen port: {0}'.format(args.listen_port))
    print('Redirect host: {0}:{1}'.format(args.redirect_ip, args.redirect_port))
    print('----------------------------------------')

    listen_ip = ''
    run_server(listen_ip, args.listen_port, args.redirect_ip, args.redirect_port)
