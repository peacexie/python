
import copy, re, json
from urllib import parse
from flask import request, g
from core import dbop, files, urlpy, req
from pyquery import PyQuery as pyq

def test():
    tmp = files.fulnm('https://i.xxx.com/index.aspx?aa=bb&cc=dd#ee')
    print(tmp[2].replace('/','@')+'!'+tmp[3].replace('&',',')) # @index!aa=bb,cc=dd
    print(tmp)

def imgp(db, act, row):

    ubase = 'http://tianyuwanbyd.fang.com/house/ajaxrequest'
    data = {}

    row = {'url':'http://tianyuwanbyd.fang.com/', 'fid':'2820093400'}
    pcaids = {'904':'效果图', '903':'实景图', '907':'配套图', '900':'户型图', '905':'样板间'}
    data['pcaids'] = pcaids

    for pcaid in pcaids:
        if pcaid=='900': # &count=false&city=东莞
            url = ubase + '/householdlist_get.php?newcode='+row['fid']+'&start=0&limit=24&room=all'
        else:
            url = ubase + '/photolist_get.php?newcode='+row['fid']+'&type='+pcaid+'&nextpage=1'
        html = ritms(url, 0)
        itms = json.loads(html)
        pdic = {}; no = 0
        for itm in itms:
            pid = itm['picID'] if 'picID' in itm else itm['pic_id']
            pdic[pid] = {'fid':pid, 'pcaid':pcaid}
            pdic[pid]['title'] = itm['title'] if 'title' in itm else itm['housetitle']
            pdic[pid]['thumb'] = itm['url'] if 'url' in itm else itm['houseimageurl']
            if 'reference_price' in itm:
                pdic[pid]['price'] = itm['reference_price']+itm['reference_price_type']
                pdic[pid]['area'] = itm['buildingarea']
            #pdic['pid-'+str(no)] = itm; no += 1
        data['p'+pcaid] = pdic


    return data

def datap(db, act, url):
    url = 'http://bgyzygy0573.fang.com/house/2014164218/housedetail.htm'
    url = 'http://zhonghuangongyuanwk.fang.com/house/2014163430/housedetail.htm'
    url = 'http://tianyuwanbyd.fang.com/house/2820093400/housedetail.htm'

    data = {}

    html = ritms(url, 0)
    left = pyq(html).find('.main-left')

    data['detail'] = pyq(left).find('.intro').html()

    equip = pyq(left).find('.sheshi_zb').html()
    equip = equip.replace("<span>","【").replace("</span>","】").replace("'","")
    equip = equip.replace("<li>","").replace("</li>","<br>").replace("</ul>","")
    equip = equip.replace('<li class="jiaotong_color">',"")
    data['equip'] = equip

    dics = {'base':0, 'sale':1, 'xiaoqu':3}
    for ki in dics:
        itms = pyq(left).find('div.main-item').eq(dics[ki]).find('ul').find('li')
        res = {}
        for i in itms:
            key = pyq(i).find('.list-left').text()
            val = pyq(i).find('.list-right').text()
            vt = pyq(i).find('.list-right-text').text()
            vf = pyq(i).find('.list-right-floor').text()
            if not val and (vt or vf):
                val = vt if vt else vf
            if '项目特色' in key:
                continue
            res[key] = val
            if ki=='base' and key=='楼盘地址：':
                break
        data[ki] = res

    temp = {}
    temp['项目特色'] = pyq(left).find('.tag').text()
    zhs = pyq(left).find('div.main-item').eq(1).find('table tr')
    res = ''
    for i in zhs:
        row = pyq(i).find('td').eq(0).text()
        if row in res or row=='预售许可证':
            continue
        res += (" , " if len(res)>0 else "") + row
    temp['预售许可证'] = res
    temp['交通'] = pyq(left).find('.jiaotong_color').text()
    temp['map'] = mapp()
    data['temp'] = temp

    return data


def urlp(db, act, page):

    page = str(page)
    data = {}
    if act=='view':
        return db.get("SELECT * FROM {url} ORDER BY id LIMIT "+page+",5")

    dmkey = '#newhouse_loupai_list li'
    itms = ritms(g.cjcfg['url'].replace('{page}',page), dmkey)
    html = ritms(g.cjcfg['url'].replace('{page}',page), 0)

    rids = r'\'vwn\.showhouseid\'\:\'([\d\,]+)\'\}\)\;'
    aids = re.findall(rids, html, re.S|re.M)[0].split(',')
    #print(aids)

    no = 0
    for i in itms:
        itm = {}
        detail = pyq(i).find('.nlc_details')
        if not detail:
            continue
        tmp = pyq(detail).find('.nlcd_name').find('a')
        title = pyq(tmp).text()
        fid = aids[no]
        itm['url'] = pyq(tmp).attr('href')
        itm['thumb'] = pyq(i).find('img[width]').attr('src').replace('/160x120','')
        itm['tags'] = pyq(i).find('.fangyuan').text()
        itm['price'] = pyq(i).find('.nhouse_price').text()
        itm['address'] = pyq(i).find('.address').text()
        tmp = pyq(i).find('.notice').html()
        if tmp:
            vtmp = re.findall(r'shoucangProcess\(([^\n]+)\)', tmp, re.S|re.M)
            itm['tmp'] = vtmp[0].replace("'",'')
        
        no += 1

        sql = "SELECT * FROM {url} WHERE fid=%s"
        row = db.get(sql, (fid,),1)
        flval = (itm['url'],fid,title,itm['tags'],itm['price'],itm['address'],itm['thumb'])
        #print(row['id'])
        if not row:
            flids = 'url,fid,title,tags,price,address,thumb'
            sql = "INSERT INTO {url} ("+flids+") VALUES (%s,%s,%s,%s,%s,%s,%s) "
            itm['_res'] = 'add';
        else:
            flids = " url=%s,fid=%s,title=%s,tags=%s,price=%s,address=%s,thumb=%s "
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

    dic = [{'type':'area', 'dmkey':'#quyu_name a'}, # 区域
        {'type':'price', 'dmkey':'#sjina_D03_08 a'}] # 价格区间
    
    res = {}
    for dk in dic:

        itms = ritms(g.cjcfg['url'].replace('{page}','1'), dk['dmkey'])
        
        for i in itms:  
            fid = pyq(i).attr('href').replace('/house/s/','').replace('/','')
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


def mapp(id=''):
    id = '2014163328'
    url = 'https://m.fang.com/map/xf/jx/'+id+'/ditu.htm'
    itms = ritms(url, 'input')
    res = {}
    for i in itms:
        key = pyq(i).attr('data-id')
        val = pyq(i).attr('value')
        if key=='searchNow':
            break;
        res[key] = val
    return res['corX'] +','+ res['corY']

def ritms(url, dkey):
    #url = 'http://newhouse.jx.fang.com/house/s/'
    fp = '.' + g.dir['cache'] + '/pages/' + files.fulnm(url)
    ok = files.tmok(fp, 720)
    if ok:
        html = files.get(fp, 'utf-8')
    else:
        html = urlpy.page(url, 'gb2312', {"Accept-Encoding":"gzip"})
        files.put(fp, html)
    if not dkey:
        return html
    doc = pyq(html)
    return doc(dkey)
    #



