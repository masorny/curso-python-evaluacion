CREATE DATABASE loginlog

CREATE TABLE registrologin(
    idlog int NOT NULL AUTO_INCREMENT,
    urlvisitada VARCHAR(300) NOT NULL,
    matricula VARCHAR(30) NOT NULL,
    fechaingreso DATETIME not null,
    
    PRIMARY KEY (idlog)
);