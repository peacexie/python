
#import os, sys, platform
#import configparser

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app, request, g):
        self.app = app
        self.request = request
        self.g = g
        self.data = {}


    # 方法格式: {xxx}Act
    # xxx优先顺序 : mkvs.key > mkvs.type > '_def'

    def _detailAct(self):
        
        print('dir(self) ------------------- ')
        res = {}
        return res

    def _defAct(self):
        res = {'_defAct_msg':'None Ctrl-Data'}
        return res 

        #{'type': 'index', 'mod': 'home', 'key': 'typid'



'''

class topicCtrl{
    
    public $ucfg = array();
    public $vars = array();

    //function __destory(){  }
    function __construct($ucfg=array(),$vars=array()){ 
        $this->ucfg = $ucfg;
        $this->vars = $vars;
    }

    // _detailAct
    function _detailAct(){
        global $_cbase;
        $m = $this->ucfg['mod'];
        $k = $this->ucfg['key'];
        $v = $this->ucfg['view'];
        if(empty($this->vars['tplname'])){
            $tpl = $this->ucfg['tplname'];
        }else{
            $dir = "/{$_cbase['tpl']['tpl_dir']}/u_topic";
            $tpl = $this->vars['tplname'];
            if($v){
                if(file_exists(DIR_SKIN."$dir/$tpl~$v.htm")){
                    $tpl = "$tpl~$v";
                }else{
                    $tpl = "$tpl~detail";
                }
            } // ?topic.2015-9c-p481.vtechs/7awse21
            $tpl = 'u_topic/'.$tpl; 
        } //echo "(($tpl))";  
        $re['newtpl'] = $tpl; // 模板
        return $re;
    }

    // _defAct
    function xxx_defAct(){
        $re['newtpl'] = 'u_topic/_index/stype'; // 模板
        return $re;
    }
    
}

'''
