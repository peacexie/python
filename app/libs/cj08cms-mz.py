
import copy, re, json, random, time
from core import argv, dbop, files, urlpy
from urllib import parse, request as ureq
from pyquery import PyQuery as pyq

def fixSale(db, act):

    cmin = int(cfg('pagemin'))
    cmax = int(cfg('pagemax'))
    data = {}
    
    for ipg in range(cmin, cmax):
        page = str(ipg);
        dmkey = 'div.houselist'
        url = liurl(page)
        itms = ritms(url, dmkey)
        html = ritms(url, 0)
        for i in itms:
            info = pyq(i).find('.info')
            if not info:
                continue
            h3 = pyq(info).find('h3')
            url = pyq(h3).find('a').attr('href')
            fid = url.split('=')[1];
            tmp = pyq(h3).find('i').attr('class');
            ccid18 = tmp.replace('btn btn-xs dais-','');
            print(fid); print(ccid18);
            db.exe("UPDATE {url} SET tag1='"+ccid18+"' WHERE fid='"+fid+"'")
     
    data['res'] = 'res'
    return data

def img(db, act):
    cbat = cfg('delimit')
    offset = random.randint(5, 15)
    limit = " LIMIT "+str(offset)+","+cbat+" "
    data = {'_end':'-', '_fids':''}
    res = {}

    if act=='view':
        res = db.get("SELECT * FROM {img} ORDER BY id "+limit+"")
    elif act=='test':
        itms = db.get("SELECT * FROM {url} ORDER BY id "+limit+"")
        for row in itms:
            fid = row['fid']
            res[fid] = imgp(db, act, row)
            data['_fids'] += fid + ','
    elif act=='done':
        itms = db.get("SELECT * FROM {url} WHERE f2=0 ORDER BY id LIMIT "+cbat)
        if not itms:
            data['_end'] = 1
        for row in itms:
            fid = row['fid']
            res[fid] = imgp(db, act, row)
            data['_fids'] += fid + ','
    else: # save
        itms = db.get("SELECT * FROM {img} WHERE f1=0 ORDER BY id LIMIT "+cbat)
        if not itms:
            data['_end'] = 1
        for row in itms:
            fid = row['fid']
            res[fid] = imgs(db, act, row)
            #print('1')
            #time.sleep(3)
            #print('2')
            data['_fids'] += fid + ','
    data['res'] = res
    return data

def imgs(db, act, row):
    url = row['thumb']
    file = urlpy.svurl(url, 'pics')
    # 放前面???
    db.exe("UPDATE {img} SET f1=1 WHERE fid='"+str(row['fid'])+"'")
    return file

def imgp(db, act, row):

    baseurl = argv.cfgs['cjcfg']['baseurl']
    ubase = baseurl + '/index.php?/ajax/pageload/aj_model/a%2C{chid}/aj_check/1/aj_pagenum/1/aj_pagesize/180/aj_nodemode/0/aj_thumb/thumb%2C184%2C134/aj_whrfields/pid3%2C%3D%2C{aid}%3Bshi%2C%3D%2C0/callback/'
    data = {}
    pcaids = {'7':'相册图', '11':'户型图'}
    data['pcaids'] = pcaids

    for pcaid in pcaids:
        #if pcaid=='900': # &count=false&city=东莞
        url = ubase.replace('{chid}',pcaid).replace('{aid}',row['fid'])
        html = ritms(url, 0)
        itms = json.loads(html)
        pdic = {}; no = 0
        for itm in itms:
            if type(itm)==str:
                print('Error:'+itm)
                continue
            pid = itm['aid']
            pdic[pid] = {'fid':pid, 'pcaid':pcaid}
            pdic[pid]['title'] = itm['catalog']
            pdic[pid]['thumb'] = itm['thumbOrg']
            if itm['caid']=='11':
                tags = {}
                tags['ccid12'] = itm['ccid12']
                tags['shi'] = itm['shi']
                tags['ting'] = itm['ting']
                tags['wei'] = itm['wei']
                tags['chu'] = itm['chu']
                pdic[pid]['tags'] = tags
                pdic[pid]['price'] = itm['dj']
                pdic[pid]['area'] = itm['mj']
            else:
                pdic[pid]['tags'] = {}
                pdic[pid]['price'] = '0'
                pdic[pid]['area'] = '0'
            # save
            sql = "SELECT * FROM {img} WHERE fid=%s"
            urow = db.get(sql, (pid,),1) #str.strip([chars])
            flval = (pid, row['fid'], pdic[pid]['title'], pcaid, pdic[pid]['price'], 
                pdic[pid]['area'], pdic[pid]['thumb'], jdump(pdic[pid]['tags']))
            if not urow:
                flids = 'fid,pid,title,pcaid,price,area,thumb,tags'
                sql = "INSERT INTO {img} ("+flids+") VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
                pdic[pid]['_res'] = 'add';
            else:
                flids = " fid=%s,pid=%s,title=%s,pcaid=%s,price=%s,area=%s,thumb=%s,tags=%s "
                whr = " WHERE fid='"+str(urow['fid'])+"' "
                sql = "UPDATE {img} SET" + flids + whr
                pdic[pid]['_res'] = 'upd';
            #data['_res'] = 'add' if not urow else 'upd'
            if act=='done':
                db.exe(sql, flval)
        # for-return
        data['p'+pcaid] = pdic
    if act=='done':
        db.exe("UPDATE {url} SET f2=1 WHERE id='"+str(row['id'])+"'")
    return data

