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
def autnm(url):
    if len(url)==0:
        url = 'index.htm'
    file = os.path.basename(url) # file.php?mod=ext&key=key
    file = file.replace('?', '---').replace('/', '!').replace('&',',')
    reg = r'\.(jpg|jpeg|gif|png|htm|html)$'
    if not re.findall(reg, file):
        file += '.htm';
    return file

def fulnm(url):
    tmp = parse.urlsplit(url)
    file = tmp[1] +'---'+ tmp[2].replace('/','!')
    if len(tmp[3])>0:
        file += '---'+ tmp[3].replace('&',',')
    if len(file)>160:
        m5 = hashlib.md5(file.encode("latin1")).hexdigest()
        file = file[:60] +'---'+ m5 +'---'+ file[-60:]
    reg = r'\.(jpg|jpeg|gif|png|htm|html)$'
    if not re.findall(reg, file):
        file += '.htm';
    return file
    pass

# 未超时判断
def tmok(fp, tmout=6):
    flag = os.path.exists(fp)
    if not flag:
        return 0
    ft = os.path.getmtime(fp)
    st = time.time()
    return 1 if st-ft<tmout*3600 else 0
