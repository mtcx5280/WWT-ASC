# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:23:27 2019

@author: VM-PC-001
"""
def wwtasc(C_Nr=2,C_name='no name',C_value='100',C_timechannel='0',C_unit='N'):
    Nr_channel = C_Nr   # edit the number of channel
    str_line12t = '{:>17.17}'.format(C_name)
    str_line10t = C_value
    str_line11t = C_timechannel
    str_line13t = '{:>17.17}'.format(C_unit)
    str_line12 = ''
    str_line10 = ''
    str_line11 = ''
    str_line13 = ''
    for i in range(Nr_channel):
        str = input('Enter Channel {} information by "Name,Number of value,Time channel,Unit" ->'.format(i+1))
        if len(str) != 0:
            str = str.split(',')
            str_12,str_10,str_11,str_13 = str[0],str[1],str[2],str[3]
        #    str_12 = input('channel {} name: '.format(i+1))
            str_12 = '{:>17.17}'.format(str_12)
        #    str_10 = input('channel {} value number: '.format(i+1))
            str_10 = '{} '.format(str_10)
        #    str_11 = input('channel {} time: '.format(i+1))
            str_11 = '{} '.format(str_11)
        #    str_13 = input('channel {} Unit: '.format(i+1))
            str_13 = '{:>17.17}'.format(str_13)
            str_line12 = str_line12 + str_12
            str_line10 = str_line10 + str_10
            str_line11 = str_line11 + str_11
            str_line13 = str_line13 + str_13
        else:
            str_line12 += str_line12t
            str_line10 += str_line10t+' '
            str_line11 += str_line11t+' '
            str_line13 += str_line13t
    print(str_line12,'\n',str_line10,'\n',str_line11,'\n',str_line13)
    
    import time as t
    wwt=open('my file.asc','w')   #用法: open('文件名','形式'), 其中形式有'w':write;'r':read.
    line_1 = 'WinWertASCIIDaten'    #1. Line: Identification
    line_2 = '19.04.15/XuXiaozhou/test.asc'  # 2. Line: Date, editor, file name
    line_3 = 'a'  #3. Line: Main text 
    line_4 = 'b'
    line_5 = 'c'
    line_6 = 'd'
    line_7 = 1.00000E-003  #7. Line: Sampling rate (in case of displaying using the time, it must always be available) 
    line_8 = 0.00000E000  #8. Line: Starting time (in case of displaying using the time, it must always be available) 
    line_9 = Nr_channel  #9. Line: Number of channels
    line_10 = str_line10  #10. Line: Number of values for each channel
    line_11 = str_line11    #11. Line: X Channel number for each channel
    line_12 = str_line12   
    line_13 = str_line13   
    wwt.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line_1,line_2,line_3,line_4,line_5,line_6,line_7,line_8,line_9,line_10,line_11,line_12,line_13))               #该语句会写入先前定义好的 text
    for i in range(100):
        start = t.perf_counter()
        wait = 0.0001
        t.sleep(wait)
        end = t.perf_counter()
        dev = abs(wait-(end-start))
        P='{:^13f}{:^13f}'.format(i,dev)
        print(P)
        wwt=open('my file.asc','a')   #用法: open('文件名','形式'), 其中形式有'w':write;'r':read.
        wwt.write(P)               #该语句会写入先前定义好的 text
        wwt.write('\n')
    wwt.close() 
    """
        File read and copy!
    """
    t.sleep(0.5)
    print('now i am copying!')
    wwt = open('my file.asc','r')
    a = wwt.readlines()
    wwt.close()
    wwt2 = open('my file2.asc','w')
    wwt2.writelines(a)
    wwt2.close()    
    return
wwtasc()
