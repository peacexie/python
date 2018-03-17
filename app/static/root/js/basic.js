
console.log('微爬(Wepy)');

// 通过id得到web元素
function jeID(id){ 
    return typeof id == 'string' ? document.getElementById(id) : id;
}

// url + _r=1234.5678
function rurl(id){
    var link = jeID(id); if(!link) return;
    var url = link.getAttribute("href");
    var r=Math.random(), p=url.indexOf('?');
    if(p<0){ url += '?' }
    if(url.indexOf('_r=')<0){
        url += '_r='+r;
    }else{
        url = url.substring(0,p) + '_r='+r;
    }
    link.setAttribute('href', url);
}
