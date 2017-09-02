import sys

def filSafe4(str,exa=['%']):

    #str = htmlentities($xStr,ENT_QUOTES,"UTF-8"); //ENT_QUOTES:编码双引号和单引号
    #str = str_replace(array('<','>'),array('&lt;','&gt;'),$xStr);
    #$str.replace(['<','>'], ['&lt;','&gt;']);
    return str;


"""

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前字母 :', fruit

    // *** Safe4过滤标题
    static function filSafe4($xStr,$exa=array('%')){
        $def = array('<','>','"',"'","\\"); //开始为前4个,\,%后续加上
        if(!empty($exa)){ 
            foreach($exa as $val) $def[] = $val;
        }
        $xStr = str_replace($def,'',$xStr); 
        return $xStr;
    }

    // *** 文本文件
    static function filText($xStr,$cbr=1){  
        if(is_array($xStr)) {
            foreach($xStr as $k => $v) $xStr[$k] = self::filText($v);
        }else{
            $xStr = htmlentities($xStr,ENT_QUOTES,"UTF-8"); //ENT_QUOTES:编码双引号和单引号
            $xStr = str_replace(array('<','>'),array('&lt;','&gt;'),$xStr);
            if($cbr) $xStr = nl2br($xStr);
        }
        return $xStr;
    }
"""
