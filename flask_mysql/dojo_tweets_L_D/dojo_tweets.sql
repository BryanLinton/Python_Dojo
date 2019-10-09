-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dojo_tweets
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojo_tweets` ;

-- -----------------------------------------------------
-- Schema dojo_tweets
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojo_tweets` DEFAULT CHARACTER SET utf8 ;
USE `dojo_tweets` ;

-- -----------------------------------------------------
-- Table `dojo_tweets`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojo_tweets`.`users` ;

CREATE TABLE IF NOT EXISTS `dojo_tweets`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(60) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dojo_tweets`.`tweets`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojo_tweets`.`tweets` ;

CREATE TABLE IF NOT EXISTS `dojo_tweets`.`tweets` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `users_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tweets_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_tweets_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `dojo_tweets`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dojo_tweets`.`liked_tweets`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojo_tweets`.`liked_tweets` ;

CREATE TABLE IF NOT EXISTS `dojo_tweets`.`liked_tweets` (
  `user_id` INT(11) NOT NULL,
  `tweet_id` INT(11) NOT NULL,
  PRIMARY KEY (`user_id`, `tweet_id`),
  INDEX `fk_users_has_tweets_tweets1_idx` (`tweet_id` ASC) VISIBLE,
  INDEX `fk_users_has_tweets_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_tweets_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `dojo_tweets`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_tweets_tweets1`
    FOREIGN KEY (`tweet_id`)
    REFERENCES `dojo_tweets`.`tweets` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
