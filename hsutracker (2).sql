-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 07, 2019 at 08:08 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hsutracker`
--

-- --------------------------------------------------------

--
-- Table structure for table `entity`
--

CREATE TABLE `entity` (
  `id` int(30) NOT NULL,
  `idBarcode` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `entity`
--

INSERT INTO `entity` (`id`, `idBarcode`) VALUES
(1, 1313);

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

CREATE TABLE `event` (
  `id` int(40) NOT NULL,
  `name` varchar(50) NOT NULL,
  `startTime` datetime NOT NULL,
  `endTime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `event`
--

INSERT INTO `event` (`id`, `name`, `startTime`, `endTime`) VALUES
(1, 'test1', '2019-11-06 00:00:00', '2019-11-07 00:00:00'),
(2, 'test2', '2019-11-08 00:00:00', '2019-11-09 00:00:00'),
(3, 'test3', '2000-01-01 00:00:00', '2000-01-01 12:00:00'),
(4, 'test4', '2000-01-01 00:00:00', '2000-01-20 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `joineventmember`
--

CREATE TABLE `joineventmember` (
  `id` int(40) NOT NULL,
  `idMember` int(40) NOT NULL,
  `idEvent` int(40) NOT NULL,
  `direction` tinyint(1) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `joinstudentparent`
--

CREATE TABLE `joinstudentparent` (
  `studentId` int(30) NOT NULL,
  `parentId` int(30) NOT NULL,
  `id` int(30) NOT NULL,
  `relationship` varchar(20) NOT NULL,
  `canCollect` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `lName` varchar(25) NOT NULL,
  `fName` varchar(25) NOT NULL,
  `mInitial` varchar(1) DEFAULT NULL,
  `dob` datetime NOT NULL,
  `address` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL,
  `id` int(30) NOT NULL,
  `photo` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`lName`, `fName`, `mInitial`, `dob`, `address`, `status`, `id`, `photo`) VALUES
('Price', 'Gareth', 'T', '1994-10-15 00:00:00', '313 Somerset Dr Fort Walton Beach, Fl 32547', 'Actve', 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `parents`
--

CREATE TABLE `parents` (
  `id` int(30) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `phone2` varchar(10) DEFAULT NULL,
  `email` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(30) NOT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `school` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `voluenteer`
--

CREATE TABLE `voluenteer` (
  `id` int(30) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `phone2` varchar(10) DEFAULT NULL,
  `email` varchar(40) NOT NULL,
  `position` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `entity`
--
ALTER TABLE `entity`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uniqueBarcode` (`idBarcode`);

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `joineventmember`
--
ALTER TABLE `joineventmember`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idMember` (`idMember`,`idEvent`),
  ADD KEY `idEvent` (`idEvent`);

--
-- Indexes for table `joinstudentparent`
--
ALTER TABLE `joinstudentparent`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studentId` (`studentId`),
  ADD KEY `parentId` (`parentId`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `parents`
--
ALTER TABLE `parents`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `voluenteer`
--
ALTER TABLE `voluenteer`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `entity`
--
ALTER TABLE `entity`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `event`
--
ALTER TABLE `event`
  MODIFY `id` int(40) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `joineventmember`
--
ALTER TABLE `joineventmember`
  MODIFY `id` int(40) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `joinstudentparent`
--
ALTER TABLE `joinstudentparent`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `joineventmember`
--
ALTER TABLE `joineventmember`
  ADD CONSTRAINT `joineventmember_ibfk_1` FOREIGN KEY (`idEvent`) REFERENCES `event` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `joineventmember_ibfk_2` FOREIGN KEY (`idMember`) REFERENCES `members` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `joinstudentparent`
--
ALTER TABLE `joinstudentparent`
  ADD CONSTRAINT `joinstudentparent_ibfk_1` FOREIGN KEY (`studentId`) REFERENCES `students` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `joinstudentparent_ibfk_2` FOREIGN KEY (`parentId`) REFERENCES `parents` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `members`
--
ALTER TABLE `members`
  ADD CONSTRAINT `members_ibfk_1` FOREIGN KEY (`id`) REFERENCES `entity` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `parents`
--
ALTER TABLE `parents`
  ADD CONSTRAINT `parents_ibfk_1` FOREIGN KEY (`id`) REFERENCES `members` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `students_ibfk_1` FOREIGN KEY (`id`) REFERENCES `members` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `voluenteer`
--
ALTER TABLE `voluenteer`
  ADD CONSTRAINT `voluenteer_ibfk_1` FOREIGN KEY (`id`) REFERENCES `members` (`id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
