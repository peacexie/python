-- Adminer 4.6.2 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `chatroom_ys`;
CREATE TABLE `chatroom_ys` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(24) NOT NULL DEFAULT '',
  `ufrom` varchar(255) NOT NULL DEFAULT '',
  `uto` varchar(24) NOT NULL DEFAULT '',
  `msgs` varchar(255) NOT NULL DEFAULT '',
  `show` tinyint(4) NOT NULL DEFAULT '1',
  `aip` varchar(255) NOT NULL DEFAULT '',
  `atime` int(11) NOT NULL DEFAULT '0',
  `auser` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `cj_attr_xx`;
CREATE TABLE `cj_attr_xx` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `fid` varchar(24) NOT NULL DEFAULT '',
  `nid` varchar(24) NOT NULL DEFAULT '',
  `title` varchar(48) CHARACTER SET gbk NOT NULL DEFAULT '',
  `type` varchar(24) NOT NULL DEFAULT 'area',
  `_site` varchar(24) NOT NULL DEFAULT '(def)',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `cj_data_xx`;
CREATE TABLE `cj_data_xx` (
  `id` mediumint(8) unsigned NOT NULL,
  `detail` text NOT NULL,
  `equip` text NOT NULL,
  `price` varchar(255) NOT NULL DEFAULT '',
  `info_base` text NOT NULL,
  `info_sale` text NOT NULL,
  `info_xiaoqu` text NOT NULL,
  `info_temp` text NOT NULL,
  `_site` varchar(24) NOT NULL DEFAULT '(def)',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `cj_img_xx`;
CREATE TABLE `cj_img_xx` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `fid` varchar(24) NOT NULL DEFAULT '',
  `nid` varchar(24) NOT NULL DEFAULT '',
  `title` varchar(48) NOT NULL DEFAULT '',
  `f1` tinyint(4) NOT NULL DEFAULT '0',
  `f2` tinyint(4) NOT NULL DEFAULT '0',
  `pcaid` varchar(24) NOT NULL DEFAULT '',
  `price` varchar(24) NOT NULL DEFAULT '',
  `area` varchar(24) NOT NULL DEFAULT '',
  `tags` varchar(255) NOT NULL DEFAULT '',
  `thumb` varchar(255) NOT NULL DEFAULT '',
  `local` varchar(255) NOT NULL DEFAULT '',
  `_site` varchar(24) NOT NULL DEFAULT '(def)',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `cj_url_xx`;
CREATE TABLE `cj_url_xx` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `fid` varchar(24) NOT NULL DEFAULT '',
  `nid` varchar(24) NOT NULL DEFAULT '',
  `title` varchar(96) NOT NULL DEFAULT '',
  `f1` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `f2` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `url` varchar(255) NOT NULL DEFAULT '',
  `tags` varchar(255) NOT NULL DEFAULT '',
  `price` varchar(255) NOT NULL DEFAULT '',
  `address` varchar(255) NOT NULL DEFAULT '',
  `nuni` int(11) NOT NULL DEFAULT '0',
  `nunf` float NOT NULL DEFAULT '0',
  `thumb` varchar(255) NOT NULL DEFAULT '',
  `local` varchar(255) NOT NULL DEFAULT '',
  `_site` varchar(24) NOT NULL DEFAULT '(def)',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `coms_nrem_ys`;
CREATE TABLE `coms_nrem_ys` (
  `cid` varchar(24) NOT NULL,
  `cno` int(11) NOT NULL DEFAULT '0',
  `title` varchar(255) NOT NULL,
  `detail` text NOT NULL,
  `mname` varchar(24) NOT NULL,
  `mtel` varchar(24) NOT NULL,
  `show` tinyint(4) NOT NULL DEFAULT '0',
  `pid` varchar(24) NOT NULL,
  `aip` varchar(255) NOT NULL DEFAULT '',
  `atime` int(11) NOT NULL DEFAULT '0',
  `auser` varchar(24) NOT NULL DEFAULT '',
  PRIMARY KEY (`cid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `docs_news_ys`;
CREATE TABLE `docs_news_ys` (
  `did` varchar(24) NOT NULL,
  `dno` int(11) NOT NULL DEFAULT '0',
  `catid` varchar(255) NOT NULL,
  `hinfo` varchar(12) DEFAULT '',
  `title` varchar(255) NOT NULL,
  `show` tinyint(4) NOT NULL DEFAULT '1',
  `click` int(11) NOT NULL DEFAULT '0',
  `aip` varchar(255) NOT NULL DEFAULT '',
  `atime` int(11) NOT NULL DEFAULT '0',
  `auser` varchar(24) NOT NULL DEFAULT '',
  PRIMARY KEY (`did`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `users_person_ys`;
CREATE TABLE `users_person_ys` (
  `uid` varchar(24) NOT NULL DEFAULT '',
  `uname` varchar(24) NOT NULL,
  `mname` varchar(96) NOT NULL,
  `grade` varchar(12) NOT NULL,
  `mfrom` varchar(12) NOT NULL DEFAULT 'c0769',
  `mtel` varchar(24) NOT NULL DEFAULT '',
  `memail` varchar(120) NOT NULL DEFAULT '',
  `show` tinyint(4) NOT NULL DEFAULT '0',
  `click` int(11) NOT NULL DEFAULT '0',
  `aip` varchar(255) NOT NULL DEFAULT '',
  `atime` int(11) NOT NULL DEFAULT '0',
  `auser` varchar(24) NOT NULL DEFAULT '',
  PRIMARY KEY (`uname`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


-- 2018-03-10 12:46:36