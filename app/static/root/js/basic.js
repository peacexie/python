
if(typeof window.console !== "undefined") {
    console.log('微爬(Wepy)');
}

// 通过id得到web元素
function jeID(id){ 
    return typeof id == 'string' ? document.getElementById(id) : id;
}

function setDev(id){
    var o = jeID(id)
    o.value = o.getAttribute('val');
}
