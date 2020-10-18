CREATE TABLE IF NOT EXISTS pharmacies (
    `Name` VARCHAR(41) CHARACTER SET utf8,
    `Address` VARCHAR(22) CHARACTER SET utf8,
    `Telephone` NUMERIC(17, 6),
    `Lat` NUMERIC(8, 6),
    `Lon` NUMERIC(7, 6)
);
INSERT INTO pharmacies VALUES
    ('LINDA - Berthold Apotheke','Lichtentaler Str. 72',49722122331,48.754705,8.243974),
    ('Augusta-Apotheke','Ludwig-Wilhelm-Platz 3',49722124537,48.758028,8.241467),
    ('Löwen Apotheke 24','Lichtentaler Str. 3',49722122120,48.760424,8.240462),
    ('Stadt-Apotheke Baden-Baden','Gernsbacher Str. 2',4.97E+11,48.761617,8.240188),
    ('Bäder Apotheke','Gernsbacher Str. 34',49722124056,48.762509,8.242719),
    ('Kreuz Apotheke Inh. Matthias Kraemer e.K.','Lange Str. 37',49722125502,48.763358,8.237667);
