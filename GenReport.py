#!/usr/bin/python
#-*-coding:utf-8-*-  
######################################################################################
# Automation Scripts
#
# File: GenLog.py
# Author: flyyou
# Purpose: This script is used to generate report
# Version: 1.0
# Requirements: Python 2.6
# Supported OS: Linux 2.6, Mac OX 10.6 and above
#
#####################################################################################

#Parameter Descriptions:
#--$1: The *.jtl file path
#--$2: The results.html file path
#--$3: The total test times of each API
from xml.dom import minidom
from xml.dom.minidom import parse, parseString, Document
import xml.etree.ElementTree
import os, sys, string, datetime, time, re, codecs, decimal, optparse


def GenWeliaoResult(filePath, genFilePath):
        XMLFileR = open(filePath)
        
        fileR = open(genFilePath, "r")
        s = fileR.read()
        fileR.close()
        fileW = open(genFilePath, "w")

        i = 0
        content = ''
        urlcontent=''
        urlList = ["/common/pushNotifyService/1.0/notifyService/pullAndroidNotify","/common/pushNotifyService/1.0/collectUnreadMessage","/weiliao/message/getNoReplyUserList",
                   "/weiliao/message/sendFriendMessage","/weiliao/message/publicservice/feedbackUserList","/weiliao/message/publicservice/getAllNewMessages",
                   "/weiliao/message/publicservice/getMessages","/weiliao/message/publicservice/sendMessage","/weiliao/message/app/getAllNewMessages",
                   "/weiliao/message/getAllNewMessages","/weiliao/user/getFriendInfo","/weiliao/user/rsyncBrokerInfo","/weiliao/message/changeRemindBrokerSwitchStatus",
                   "/broker/3.0/rest/haopan/brokerPlanReport","/broker/3.0/rest/properties/propInfo","/broker/3.0/rest/haopan/propPlanInfo","/broker/3.0/rest/haopan/unRecommendProp",
                   "/3.0/rest/haopan/propPlanInfo"]
        appname =['','','','','','','','','','','','','','','','','','','','','','','','','',]
        urlcount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
	try:
                while 1:                        
                        lines = XMLFileR.readlines()
                        if not lines:
                                break

                        for line in lines:
                                temp = line.split('	')
                                name = temp[0]
                                #print name
                                
                                if(name.find("api.") >= 0):
                                        #print name                                        
                                        url = temp[1]                                       
                                        countlist = temp[3].split('\n')
                                        count = countlist[0]
                                        for j in range(0,18):
                                                #print urlList[j]
                                                if(url.find(urlList[j]) == 0):
                                                        appname[j] = name
                                                        urlcount[j] = urlcount[j] + int(count)
                                                        #print urlList[j]
                                                        #x = x.replace(urlList[j],'')
                for j in range(0,18):
                        print urlList[j] + ":" + str(urlcount[j])
                        urlcontent = ReplaceContentBlueViolet(appname[j],urlList[j],urlcount[j],urlcontent)
                s = s.replace('<td><font>WeiliaoAPIContent</font></td>', urlcontent)
                #print s
                                        
        finally:
                XMLFileR.close()
                       
                #XMLFileW.write(x)
                #XMLFileW.close()                

                fileW.write(s)
                fileW.close()

def GenResult(filePath, genFilePath):
        XMLFileR = open(filePath)
        
        fileR = open(genFilePath, "r")
        s = fileR.read()
        fileR.close()
        fileW = open(genFilePath, "w")
        
        i = 0
        content = ''
        urlcontent=''
        urlList = ["/common/pushNotifyService/1.0/notifyService/pullAndroidNotify","/common/pushNotifyService/1.0/collectUnreadMessage","/weiliao/message/getNoReplyUserList",
                   "/weiliao/message/sendFriendMessage","/weiliao/message/publicservice/feedbackUserList","/weiliao/message/publicservice/getAllNewMessages",
                   "/weiliao/message/publicservice/getMessages","/weiliao/message/publicservice/sendMessage","/weiliao/message/app/getAllNewMessages",
                   "/weiliao/message/getAllNewMessages","/weiliao/user/getFriendInfo","/weiliao/user/rsyncBrokerInfo","/weiliao/message/changeRemindBrokerSwitchStatus",
                   "/broker/3.0/rest/haopan/brokerPlanReport","/broker/3.0/rest/properties/propInfo","/broker/3.0/rest/haopan/propPlanInfo","/broker/3.0/rest/haopan/unRecommendProp",
                   "/3.0/rest/haopan/propPlanInfo"]
        appname =['','','','','','','','','','','','','','','','','','','','','','','','','',]
        urlcount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
	try:
 
                while 1:
                        lines = XMLFileR.readlines()
                        if not lines:
                                break

                        for line in lines:
                                temp = line.split('	')
                                name = temp[0]
                                #print name
                                
                                if(name.find("api.") >= 0):
                                        #print name                                        
                                        url = temp[1]                                       
                                        countlist = temp[3].split('\n')
                                        count = countlist[0]
                                        if(int(count) > 2000):
                                                content = ReplaceContentGreen(name,url,count,content)

                                        if(int(count) > 500 and int(count) <= 2000):
                                                content = ReplaceContentGray(name,url,count,content)
                                                
                                        if(int(count) > 100 and int(count) <= 500):
                                                content = ReplaceContentRed(name,url,count,content)
                s = s.replace('<td><font>APIContent</font></td>', content)
                #print s
                                
       


                                        
        finally:
                XMLFileR.close()                

                fileW.write(s)
                fileW.close()          
                  
	#except:
                #print "throw exception from GenResult"
                #pass

                
