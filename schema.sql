CREATE TABLE users (id SERIAL PRIMARY KEY, 
            username VARCHAR UNIQUE (30), password VARCHAR (200), 
            joindate TIMESTAMP, visible BOOLEAN);

CREATE TABLE stations (id SERIAL PRIMARY KEY, 
            station_name VARCHAR (100), addr VARCHAR (150), city VARCHAR (100), 
            postnr VARCHAR (10), road VARCHAR (10), operational BOOLEAN, 
            visible BOOLEAN);

CREATE TABLE prices (id SERIAL PRIMARY KEY, station_id INTEGER REFERENCES stations,
            user_id INTEGER REFERENCES users, time TIMESTAMP, visible BOOLEAN,
            type1_price FLOAT(5), type2_price FLOAT(5), type3_price FLOAT(5), type4_price FLOAT (5));

CREATE TABLE requests (id SERIAL PRIMARY KEY, sender_id INTEGER REFERENCES users,
            message VARCHAR (200), time TIMESTAMP, visible BOOLEAN);

CREATE TABLE chat (id SERIAL PRIMARY KEY, sender_id INTEGER REFERENCES users,
            message VARCHAR, time TIMESTAMP);

CREATE TABLE admin_users (user_id INTEGER REFERENCES users);

CREATE TABLE products (id SERIAL PRIMARY KEY, name VARCHAR (30));

INSERT INTO users (username,password,joindate) VALUES ('BOSS','pbkdf2:sha256:150000$V0pONHil$d8abb05ccc68d571eee30bffe99f6be7515126e90c4580f2f6912f3e8634dc67',NOW());

INSERT INTO admin_users (user_id) VALUES (1);

INSERT INTO products (name) VALUES ('95 E10');
INSERT INTO products (name) VALUES ('98 E5');
INSERT INTO products (name) VALUES ('DIESEL');
INSERT INTO products (name) VALUES ('E85');


INSERT INTO stations (station_name,addr, city, postnr, road, operational, visible)
             VALUES ('Shell Express Itäväylä','Vehkalahdentie 39','Helsinki','00950','170',TRUE,TRUE);

INSERT INTO prices (station_id,user_id,time,type1_price,type2_price,type3_price) VALUES
            (1,1,NOW(),1.619,1.728,1.489);