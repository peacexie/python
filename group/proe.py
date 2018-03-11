
#作者：Joseph
#链接：https://www.zhihu.com/question/35637215/answer/142317271
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import os
import time
from multiprocessing import Pool
import random

class MyThread(object):

    def long_time_task(self,i):
        print('Run task %s (%s)...' % (i, os.getpid()))
        time.sleep(random.random() * 3)
        print(i)
    
    def parse_thread(self):
        print('Parent process %s.' % os.getpid())
        p = Pool()
        results = []
        for i in range(10):
            results.append(p.apply_async(self.long_time_task,args=(i,)))
        # If trying to get the result, error will be reported here
        for res in results:
            print(res.get())
    
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')
    
def main(): 
    print("start")
    tt=MyThread()
    tt.parse_thread()
    
if __name__=="__main__":
    main()
