#多线程
from time import sleep
from threading import Thread

tasks = ['movie1','movie2','movie3','movie4','movie5','movie6','movie7','movie8','movie9','movie10']

def download(movie):
    print(f'开始下载 {movie}')
    sleep(2)
    print(f'下载完成 {movie}')

for task in tasks:
    t = Thread(target=download,args=(task,))
    t.start()

from datetime import datetime
print(datetime.utcnow)

"""GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），
使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以
在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。
 多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大"""

