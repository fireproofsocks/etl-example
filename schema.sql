# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.22)
# Database: parking
# Generation Time: 2019-06-21 20:06:51 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table violations
# ------------------------------------------------------------

CREATE TABLE `violations` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ticket_number` int(11) unsigned NOT NULL,
  `issue_date` datetime NOT NULL,
  `make` varchar(8) NOT NULL DEFAULT '',
  `body_style` varchar(16) NOT NULL DEFAULT '',
  `color` varchar(8) NOT NULL DEFAULT '',
  `location` varchar(32) NOT NULL DEFAULT '',
  `route` varchar(32) NOT NULL DEFAULT '',
  `agency` varchar(32) NOT NULL DEFAULT '',
  `violation_code` varchar(32) NOT NULL DEFAULT '',
  `violation_description` varchar(64) NOT NULL DEFAULT '',
  `fine_amount` decimal(6,2) NOT NULL DEFAULT '0.00',
  `latitude` double(13,9) NOT NULL DEFAULT '0.000000000',
  `longitude` double(13,9) NOT NULL DEFAULT '0.000000000',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
