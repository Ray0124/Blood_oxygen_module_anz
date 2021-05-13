from threading import Event,Thread
import time
import random

event = Event()

def Light():
    print('红灯亮了')
    time.sleep(random.randint(1, 2))
    event.set()  # 设置标志位
    print('绿灯亮了')


# def car(i):
#     print('%s 正在等红灯' % i)
#     event.wait()  #等待设置标志位
#     print('%s加油起步' % i)
def car(i):
    print('%s 正在等红灯' % i)
    event.clear()  # 清除标志位
    print('%s 加油起步' % i)

t1 = Thread(target=Light)
t1.start()

for i in range(3):
    t = Thread(target=car, args=(i,))
    t.start()