def data(db, act):

    cbat = cfg('delimit')
    offset = random.randint(5, 15)
    limit = " LIMIT "+str(offset)+","+cbat+" "
    data = {'_end':'-', '_fids':''}
    res = {}

    if act=='view':
        res = db.get("SELECT * FROM {data} ORDER BY id "+limit+"")
    elif act=='done':
        itms = db.get("SELECT * FROM {url} WHERE f1=0 ORDER BY id LIMIT "+cbat)
        if not itms:
            data['_end'] = 1
        for row in itms:
            fid = row['fid']
            res[fid] = datap(db, act, row)
            data['_fids'] += fid + ','
    else: # test
        itms = db.get("SELECT * FROM {url} ORDER BY id "+limit+"")
        for row in itms:
            fid = row['fid']
            res[fid] = datap(db, act, row)
            data['_fids'] += fid + ','
    data['res'] = res
    return data

def datap(db, act, row):

    baseurl = argv.cfgs['cjcfg']['baseurl']
    data = {}
    fid = row['fid']
    rid = row['id']
    url = baseurl + '/archive.php?aid='+fid+'&addno=12'
    html = ritms(url, 0)

    data['detail'] = pyq(html).find('.xmjj').find('.lp-tabcon').html().replace(baseurl,'')
    data['equip'] = pyq(html).find('.xmpt').find('.lp-tabcon').html().replace(baseurl,'').replace('href','x')
    binfos = pyq(html).find('.lp-detail')

    dts = pyq(binfos).find('dt')
    dds = pyq(binfos).find('dd')
    base = {}
    no = 0
    for i in dts:
        key = pyq(i).text()
        val = pyq(binfos).find('dd').eq(no).text()
        key = key.replace(' ','').replace('&nbsp;','').replace('：','').replace('　','');
        val = val.replace(' ','').replace('&nbsp;','').replace('：','').replace('　','');
        if key: # && val
            base[key] = val
        no = no + 1
    data['base'] = base
    '''
    '''
    data['sale'] = ''
    data['xiaoqu'] = ''
    data['temp'] = ''
    # save
    sql = "SELECT * FROM {data} WHERE id=%s"
    urow = db.get(sql, (rid,),1) #str.strip([chars])
    flids = 'id,detail,equip,info_base,info_sale,info_xiaoqu,info_temp'
    flval = (rid, data['detail'].strip(), data['equip'].strip(), jdump(data['base']), 
        jdump(data['sale']), jdump(data['xiaoqu']), jdump(data['temp']))
    sql = "REPLACE INTO {data} ("+flids+") VALUES (%s,%s,%s,%s,%s,%s,%s) "
    data['_res'] = 'add' if not urow else 'upd'
    if act=='done':
        db.exe(sql, flval)
        db.exe("UPDATE {url} SET f1=1 WHERE id='"+str(rid)+"'")
    return data

def url(db, act):

    cmin = int(cfg('pagemin'))
    cmax = int(cfg('pagemax'))
    cbat = int(cfg('delimit'))
    #proc = int(cfg('proc'))
    data = {}
    data = {'_end':'-', '_pages':''}
    act = argv.get('act', 'view')
    if act=='done':
        page = int(argv.get('page', '1'))
        start = max(cmin, page)
        end = start + cbat
        if end>cmax+1:
            end = cmax+1
        for i in range(start, end):
            res = urlp(db, act, i)
            data['_pages'] += str(i) + ','
            data['_pend'] = i+1
        if i>=cmax:
            data['_end'] = 1
    else:
        page = random.randint(cmin, cmax)
        res = urlp(db, act, page)
        data['_pages'] = page
    # 
    data['res'] = res
    return data

