'''
Description: 
Author: Phoenix Zhong
Date: 2020-12-07 11:54:43
LastEditTime: 2020-12-07 11:54:44
LastEditors: Phoenix Zhong
FilePath: /python/threading_test.py
'''
import threading

event_obj = threading.Event()

def runthreading(event):
    print("Start...")
    event.wait()
    print("End...")



for n in range(10):
    t = threading.Thread(target=runthreading, args=(event_obj,))
    t.start()

event_obj.clear()
inp = input("True/False?>> ")
if inp == "True":
    event_obj.set()