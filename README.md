# VirtualEnv creation
```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```

# Run program on Windows
```
set FLASK_APP=main
set FLASK_ENV=development
python -m flask run
```

# MySQL Database creation
```sql
CREATE DATABASE IF NOT EXISTS dashboard;
USE dashboard;

DROP TABLE IF EXISTS chart_table;

CREATE TABLE IF NOT EXISTS chart_table (
	`PersonID` int AUTO_INCREMENT PRIMARY KEY,
    `LastName` varchar(255) NULL,
    `Section` float NULL,
    `AttentionSpan` varchar(255) NULL,
    `GradeAverage` float NULL
);

ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';

INSERT INTO `chart_table` (`LastName`, `Section`, `AttentionSpan`, `GradeAverage`) VALUES ("Zou", 1, "good", 95);
INSERT INTO `chart_table` (`LastName`, `Section`, `AttentionSpan`, `GradeAverage`) VALUES ("Kabdou", 1, "great", 100);
INSERT INTO `chart_table` (`LastName`, `Section`, `AttentionSpan`, `GradeAverage`) VALUES ("To", 2, "great", 95);
INSERT INTO `chart_table` (`LastName`, `Section`, `AttentionSpan`, `GradeAverage`) VALUES ("Mao", 2, "excellent", 98);
INSERT INTO `chart_table` (`LastName`, `Section`, `AttentionSpan`, `GradeAverage`) VALUES ("Chadha", 9, "excellent", 90);
INSERT INTO `chart_table` (`LastName`, `Section`, `AttentionSpan`, `GradeAverage`) VALUES ("Chen", 3, "decent", 80);
INSERT INTO `chart_table` (`LastName`, `Section`, `AttentionSpan`, `GradeAverage`) VALUES ("Guo", 4, "good", 64);
INSERT INTO `chart_table` (`LastName`, `Section`, `AttentionSpan`, `GradeAverage`) VALUES ("Porwal", 4, "great", 65);
INSERT INTO `chart_table` (`LastName`, `Section`, `AttentionSpan`, `GradeAverage`) VALUES ("Lu", 5, "decent", 96);
INSERT INTO `chart_table` (`LastName`, `Section`, `AttentionSpan`, `GradeAverage`) VALUES ("Wei", 5, "good", 95);


DROP TABLE IF EXISTS scatter_table;

CREATE TABLE IF NOT EXISTS scatter_table (
	`PersonID` int AUTO_INCREMENT PRIMARY KEY,
    `LastName` varchar(255) NULL,
    `Section` float NULL,
    `TimeLogged` float NULL,
    `GradeAverage` float NULL
);

ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';

INSERT INTO `scatter_table` (`LastName`, `Section`, `TimeLogged`, `GradeAverage`) VALUES ("Zou", 1, 80, 95);
INSERT INTO `scatter_table` (`LastName`, `Section`, `TimeLogged`, `GradeAverage`) VALUES ("Kabdou", 1, 98, 100);
INSERT INTO `scatter_table` (`LastName`, `Section`, `TimeLogged`, `GradeAverage`) VALUES ("To", 2, 85, 95);
INSERT INTO `scatter_table` (`LastName`, `Section`, `TimeLogged`, `GradeAverage`) VALUES ("Mao", 2, 90, 98);
INSERT INTO `scatter_table` (`LastName`, `Section`, `TimeLogged`, `GradeAverage`) VALUES ("Chadha", 3, 75, 90);
INSERT INTO `scatter_table` (`LastName`, `Section`, `TimeLogged`, `GradeAverage`) VALUES ("Chen", 3, 60, 80);
INSERT INTO `scatter_table` (`LastName`, `Section`, `TimeLogged`, `GradeAverage`) VALUES ("Guo", 4, 50, 64);
INSERT INTO `scatter_table` (`LastName`, `Section`, `TimeLogged`, `GradeAverage`) VALUES ("Porwal", 4, 78, 65);
INSERT INTO `scatter_table` (`LastName`, `Section`, `TimeLogged`, `GradeAverage`) VALUES ("Lu", 5, 89, 96);
INSERT INTO `scatter_table` (`LastName`, `Section`, `TimeLogged`, `GradeAverage`) VALUES ("Wei", 5, 90, 95);



select * from chart_table;
select * from scatter_table;
```