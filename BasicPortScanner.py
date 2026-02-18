#! /usr/bin/python3

import sys
import socket

# If user executed file with no arguments
if len(sys.argv) == 1:
    print(f"Usage : {sys.argv[0]} IP Start-port(optional) End-Port(optional)",file=sys.stderr);
    exit(1);

IP = sys.argv[1]
Starting_port = 1 ;
Ending_port = 65535 ;

# If Starting & Ending port supplied by User .
if len(sys.argv) >= 3 :
    Starting_port = int(sys.argv[2]);
    if len(sys.argv) >= 4 :
        Ending_port = int(sys.argv[3]);

def port_status_checker(port:int) -> bool: 
    try:   
        Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # Default IPv4 & TCP connection
        Connection.settimeout(1);
        Connection.connect((IP, port));
        Connection.close()
        return True;
    except (ConnectionRefusedError , socket.timeout) :
        return False;

for port in range(Starting_port,Ending_port + 1):
    response = port_status_checker(port);
    if response :
        print (f"[+] Open Port Found -> {port}");



