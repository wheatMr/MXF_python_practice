# -*- coding: UTF-8 -*-
# Time : 2018/2/5 10:54
# Author : liang
from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)...' %(name, os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    #利用multiprocessing模块中Process类定义命名一个子进程
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    #start()方法启动，创建进程
    p.start()
    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('Childe process end.')


