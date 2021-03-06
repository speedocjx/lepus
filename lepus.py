#!/bin/env python
#coding:utf-8
import os
import sys
import string
import time
import datetime
import MySQLdb
import logging
import logging.config
logging.config.fileConfig("etc/logger.ini")
logger = logging.getLogger("lepus")
path='./include'
sys.path.insert(0,path)
import functions as func
from multiprocessing import Process;
  

def job_run(script_name,times):
    while True:
        os.system("python "+script_name+".py")
        time.sleep(int(times))


def main():
    logger.info("lepus controller start.")
    monitor = func.get_option('monitor')
    monitor_mysql = func.get_option('monitor_mysql')
    monitor_mongodb = func.get_option('monitor_mongodb')
    monitor_oracle = func.get_option('monitor_oracle')
    monitor_redis = func.get_option('monitor_redis')
    monitor_sqlserver = func.get_option('monitor_sqlserver')
    monitor_os = func.get_option('monitor_os')
    monitor_memcache = func.get_option('monitor_memcache')
    alarm = func.get_option('alarm')
    frequency_monitor = func.get_option('frequency_monitor')
    frequency_monitor_alarm = int(frequency_monitor)+10

    joblist = []
    if monitor=="1":
        if monitor_mysql=="1":
            '''job = Process(target = job_run, args = ('check_mysql',frequency_monitor))'''
            job = Process(target = job_run, args = ('check_mysql',10))
            joblist.append(job)
            job.start()
        '''
        time.sleep(3)
        if monitor_oracle=="1":
            job = Process(target = job_run, args = ('check_oracle',frequency_monitor))
            joblist.append(job)
            job.start()
        '''
        time.sleep(3)
        if monitor_mongodb=="1":
            job = Process(target = job_run, args = ('check_mongodb',frequency_monitor))
            joblist.append(job)
            job.start()

        time.sleep(3)
        if monitor_redis=="1":
            job = Process(target = job_run, args = ('check_redis',frequency_monitor))
            joblist.append(job)
            job.start()

        time.sleep(3)
        if monitor_memcache=="1":
            job = Process(target = job_run, args = ('check_memcache',frequency_monitor))
            joblist.append(job)
            job.start()

        time.sleep(3)
        if monitor_os=="1":
            job = Process(target = job_run, args = ('check_os',frequency_monitor))
            joblist.append(job)
            job.start()

        time.sleep(3)
        if monitor_sqlserver=="1":
            #job = Process(target = job_run, args = ('check_sqlserver',frequency_monitor))
            job = Process(target = job_run, args = ('check_sqlserver',10))
            joblist.append(job)
            job.start()

        time.sleep(3)
        if alarm=="1":
            '''job = Process(target = job_run, args = ('alarm',frequency_monitor_alarm))'''
            job = Process(target = job_run, args = ('alarm',10))
            joblist.append(job)
            job.start()    

        for job in joblist:
            job.join();

    logger.info("lepus controller finished.")
    

  
if __name__ == '__main__':  
    main()
