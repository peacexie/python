-- Adminer 4.7.1 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `cms_crawl_data`;
CREATE TABLE `cms_crawl_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(24) NOT NULL DEFAULT '' COMMENT '城市',
  `ruleid` int(11) NOT NULL DEFAULT '0' COMMENT '采集规则ID',
  `toid` int(11) NOT NULL DEFAULT '0' COMMENT '入库ID',
  `flag` int(11) NOT NULL DEFAULT '0' COMMENT '0-默认,1-网址,2-内容,3-入库,6-过滤,7-删除',
  `frem` varchar(24) NOT NULL DEFAULT '' COMMENT '过滤编码(no-detail,skip-title)',
  `ctime` varchar(24) NOT NULL DEFAULT '' COMMENT '采集时间:mm-dd hh:ii',
  `title` varchar(255) NOT NULL DEFAULT '',
  `url` varchar(255) NOT NULL DEFAULT '',
  `dpub` varchar(24) NOT NULL DEFAULT '' COMMENT '原始发布时间:yyyy-mm-dd',
  `dfrom` varchar(24) NOT NULL DEFAULT '' COMMENT '原始来源',
  `detail` mediumtext NOT NULL,
  `catid` varchar(255) NOT NULL DEFAULT '' COMMENT '默认栏目',
  `sfrom` varchar(255) NOT NULL DEFAULT '' COMMENT '默认来源',
  `suser` varchar(255) NOT NULL DEFAULT '' COMMENT '默认作者',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `cms_crawl_rule`;
CREATE TABLE `cms_crawl_rule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(12) NOT NULL DEFAULT '' COMMENT '城市',
  `name` varchar(24) NOT NULL DEFAULT '' COMMENT '任务名称',
  `url` varchar(255) NOT NULL DEFAULT '' COMMENT '采集地址',
  `slist` varchar(48) NOT NULL DEFAULT '' COMMENT '列表-选择器',
  `surl` varchar(48) NOT NULL DEFAULT '' COMMENT '网址-选择器',
  `stitle` varchar(48) NOT NULL DEFAULT '' COMMENT '标题-选择器',
  `detail` varchar(48) NOT NULL DEFAULT '' COMMENT '详情-选择器',
  `dpub` varchar(48) NOT NULL DEFAULT '' COMMENT '发布时间-选择器',
  `dfrom` varchar(48) NOT NULL DEFAULT '' COMMENT '来源-选择器',
  `catid` varchar(12) NOT NULL DEFAULT '' COMMENT '默认保存-栏目',
  `sfrom` varchar(48) NOT NULL DEFAULT '' COMMENT '默认保存-来源',
  `suser` varchar(48) NOT NULL DEFAULT '' COMMENT '默认保存-作者',
  `field` varchar(12) NOT NULL DEFAULT '' COMMENT '过滤-字段(网址/标题/来源)',
  `fop` varchar(12) NOT NULL DEFAULT '' COMMENT '过滤-操作(只需要/排除)',
  `fval` varchar(24) NOT NULL DEFAULT '' COMMENT '过滤-值(A特征,B特征)',
  `cfgs` text NOT NULL COMMENT '扩展配置',
  `status` tinyint(4) NOT NULL DEFAULT '1',
  `debug` tinyint(4) NOT NULL DEFAULT '1',
  `agent` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO `cms_crawl_rule` (`id`, `city`, `name`, `url`, `slist`, `surl`, `stitle`, `detail`, `dpub`, `dfrom`, `catid`, `sfrom`, `suser`, `field`, `fop`, `fval`, `cfgs`, `status`, `debug`, `agent`) VALUES
(1024,	'dg',	'(demo)dg市政府-政务公告',	'http://www.dg.gov.cn/cndg/notice/news.shtml',	'.lbkj li',	'a',	'a',	'#zoomcon,.xq',	'PUBLISHTIME',	'#ly',	'1014',	'东莞政府门户网站',	'房掌柜整理',	'dfrom',	'inc',	'东莞市人民政府办公室',	'tab_repd==阳光网=房掌柜@@<UCAPCONTENT>@@</UCAPCONTENT>',	1,	1,	0),
(1025,	'dg',	'(demo)dg发改局-通知公告',	'http://dgdp.dg.gov.cn/007330029/0801/list2.shtml',	'.list-right_title',	'a',	'a',	'.cen',	'PUBLISHTIME:eq(1)',	'PUBLISHTIME:eq(2)',	'1014',	'a默认来源',	'b默认作者',	'dfrom',	'',	'东莞政府门户网站',	'tab_repd==阳光网=房掌柜@@<UCAPCONTENT>@@</UCAPCONTENT>',	1,	0,	0),
(1033,	'dg',	'(demo)dg建设局-通知公告(?)',	'http://zjj.dg.gov.cn/business/htmlfiles/dgjsj/ptzgg/list.htm',	'#DocumentsDataSrc12 INFO',	'InfoURL',	'Title',	'#zoom',	'',	'',	'1009',	'',	'',	'',	'',	'das,dsad',	'pre_url==http://zjj.dg.gov.cn/publicfiles/business/htmlfiles/\r\npre_list==<xml id=\"DocumentsDataSrc12\">(*)</xml>',	0,	1,	0),
(1036,	'dg',	'(demo)dg公共资源-通知公告',	'http://ggzy.dg.gov.cn/ggzy/website/WebPagesManagement/GovNews/list?fcGovtype=Notice&noticeType=1&KindIndex=0&noticeType=1&KindIndex=0',	'#old_data tr',	'a',	'a',	'.content',	'.date:last',	'',	'1014',	'',	'房掌柜整理',	'dfrom',	'',	'',	'tab_rept==发布日期：',	1,	0,	0),
(1037,	'dg',	'(demo)dg自然资源局-通知公告',	'http://land.dg.gov.cn/007330205/0801/gtjList.shtml',	'.list-right_title',	'a',	'a',	'UCAPCONTENT',	'PUBLISHTIME:eq(1)',	'PUBLISHTIME:eq(0)',	'1009',	'',	'',	'',	'',	'',	'tab_repd==阳光网=房掌柜@@<UCAPCONTENT>@@</UCAPCONTENT>',	1,	0,	0),
(1064,	'tgz',	'测试2',	'/admin/jumpLogin',	'list',	'a',	'',	'detail',	'',	'',	'1009',	'',	'',	'',	'',	'',	'',	0,	0,	0),
(1066,	'test',	'fzgtest',	'http://dg.fzg360.com/news/lists/catid/1009.html',	'.box_news',	'h3 a',	'.newscon h1',	'.detailcon',	'.author span:eq(1)',	'.author span:eq(2) em',	'1009',	'',	'',	'',	'',	'',	'',	0,	0,	0);

-- 2019-06-06 09:53:08
