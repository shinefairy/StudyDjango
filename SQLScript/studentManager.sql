/*
 Navicat MySQL Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : localhost
 Source Database       : studentManager

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : utf-8

 Date: 10/24/2018 20:00:02 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `class`
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `class`
-- ----------------------------
BEGIN;
INSERT INTO `class` VALUES ('2', '全栈2期'), ('5', '全栈6期'), ('6', '全栈6期'), ('7', '全栈7期'), ('8', '全栈10期');
COMMIT;

-- ----------------------------
--  Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `c` (`cid`),
  CONSTRAINT `c` FOREIGN KEY (`cid`) REFERENCES `class` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `teacher`
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `teacher`
-- ----------------------------
BEGIN;
INSERT INTO `teacher` VALUES ('1', '林海峰'), ('2', '林志平'), ('3', '林青霞');
COMMIT;

-- ----------------------------
--  Table structure for `teacher2class`
-- ----------------------------
DROP TABLE IF EXISTS `teacher2class`;
CREATE TABLE `teacher2class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tid` (`tid`),
  KEY `cid` (`cid`),
  KEY `tid_2` (`tid`),
  KEY `cid_2` (`cid`),
  KEY `tid_3` (`tid`),
  KEY `cid_3` (`cid`),
  CONSTRAINT `c1` FOREIGN KEY (`cid`) REFERENCES `class` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `t1` FOREIGN KEY (`tid`) REFERENCES `teacher` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `teacher2class`
-- ----------------------------
BEGIN;
INSERT INTO `teacher2class` VALUES ('2', '1', '2'), ('3', '2', '2');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
