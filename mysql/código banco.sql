-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: colegio
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos` (
  `id_aluno` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `matricula` int NOT NULL,
  PRIMARY KEY (`matricula`),
  UNIQUE KEY `matricula_UNIQUE` (`id_aluno`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (1,'Marcos',992),(11,'patrick',1123),(2,'Gabriel',2355),(3,'Pedro',8734),(9,'Jorge Lucas',8772),(8,'Carlos',8882),(14,'kauan',9025),(10,'rodrigo henrique',9088),(6,'Paulinho',9264),(15,'Joao Pedro',9267);
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disciplina`
--

DROP TABLE IF EXISTS `disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disciplina` (
  `id_disciplina` int NOT NULL AUTO_INCREMENT,
  `nome_disciplina` varchar(45) NOT NULL,
  PRIMARY KEY (`id_disciplina`),
  UNIQUE KEY `nome_disciplina_UNIQUE` (`nome_disciplina`),
  UNIQUE KEY `id_disciplina_UNIQUE` (`id_disciplina`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disciplina`
--

LOCK TABLES `disciplina` WRITE;
/*!40000 ALTER TABLE `disciplina` DISABLE KEYS */;
INSERT INTO `disciplina` VALUES (9,'biologia'),(7,'ciencias'),(5,'física'),(3,'geografia'),(4,'história'),(8,'literatura'),(2,'matemática'),(1,'português'),(6,'quimica');
/*!40000 ALTER TABLE `disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notas`
--

DROP TABLE IF EXISTS `notas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notas` (
  `id_notas` int NOT NULL AUTO_INCREMENT,
  `nota1` varchar(45) DEFAULT NULL,
  `nota2` varchar(45) DEFAULT NULL,
  `nota3` varchar(45) DEFAULT NULL,
  `alunos_matricula` int NOT NULL,
  `disciplina_id_disciplina` int NOT NULL,
  `media` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_notas`,`alunos_matricula`,`disciplina_id_disciplina`),
  UNIQUE KEY `id_notas_UNIQUE` (`id_notas`),
  KEY `fk_notas_alunos_idx` (`alunos_matricula`),
  KEY `fk_notas_disciplina1_idx` (`disciplina_id_disciplina`),
  CONSTRAINT `fk_notas_disciplina1` FOREIGN KEY (`disciplina_id_disciplina`) REFERENCES `disciplina` (`id_disciplina`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notas`
--

LOCK TABLES `notas` WRITE;
/*!40000 ALTER TABLE `notas` DISABLE KEYS */;
INSERT INTO `notas` VALUES (1,'8','7','5',2355,4,NULL),(5,'3','7','5',8734,2,'6.0'),(7,'3','7','5',992,4,'3.3'),(9,'9','5','8',772,5,NULL),(10,'8','5','7',2355,5,NULL),(11,'8','6','9',8922,5,NULL),(12,'8','5','0',8922,6,NULL),(31,'7','3','6',992,5,'3.3'),(32,'8','5','9',992,8,'6.0'),(34,'8','4','6',8734,3,'6.0'),(35,'9','3','6',9264,6,'6.0'),(36,'8','5','9',9274,4,'7.3'),(37,'9','2','6',8882,2,'5.7'),(39,'9','4','8',992,6,'3.3'),(40,'5','3','2',992,3,'3.3'),(44,'7','5','6',8772,8,'6.0'),(45,'8','4','6',8772,4,'6.0'),(46,'3','4','6',8772,5,'4.3'),(47,'7','3','5',9088,6,'5.0'),(48,'7','5','6',8772,7,'6.0'),(49,'6','4','5',992,7,'5.0'),(50,'8','3','5',1123,3,'5.3'),(51,'2','3','5',9025,1,'3.3'),(52,'5','6','5',9267,1,'5.3');
/*!40000 ALTER TABLE `notas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'colegio'
--

--
-- Dumping routines for database 'colegio'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-23 20:23:33
