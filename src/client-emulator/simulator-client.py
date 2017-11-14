#!/usr/bin/env python3
#coding: utf-8

import socket
import time
import argparse
import sys

def run_client(content_type, ip_address, port):
    client = socket.socket()

    try:
        client.connect((ip_address, port))
    except Exception as e:
        print(e)
        exit(1)

    content={
    1:[b'circle\n', b'line\n', b'rectangle\n', b'bar\n', b'ellipse\n', b'point\n'],
    2:[b'One\n', b'two\n', b'three\n', b'four\n', b'six\n', b'seven\n'],
    3:[b'green\n', b'orange\n', b'red\n', b'white\n', b'blue\n', b'grey\n'],
    }

    while 1:
        for item in content[content_type]:
            try:
                client.send(item)
            except Exception as e:
                print(e)
                exit(2)
            time.sleep(1)


if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Traffic flooder')

    parser.add_argument('-c', action='store', dest='content_type', 
        type=int, help='Choice content type 1 to 3 (1 - figure, 2 - digit, 3 - color)')

    parser.add_argument('-a', action='store', dest='ip_address', 
        type=str, help='Remote IP')

    parser.add_argument('-p', action='store', dest='port', 
        type=int, help="Remote port")

    args = parser.parse_args()    

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    run_client(args.content_type, args.ip_address, args.port)

    
