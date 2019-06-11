# files:文件相关

import os, time, hashlib, re
from urllib import parse

def get(fp, cset='utf-8', mode='rb'):
    flag = os.path.exists(fp)
    if not flag:
        return ''
    data = ''
    fh = open(fp, mode)
    data = fh.read()
    fh.close()
    if cset:
        data = data.decode(cset)
    return data

def put(fp, data): 
    with open(fp,'w', encoding='utf-8') as f:
        f.write(data)
    f.close()

# 自动文件名
def autnm(url, full=0):
    if len(url)==0:
        url = 'index.htm'
    file = url if (full or not os.path.basename(url)) else os.path.basename(url)
    file = re.sub("http(s)?://",'',file)
    file = file.replace('/','!').replace('?','---').replace('&',',')
    file = re.sub('[:*"<>|]','`',file)
    if len(file)>160: # /|\?& :*<>
        m5 = hashlib.md5(file.encode("latin1")).hexdigest()
        file = file[:60] +'---'+ m5 +'---'+ file[-60:]
    reg = r'\.(jpg|jpeg|gif|png|htm|html)$'
    if not re.findall(reg, file):
        file += '.htm';
    return file

# 未超时判断
def tmok(fp, tmout=60):
    flag = os.path.exists(fp)
    if not flag:
        return 0
    ft = os.path.getmtime(fp)
    st = time.time()
    return 1 if st-ft<tmout*60 else 0
