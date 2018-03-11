
#作者：Joseph
#链接：https://www.zhihu.com/question/35637215/answer/142317271
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import os
import time
from multiprocessing import Pool
import random

class MyThread(object):

    def __init__(self, func):
        self.func = func
    
    def long_time_task(self,i):
        print('Run task %s (%s)...' % (i, os.getpid()))
        time.sleep(random.random() * 3)
        print(i)
        return (i, os.getpid())
    
    def parse_thread(self):
        print('Parent process %s.' % os.getpid())
        p = Pool()
        results = []
        for i in range(10):
            results.append(p.apply_async(long_time_task_wrapper,args=(self,i,)))
        
        # Now can get the result
        for res in results:
            print(res.get())
        
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')
    
def long_time_task_wrapper(cls_instance, i):
        return cls_instance.long_time_task(i)
    
def main(): 
    print("start")
    tt=MyThread(long_time_task_wrapper)
    tt.parse_thread()
    
if __name__=="__main__": 
    main()

