-- Adminer 4.6.2 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `cj08_attr_99`;
CREATE TABLE `cj08_attr_99` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `fid` varchar(24) NOT NULL DEFAULT '',
  `nid` varchar(24) NOT NULL DEFAULT '',
  `title` varchar(48) CHARACTER SET gbk NOT NULL DEFAULT '',
  `type` varchar(24) NOT NULL DEFAULT 'area',
  `_site` varchar(24) NOT NULL DEFAULT '(def)',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `cj08_data_99`;
CREATE TABLE `cj08_data_99` (
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


DROP TABLE IF EXISTS `cj08_img_99`;
CREATE TABLE `cj08_img_99` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `fid` varchar(24) NOT NULL DEFAULT '',
  `pid` varchar(24) NOT NULL DEFAULT '',
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


DROP TABLE IF EXISTS `cj08_url_99`;
CREATE TABLE `cj08_url_99` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `fid` varchar(24) NOT NULL DEFAULT '',
  `nid` varchar(24) NOT NULL DEFAULT '',
  `title` varchar(96) NOT NULL DEFAULT '',
  `f1` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `f2` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `url` varchar(255) NOT NULL DEFAULT '',
  `tag1` varchar(255) NOT NULL DEFAULT '',
  `tag2` varchar(255) NOT NULL,
  `tags` varchar(255) NOT NULL DEFAULT '',
  `price` varchar(255) NOT NULL DEFAULT '',
  `address` varchar(255) NOT NULL DEFAULT '',
  `nuni` int(11) NOT NULL DEFAULT '0',
  `nunf` float NOT NULL DEFAULT '0',
  `map` varchar(255) NOT NULL DEFAULT '',
  `thumb` varchar(255) NOT NULL DEFAULT '',
  `local` varchar(255) NOT NULL DEFAULT '',
  `_site` varchar(24) NOT NULL DEFAULT '(def)',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


-- 2018-07-06 04:17:44
