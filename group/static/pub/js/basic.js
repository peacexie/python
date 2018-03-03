
// js Config
var _cbase={}; _cbase.run={}; _cbase.sys={}; _cbase.path={}; _cbase.ck={};
_cbase.safe={}; _cbase.safil={}; _cbase.jsrun={};
if(typeof(_pbase)=='undefined'){_pbase={}} 

/*
_cbase.run.rsite = 'http://txmao.txjia.com';
_cbase.run.rmain = 'http://txmao.txjia.com';
_cbase.run.roots = 'http://txmao.txjia.com/root';
_cbase.run.rskin = 'http://txmao.txjia.com/skin';
*/

// urlEncode
function urlEncode(url,ext,percent){
    if(percent){
        url = url.replace('\\%','%25');    
    }
    var a = [ '\\#' , '\\&' ]; 
    var b = [ '%23' , '%26' ]; 
    var i;
    for(i=0; i<a.length;i++){
        url = url.replace(new RegExp(a[i],"g"),b[i]);
    };
    var c = [ '\\+' ,'\\ ' , '\\"' , "\\'" , '\\<' , '\\>' , "\\\r" , "\\\n" , "\\\\" ];
    var d = [ '%2B' ,'+'   , '%22' , '%27' , '%3C' , '%3E' , '%0D'  , '%0A'  , '%5C'  ];
    if(ext){
        for(i=0; i<c.length;i++){
            url = url.replace(new RegExp(c[i],"g"),d[i]);
        };
    } 
    return url;
}

// <b class="qrcode_tip" onMouseOver="qrurl_act(id,1)" onMouseOut="qrurl_act(id,0)">扫码<i class="qrcode_pic"></i></b
function qrurl_set(id,url){ 
    cls = 'qrcode_pic';
    if($('#'+cls+id).html().length>24) return;
    url = url.length>12 ? url : window.location.href;
    url = urlEncode(url);
    img = "<img src='"+_cbase.run.roots+"/plus/ajax/vimg.php?mod=qrShow&data="+url+"' width='180' height='180' />";
    $('#'+cls+id).html('扫描网址到手机<br>'+img); // onload='imgShow(this,180,180)'
}
function qrurl_act(id,type,url){
    if(url) qrurl_set(id,url);
    if(type) $('#qrcode_pic'+id).show();
    else $('#qrcode_pic'+id).hide();
}

function qrcargo_act(id,type,url){
    if(url){
         var src = $('#qrcode_pic'+id).attr('src');
         if(!src){
            if(url.indexOf('?')>=0){ //08tools/yssina/1/root/run/mob.php?cargo.2015-97-dad1
                url = _cbase.run.rsite+url; 
                img = _cbase.run.roots+"/plus/ajax/vimg.php?mod=qrShow&data="+url; 
                $('#qrcode_pic'+id).find('img').attr('src',img);
            }else{//cargo.2015-97-dad1
                var extp = Math.random().toString(36).substr(2); 
                extp = url+','+extp;
                var url = 'actys=getQrcode&qrmod=send&extp='+extp+'&datatype=js&varname=data';
                $.getScript(_cbase.run.roots+'/plus/api/wechat.php?'+url, function(){ 
                    img = data.url; 
                    $('#qrcode_pic'+id).find('img').attr('src',img);
                });    
            }
         }
    } 
    if(type) $('#qrcode_pic'+id).show();
    else $('#qrcode_pic'+id).hide();
}

function mpro_vbig(e){
    var src = $(e).prop('src');
    $('#picBig').html("<img src='"+src+"' width=400 height=300 data-val='"+src+"' onload='imgShow(this,400,300)'>");
}

function qrActs(){
    $('div.nav').on('mouseover','a',function(){
        var href = $(this).prop('href');    
        var mod = $(this).find('i').prop('id').replace('qrcode_pic','');    
        qrurl_act(mod,1,href);
    });
    $('div.nav').on('mouseout','a',function(){
        var mod = $(this).find('i').prop('id').replace('qrcode_pic','');    
        qrurl_act(mod,0);
    });
    $('.qrcode_home').on('mouseover','',function(){
        var href = $(this).attr('_url');
        qrurl_act('home',1,_burl+href);
    });
    $('.qrcode_home').on('mouseout','',function(){
        qrurl_act('home',0);
    });
}
