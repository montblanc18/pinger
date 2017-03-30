#!/usr/bin/env ruby
# -*- coding: utf-8 -*-
# This script sends ping for IP address which you choose.
# Please add new IP address to IpList if you want. 
#
require "optparse"

##############
# parameters #
##############

IpList=[
	["www.yahoo.co.jp","183.79.135.206"],
	["www.google.co.jp","74.125.203.94"]]

$time_interval=1
DEFAULT_ARGUMENT_ENTER = 10000
$argument_enter=DEFAULT_ARGUMENT_ENTER

#############
# functions #
#############

# Ctrl + C trap                                                                                        
Signal.trap(:INT){
  puts "SIGINT"
  exit(0)
}

def KillProcess()
    exit
end

def MainFunction()
	print "This is Host Address List.\n"
	print "==================\n"
	for i in 0..IpList.length-1
		print i,": ",IpList[i][0],"(",IpList[i][1],")\n"
    end
    print "100: ping for www.google.co.jp\n"
	print "q: quit\n"
	print "==================\n"	
	print "Please enter number:"
    # argument or not 
    if $argument_enter == DEFAULT_ARGUMENT_ENTER then
        enter=gets.chomp
    else
        enter = $argument_enter
        $argument_enter = DEFAULT_ARGUMENT_ENTER
    end
	print "\n"
	print "The command entered is ",enter,"\n"
	if "q" == enter.to_s then
		print "Quit!!!\n"
		KillProcess()
	end
    enter = enter.to_i
	if enter <= IpList.length then
		print "Ping for ",IpList[enter][0],"(",IpList[enter][1],")\n"
		cmd=sprintf("ping -i %d -c 3 %s",$time_interval,IpList[enter][1])
        print "\n===========\n\n\n"
    elsif enter == 100 then
        print "Ping for google(173.194.38.24)...\n"
        #ping www.google.co.jp
        #ping 173.194.38.24
        cmd=sprintf("ping -i %d 74.125.203.94",$time_interval)
    else
        print "[Error]You typed wrong number!!!"
        exit
    end
    print cmd,"\n"
    system(cmd)
end

########
# main #
########
# option
opts={}

if __FILE__== $0 then
    ARGV.options do |o|
      o.on("-i X","--interval","Set time interval between pings (sec, default is 1)"){|x|
          opts[:time_inteval]=x
            $time_interval = x.to_i
            print "You set the time interval between pings for ",x," sec.\n\n"
        }
        o.on("-n X","--number X","Choose the number which IP you want to ping as arguments."){|x|
          opts[:number] = x
            $argument_enter = x
        }
        o.parse!
    end
    
    while true do
        MainFunction()
    end
end
