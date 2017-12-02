#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This script sends ping for IP address which you choose.
# Please add new IP address to IpList if you want. 
# 
# 
import argparse
import os

# ############
# parameters #
# ############

IpList=[
  ["www.yahoo.co.jp","183.79.135.206"],
  ["www.google.co.jp","74.125.203.94"]]

DEFAULT_TIME_INTERVAL = 1
DEFAULT_ARGUMENT_ENTER = 10000
argument_enter = DEFAULT_ARGUMENT_ENTER

# ###########
# functions #
# ###########

def kill_process():
    exit()

def main(args):
    global argument_enter
    print('This is Host Address List')
    print('==================')
    for i in range(len(IpList)):
        print('{}: {} ({})'.format(i, IpList[i][0], IpList[i][1]))
    print('100: ping for www.google.co.jp')
    print('q: quit')
    print('==================\n')
    print('Please enter number:')
    # argument or not    
    if argument_enter == DEFAULT_ARGUMENT_ENTER:
        enter = input('>>> ')
    else:
        enter = argument_enter
        argument_enter = DEFAULT_ARGUMENT_ENTER
    print()
    print('The command entered is '.format(enter))
    if 'q' == str(enter):
        print('Quit!!!')
        kill_process()
    elif '' == str(enter):
        print('Your did not enter command.')
        
    enter = int(enter)
    if enter <= len(IpList):
        print('Ping for {} ({})'.format(IpList[enter][0],IpList[enter][1]))
        cmd = 'ping -i %d -c 3 %s' % (args.interval, IpList[enter][1])
        print('\n===========\n\n\n')
    elif enter == 100:
        print('Ping for google(173.194.38.24)...')
        #ping www.google.co.jp
        #ping 173.194.38.24
        cmd = 'ping -i %d 74.125.203.94 ' % args.interval
    else:
        print('[Error]You typed wrong number!!!')
        exit
    print(cmd)
    os.system(cmd)


########
# main #
########
# option

if __name__== '__main__':
    parser = argparse.ArgumentParser(description='Ping for any IP adress.')
    parser.add_argument('-i', '--interval', type = int, default = DEFAULT_TIME_INTERVAL, 
                        help = 'Set the time interval between pings (sec, default is 1)')
    parser.add_argument('-n', '--number', type = int, default = DEFAULT_ARGUMENT_ENTER,
                        help = 'Choose the number of IP adress which you want to send pings.')
    args = parser.parse_args()

    # Checking Options...
    if args.number != DEFAULT_ARGUMENT_ENTER:
        argument_enter = args.number
    
    while True:
        main(args)

