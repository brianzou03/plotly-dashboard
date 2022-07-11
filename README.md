# VirtualEnv creation
```
python3 -m venv ./venv
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

DROP TABLE IF EXISTS dash_table;

CREATE TABLE IF NOT EXISTS dash_table (
	`PersonID` int AUTO_INCREMENT PRIMARY KEY,
    `LastName` varchar(255) NULL,
    `Stat1` float NULL,
    `Stat2` float NULL,
    `Stat3` float NULL
);

ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';

INSERT INTO `dash_table` (`LastName`, `Stat1`, `Stat2`, `Stat3`) VALUES ("Zou", 1, 50, 100);
INSERT INTO `dash_table` (`LastName`, `Stat1`, `Stat2`, `Stat3`) VALUES ("Kabdou", 5, 60, 100);
INSERT INTO `dash_table` (`LastName`, `Stat1`, `Stat2`, `Stat3`) VALUES ("To", 7, 80, 95);

select * from dash_table;

```