def urlp(db, act, page):

    page = str(page);
    data = {}
    if act=='view':
        return db.get("SELECT * FROM {url} ORDER BY id LIMIT "+page+",5")

    dmkey = 'div.houselist'
    url = liurl(page)
    itms = ritms(url, dmkey)
    html = ritms(url, 0)

    no = 0
    for i in itms:
        itm = {}
        info = pyq(i).find('.info')
        if not info:
            continue
        tmp = pyq(info).find('h3').find('a')
        title = pyq(tmp).text()
        itm['url'] = pyq(tmp).attr('href')
        fid = itm['url'].split('=')[1];
        itm['thumb'] = pyq(i).find('img[width]').attr('data-original').replace('_160_120','')
        itm['tags'] = pyq(i).find('.tags').html().replace('</span><span>',',').replace('</span>','').replace('<span>','')
        itm['price'] = pyq(i).find('.dj').text()
        itm['address'] = pyq(i).find('p').eq(0).text().replace('查看地图','').replace(' ','').replace('','')
        mapurl = pyq(i).find('p').eq(0).find('.icon3').attr('href')
        if mapurl:
            itm['local'] = mapurl.split('#')[1].split('&zoom')[0].replace('lat=','').replace('&lng=',',');
        itm['tmp'] = '';
        #print(fid); lat=23.7609534251&lng=114.671497117
        no += 1
        # save
        sql = "SELECT * FROM {url} WHERE fid=%s"
        row = db.get(sql, (fid,),1)
        flval = (itm['url'],fid,title,itm['tags'],itm['price'],itm['address'],itm['thumb'],itm['local'])
        #print(row['id'])
        if not row:
            flids = 'url,fid,title,tags,price,address,thumb,local'
            sql = "INSERT INTO {url} ("+flids+") VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            itm['_res'] = 'add';
        else:
            flids = " url=%s,fid=%s,title=%s,tags=%s,price=%s,address=%s,thumb=%s,local=%s "
            whr = " WHERE id='"+str(row['id'])+"' "
            sql = "UPDATE {url} SET" + flids + whr
            itm['_res'] = 'upd';
        if act=='done':
            db.exe(sql, flval)
        data[fid+':'+title] = itm
        
    return data

def area(db, act):

    if act=='view':
        return db.get("SELECT * FROM {attr} ORDER BY id")

    dic = [{'type':'area', 'dmkey':'.list-1 a'}, # 区域
        {'type':'price', 'dmkey':'.list-17 a'}] # 价格区间
    
    res = {}
    for dk in dic:

        itms = ritms(liurl(), dk['dmkey'])
        
        for i in itms: # baseurl
            fid = pyq(i).attr('href').replace('/index.php?caid=2&','').replace('&addno=1','')
            fid = fid.replace(argv.cfgs['cjcfg']['baseurl'],'')
            title = pyq(i).text()
            sql = "SELECT * FROM {attr} WHERE title=%s AND type=%s"
            row = db.get(sql, (title,dk['type']),1)
            if not row:
                if act=='done':
                    sql = "INSERT INTO {attr} (title,fid,type) VALUES (%s,%s,%s) "
                    db.exe(sql, (title,fid,dk['type']))
                res[dk['type']+':'+title] = 'add';
            else:
                res[dk['type']+':'+title] = 'skip';

    return res
    #

def ritms(url, dkey):
    #url = 'http://newhouse.jx.fang.com/house/s/'
    fp = argv.cfgs['dir']['cache'] + '/pages/' + files.autnm(url, 1)
    ok = files.tmok(fp, 720)
    if ok:
        html = files.get(fp, 'utf-8')
    else:
        html = urlpy.page(url)
        files.put(fp, html)
    if not dkey:
        return html
    doc = pyq(html)
    return doc(dkey)
    #

def jdump(dic):
    return json.dumps(dic, ensure_ascii=False)

def cfg(key=None):
    cjcfg = argv.cfgs['cjcfg']; 
    return cjcfg[key] if key in cjcfg.keys() else None

def liurl(page=1):
    site = cfg('site')
    url = 'http://www.kjfcw.com/index.php?caid=2&addno=1&page={page}'
    return url.replace('{site}',site).replace('{page}',str(page))
