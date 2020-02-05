-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: football_database
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Club`
--

DROP TABLE IF EXISTS `Club`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Club` (
  `Stadium` varchar(20) NOT NULL,
  `League_name` varchar(20) NOT NULL,
  `Logo` blob,
  `Club_name` varchar(30) NOT NULL,
  PRIMARY KEY (`Club_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Club`
--

LOCK TABLES `Club` WRITE;
/*!40000 ALTER TABLE `Club` DISABLE KEYS */;
INSERT INTO `Club` VALUES ('Emirates Stadium','Premier League',NULL,'Arsenal'),('Wanda Metropolitano','La Liga',NULL,'Atlético Madrid'),('Stamford Bridge','Premier League',NULL,'Chelsea'),('Camp Nou','La Liga',NULL,'FC Barcelona'),('San Siro','Serie A',NULL,'Inter Milan'),('Allianz Stadium','Serie A',NULL,'Juventus'),('Anfield Stadium','Premier League',NULL,'Liverpool'),('Etihad Stadium','Premier League',NULL,'Manchester City'),('Old Trafford','Premier League',NULL,'Manchester United'),('San Paolo Stadium','Serie A',NULL,'Napoli'),('Santiago Bernabéu','La Liga',NULL,'Real Madrid');
/*!40000 ALTER TABLE `Club` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Country`
--

DROP TABLE IF EXISTS `Country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Country` (
  `Name` varchar(20) NOT NULL,
  `League_name` varchar(20) NOT NULL,
  `Logo` blob,
  `Manager_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Country`
--

LOCK TABLES `Country` WRITE;
/*!40000 ALTER TABLE `Country` DISABLE KEYS */;
INSERT INTO `Country` VALUES ('England','Premier League',_binary 'NULL',2),('Italy',' Series A',_binary 'NULL',3),('Spain','La liga',_binary 'NULL',1);
/*!40000 ALTER TABLE `Country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Injuries`
--

DROP TABLE IF EXISTS `Injuries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Injuries` (
  `Player_ID` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Injury_name` varchar(20) NOT NULL,
  `Duration_of_injury_weeks` int(11) DEFAULT NULL,
  KEY `Player_ID` (`Player_ID`),
  CONSTRAINT `Injuries_ibfk_1` FOREIGN KEY (`Player_ID`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Injuries`
--

LOCK TABLES `Injuries` WRITE;
/*!40000 ALTER TABLE `Injuries` DISABLE KEYS */;
INSERT INTO `Injuries` VALUES (15,'2020-01-16','Groin',NULL);
/*!40000 ALTER TABLE `Injuries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `League`
--

DROP TABLE IF EXISTS `League`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `League` (
  `League_name` char(20) NOT NULL,
  `Logo` blob,
  `Country` char(20) NOT NULL,
  PRIMARY KEY (`League_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `League`
--

LOCK TABLES `League` WRITE;
/*!40000 ALTER TABLE `League` DISABLE KEYS */;
INSERT INTO `League` VALUES ('La Liga',_binary 'NULL','Spain'),('Premier League',_binary 'NULL','England'),('Serie A',_binary 'NULL','Italy');
/*!40000 ALTER TABLE `League` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manager`
--

DROP TABLE IF EXISTS `Manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Manager` (
  `Win_Percentage` decimal(3,1) DEFAULT NULL,
  `Current_Club` varchar(20) DEFAULT NULL,
  `Active_since` int(11) NOT NULL,
  `Manager_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(15) NOT NULL,
  `Country` varchar(15) DEFAULT NULL,
  `Formation` varchar(15) DEFAULT NULL,
  `Photo` blob,
  `Contract` int(11) DEFAULT NULL,
  `Salary` int(11) DEFAULT NULL,
  PRIMARY KEY (`Manager_ID`),
  KEY `Current_Club` (`Current_Club`),
  CONSTRAINT `Manager_ibfk_1` FOREIGN KEY (`Current_Club`) REFERENCES `Club` (`Club_name`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manager`
--

LOCK TABLES `Manager` WRITE;
/*!40000 ALTER TABLE `Manager` DISABLE KEYS */;
INSERT INTO `Manager` VALUES (33.3,'Arsenal',2019,1,'Mikel Arteta','Spain','4-2-3-1',NULL,2023,NULL),(71.8,'Manchester City',2016,2,'Pep Guardiola','Spain','4-3-3',NULL,2021,NULL),(60.9,'Liverpool',2015,3,'Jürgen Klopp','Germany','4-3-3',NULL,2024,NULL),(50.0,'Chelsea',2019,4,'Frank Lampard','England','4-2-3-1',NULL,2022,NULL),(50.0,'Manchester United',2018,5,'Ole Solksjaer','Norway','4-2-3-1',NULL,2022,NULL),(77.4,'Juventus',2019,6,'Maurizio Sarri','Italy','4-3-3',NULL,2022,NULL),(63.3,'Inter Milan',2019,7,'Antonio Conte','Italy','3-4-2-1',NULL,2022,NULL),(55.6,'Napoli',2019,8,'Gennaro Gattuso','Italy','4-3-3',NULL,NULL,NULL),(80.0,'FC Barcelona',2020,9,'Quique Setien','Spain','3-4-2-1',NULL,2020,NULL),(58.1,'Real Madrid',2019,10,'Zinedine Zidane','France','4-3-3',NULL,2020,NULL),(60.0,'Atletico Madrid',2011,11,'Diego Simeone','Spain','4-4-2',NULL,2022,NULL);
/*!40000 ALTER TABLE `Manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Match_Details`
--

DROP TABLE IF EXISTS `Match_Details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Match_Details` (
  `Date` date NOT NULL,
  `Team1` varchar(20) NOT NULL,
  `Team2` varchar(20) NOT NULL,
  `Venue` varchar(20) NOT NULL,
  `Score` varchar(20) DEFAULT NULL,
  `Shots_1` int(11) DEFAULT NULL,
  `Shots_2` int(11) DEFAULT NULL,
  `Possession_percentage_1` int(11) DEFAULT NULL,
  `Possession_percentage_2` int(11) DEFAULT NULL,
  `Red_Cards_1` int(11) DEFAULT NULL,
  `Red_Cards_2` int(11) DEFAULT NULL,
  `Yellow_Cards_1` int(11) DEFAULT NULL,
  `Yellow_Cards_2` int(11) DEFAULT NULL,
  `Referee_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Date`,`Team1`,`Team2`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Match_Details`
--

LOCK TABLES `Match_Details` WRITE;
/*!40000 ALTER TABLE `Match_Details` DISABLE KEYS */;
INSERT INTO `Match_Details` VALUES ('2019-10-07','Inter Milan','Juventus','San Siro','1-2',10,18,52,48,0,0,2,3,'5'),('2019-11-10','Liverpool','Manchester City','Anfield','3-1',12,18,45,55,0,0,0,2,'1'),('2019-11-23','Manchester City','Chelsea','Etihad','2-1',15,11,46,54,0,0,1,1,'3'),('2019-12-07','Manchester City','Manchester United','Etihad','1-2',23,11,72,28,0,0,3,2,'3'),('2019-12-19','Barcelona','Real Madrid','Camp Nou','0-0',9,17,53,47,0,0,3,5,'8'),('2020-01-02','Real Madrid','Atletico Madrid','Santiago Bernabeu','1-0',16,4,66,34,0,0,2,2,'7'),('2020-01-07','Napoli','Inter Milan','Stadio San Paolo','1-3',19,14,57,43,0,0,0,5,'6'),('2020-01-19','Liverpool','Manchester United','Anfield','2-0',16,9,54,46,0,0,1,3,'2'),('2020-01-22','Chelsea','Arsenal','Stamford Bridge','2-2',19,2,59,41,0,1,2,1,'2'),('2020-01-27','Napoli','Juventus','Stadio San Paolo','2-1',15,8,52,48,0,0,2,5,'4');
/*!40000 ALTER TABLE `Match_Details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Referee`
--

DROP TABLE IF EXISTS `Referee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Referee` (
  `Referee_Name` varchar(20) NOT NULL,
  `Red_cards` int(11) DEFAULT NULL,
  `Yellow_cards` int(11) DEFAULT NULL,
  `Referee_id` int(11) NOT NULL,
  `Penalties_given` int(11) DEFAULT NULL,
  `League_name` varchar(20) NOT NULL,
  `Appearances` int(11) DEFAULT NULL,
  `Salary` int(11) DEFAULT NULL,
  PRIMARY KEY (`Referee_id`),
  KEY `League_name` (`League_name`),
  CONSTRAINT `Referee_ibfk_1` FOREIGN KEY (`League_name`) REFERENCES `League` (`League_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Referee`
--

LOCK TABLES `Referee` WRITE;
/*!40000 ALTER TABLE `Referee` DISABLE KEYS */;
INSERT INTO `Referee` VALUES ('Mike Dean',2,80,1,4,'Premier League',18,0),('Michael Oliver',2,64,2,2,'Premier League',18,0),('Kevin Friend',3,59,3,2,'Premier League',17,0),('Mario Melero López',2,72,4,4,'La Liga',12,0),('Jesús Gil Manzano',5,59,5,5,'La Liga',12,0),('Adrián Cordero Vega',1,43,6,8,'La Liga',12,0),('Daniele Doveri',1,53,7,1,'Serie A',11,0),('Gianluca Rocchi',5,68,8,7,'Serie A',11,0),('Federico La Penna',3,51,9,5,'Serie A',11,0);
/*!40000 ALTER TABLE `Referee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Season_club`
--

DROP TABLE IF EXISTS `Season_club`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Season_club` (
  `Matches_played` int(11) DEFAULT NULL,
  `Matches_won` int(11) DEFAULT NULL,
  `Matches_Lost` int(11) DEFAULT NULL,
  `League_Position` int(11) DEFAULT NULL,
  `Club_name` varchar(20) NOT NULL,
  `Season_Year` varchar(20) DEFAULT NULL,
  `League_Name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Club_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Season_club`
--

LOCK TABLES `Season_club` WRITE;
/*!40000 ALTER TABLE `Season_club` DISABLE KEYS */;
INSERT INTO `Season_club` VALUES (32,21,10,5,'Arsenal','2018-2019','Series A'),(38,20,9,3,'Atalanta','2018-2019','Series A'),(38,26,3,1,'Barcelona','2018-2019','La lega'),(38,28,4,1,'Juventus','2018-2019','Series A'),(39,30,1,2,'Liverpool','2018-2019','Premium League'),(38,32,4,1,'Manchester city',' 2018-2019','Premium League'),(38,19,10,4,'Manchester United','2018-2019','Premium League'),(38,24,7,2,'Napoli','2018-2019','Series A'),(38,21,12,3,'Real Madrid','2018-2019','La lega'),(38,17,13,6,'Sevilla','2018-2019','La lega'),(38,23,13,4,'Tottenham','2018-2019','Premium League'),(38,15,7,4,'Valencia','2018-2019','La lega'),(38,16,13,7,'Wolves','2018-2019','Premium League');
/*!40000 ALTER TABLE `Season_club` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Season_country`
--

DROP TABLE IF EXISTS `Season_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Season_country` (
  `Matches_played` int(11) DEFAULT NULL,
  `Matches_won` int(11) DEFAULT NULL,
  `Matches_Lost` int(11) DEFAULT NULL,
  `Name` varchar(20) NOT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Season_country`
--

LOCK TABLES `Season_country` WRITE;
/*!40000 ALTER TABLE `Season_country` DISABLE KEYS */;
/*!40000 ALTER TABLE `Season_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Season_player`
--

DROP TABLE IF EXISTS `Season_player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Season_player` (
  `Player_ID` int(11) DEFAULT NULL,
  `Games_Played` int(11) NOT NULL,
  `Goals` int(11) DEFAULT NULL,
  `Assists` int(11) DEFAULT NULL,
  `Yellow_cards` int(11) DEFAULT NULL,
  `Red_cards` int(11) DEFAULT NULL,
  `Club` varchar(30) NOT NULL,
  `Tackles` int(11) DEFAULT NULL,
  KEY `Player_ID` (`Player_ID`),
  CONSTRAINT `Season_player_ibfk_1` FOREIGN KEY (`Player_ID`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Season_player`
--

LOCK TABLES `Season_player` WRITE;
/*!40000 ALTER TABLE `Season_player` DISABLE KEYS */;
INSERT INTO `Season_player` VALUES (1,16,2,2,3,0,'Liverpool',10),(2,24,3,4,1,0,'Liverpool',53),(6,4,0,0,0,0,'Manchester City',0),(8,18,3,7,0,0,'Manchester City',18),(12,9,1,0,4,0,'Manchester United',12),(14,24,3,6,3,0,'Manchester United',20),(16,10,2,0,2,0,'Chelsea',14),(20,24,4,4,2,0,'Chelsea',33),(17,23,4,2,9,0,'Chelsea',49),(21,25,0,0,2,0,'Arsenal',0),(22,18,2,0,5,0,'Arsenal',24),(23,22,2,0,4,1,'Arsenal',22);
/*!40000 ALTER TABLE `Season_player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `player` (
  `player_name` varchar(30) NOT NULL,
  `Games_Played` int(11) DEFAULT NULL,
  `Goals` int(11) DEFAULT NULL,
  `Assists` int(11) DEFAULT NULL,
  `Main_position` varchar(15) DEFAULT NULL,
  `Age` int(11) NOT NULL,
  `Country_representation` varchar(20) NOT NULL,
  `Player_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Current_Club` varchar(15) DEFAULT NULL,
  `Active_since` varchar(15) NOT NULL,
  `Photo` blob,
  `Contract` varchar(20) NOT NULL,
  `Market_Value` int(11) NOT NULL,
  `Salary` int(11) DEFAULT NULL,
  `Height` int(11) DEFAULT NULL,
  `Weight` int(11) DEFAULT NULL,
  `Preferred_foot` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Player_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES ('\"James Milner\"',532,55,84,'\"Midfielder\"',34,'\"England\"',1,'\"Liverpool\"','2001','','2022',10800000,0,175,72,''),('\"jordan Henderson\"',334,29,45,'\"Midfielder\"',29,'\"England\"',2,'\"Liverpool\"','2008','','2023',31500000,0,182,75,''),('\"Joel Matip\"',83,4,0,'\"Defender\"',28,'\"Cameroon\"',3,'\"Liverpool\"','2017','','2024',36000000,0,195,78,''),('\"Sadio Mane\"',181,77,28,'\"Forward\"',28,'\"Senegal\"',4,'\"Liverpool\"','2015','','2023',135000000,0,175,68,''),('\"Alisson\"',55,0,1,'\"Goalkeeper\"',31,'\"Brazil\"',5,'\"Liverpool\"','2018','','2024',81000000,0,185,72,''),('\"Claudio Bravo\"',29,0,0,'\"Goalkeeper\"',36,'\"Chile\"',6,'\"Manchester Cit','2016','','2020',1350000,0,184,76,''),('\"Kyle Walker\"',282,7,27,'\"Defender\"',29,'\"England\"',7,'\"Manchester Cit','2010','','2024',45000000,0,178,75,''),('\"David Silva\"',300,57,90,'\"Midfielder\"',34,'\"Spain\"',8,'\"Manchester Cit','2010','','2020',13500000,0,173,70,''),('\"Riyadh Mahrez\"',187,53,38,'\"Forward\"',28,'\"Algeria\"',9,'\"Manchester Cit','2014','','2023',53000000,0,179,79,''),('\"Gabriel Jesus\"',89,36,14,'\"Forward\"',22,'\"Brazil\"',10,'\"Manchester Cit','2016','','2023',63000000,0,175,76,''),('\"David de Gea\"',300,0,0,'\"Goalkeeper\"',29,'\"Spain\"',11,'\"Manchester Uni','2011','','2023',54000000,0,192,79,''),('\"Brandon Williams\"',9,1,0,'\"Defender\"',19,'\"England\"',12,'\"Manchester Uni','2019','','2022',6300000,0,171,67,''),('\"Andreas Pereira\"',42,2,4,'\"Midfielder\"',24,'\"Brazil\"',13,'\"Manchester Uni','2014','','2023',18000000,0,178,65,''),('\"Daniel James\"',24,3,6,'\"Midfielder\"',22,'\"Wales\"',14,'\"Manchester Uni','2015','','2024',25200000,0,170,72,''),('\"Marcus Rashford\"',133,41,18,'\"Forward\"',22,'\"England\"',15,'\"Manchester Uni','2015','','2023',72000000,0,180,80,''),('\"Antonio Rudiger\"',70,1,5,'\"Goalkeeper\"',26,'\"Germany\"',16,'\"Chelsea\"','2017','','2022',45000000,0,190,82,''),('\"Jorginho\"',60,6,2,'\"Midfielder\"',28,'\"Italy\"',17,'\"Chelsea\"','2018','','2023',5850000,0,180,66,''),('\"Mateo Kovacic\"',54,1,5,'\"Midfielder\"',25,'\"Croatia\"',18,'\"Chelsea\"','2018','','2024',40500000,0,178,64,''),('\"Tammy Abraham\"',57,18,4,'\"Forward\"',22,'\"England\"',19,'\"Chelsea\"','2015','','2022',45000000,0,190,79,''),('\"Willian\"',222,32,30,'\"Forward\"',31,'\"Brazil\"',20,'\"Chelsea\"','2013','','2020',28800000,0,175,67,''),('\"Bernd Leno\"',57,0,0,'\"Goalkeeper\"',27,'\"Germany\"',21,'\"Arsenal\"','2018','','2023',31500000,0,190,80,''),('\"Sokratis\"',43,3,2,'\"Defender\"',31,'\"Greece\"',22,'\"Arsenal\"','2018','','2021',16200000,0,186,66,''),('\"David Luiz\"',182,13,6,'\"Defender\"',32,'\"Brazil\"',23,'\"Arsenal\"','2010','','2021',13500000,0,189,68,'');
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-05 10:48:16