def ReplaceContentBlueViolet(name,url,count,content):
        if(name.find('api.anjuke.com') == 0 ):
               content = content + "<tr><td>"  + name + \
                         "</td><td>" + "安居客" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="BlueViolet">' + str(count) + \
                         "</font>" + \
                         "</td></tr>" 
        if(name.find('api.haozu.com') == 0 ):
               content = content + "<tr><td>"  + name + \
                         "</td><td>" + "好租" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="BlueViolet">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        if(name.find('api.aifang.com') == 0 ):
                content = content + "<tr><td>"  + name + \
                         "</td><td>" + "爱房" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="BlueViolet">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        if(name.find('iapi.jinpu.com') == 0 ):
                content = content + "<tr><td>"  + name + \
                         "</td><td>" + "金铺" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="BlueViolet">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        return content

def ReplaceContentGreen(name,url,count,content):
        
        if(name.find('api.anjuke.com') == 0 ):
               content = content + "<tr><td>"  + name + \
                         "</td><td>" + "安居客" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="green">' + str(count) + \
                         "</font>" + \
                         "</td></tr>" 
        if(name.find('api.haozu.com') == 0 ):
               content = content + "<tr><td>"  + name + \
                         "</td><td>" + "好租" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="green">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        if(name.find('api.aifang.com') == 0 ):
                content = content + "<tr><td>"  + name + \
                         "</td><td>" + "爱房" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="green">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        if(name.find('iapi.jinpu.com') == 0 ):
                content = content + "<tr><td>"  + name + \
                         "</td><td>" + "金铺" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="green">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        return content

def ReplaceContentGray(name,url,count,content):
        
        if(name.find('api.anjuke.com') == 0 ):
               content = content + "<tr><td>"  + name + \
                         "</td><td>" + "安居客" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="gray">' + str(count) + \
                         "</font>" + \
                         "</td></tr>" 
        if(name.find('api.haozu.com') == 0 ):
               content = content + "<tr><td>"  + name + \
                         "</td><td>" + "好租" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="gray">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        if(name.find('api.aifang.com') == 0 ):
                content = content + "<tr><td>"  + name + \
                         "</td><td>" + "爱房" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="gray">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        if(name.find('iapi.jinpu.com') == 0 ):
                content = content + "<tr><td>"  + name + \
                         "</td><td>" + "金铺" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="gray">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        return content

def ReplaceContentRed(name,url,count,content):
        if(name.find('api.anjuke.com') == 0 ):
                content = content + "<tr><td>"  + name + \
                         "</td><td>" + "安居客" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="red">' + str(count) + \
                         "</font>" + \
                         "</td></tr>" 
        if(name.find('api.haozu.com') == 0 ):
                content = content + "<tr><td>"  + name + \
                         "</td><td>" + "好租" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="red">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        if(name.find('api.aifang.com') == 0 ):
                content = content + "<tr><td>"  + name + \
                         "</td><td>" + "爱房" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="red">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        if(name.find('iapi.jinpu.com') == 0 ):
                content = content + "<tr><td>"  + name + \
                         "</td><td>" + "金铺" + \
                         "</td><td>" + url + \
                         "</td><td>"  + '<font color="red">' + str(count) + \
                         "</font>" + \
                         "</td></tr>"
        return content

if __name__ == '__main__':
        reload(sys)
        sys.setdefaultencoding('utf8')
        filePath = sys.argv[1]
        genFilePath = sys.argv[2]
        print "start.."
        GenWeliaoResult(filePath, genFilePath)
        GenResult(filePath, genFilePath)


