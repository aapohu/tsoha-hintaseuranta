
add_user = "INSERT INTO users (username, password, joindate, visible) \
            VALUES (:name, :password, NOW() AT TIME ZONE 'Europe/Helsinki', TRUE);"

add_price = "INSERT INTO prices (station_id, user_id, time, visible, type1_price, type2_price, type3_price, type4_price) \
             VALUES (:station, :user, NOW() AT TIME ZONE 'Europe/Helsinki', TRUE, :price1, :price2, :price3, :price4);"

add_station = "INSERT INTO stations (station_name, addr, city, postnr, road, operational, visible) \
               VALUES (:name, :address, :city, :postnr, :road, TRUE, TRUE);"

update_station = "UPDATE stations SET station_name = :name, addr = :address, city = :city, postnr = :postnr, road = :road WHERE id=:id;"

hide_price = "UPDATE prices SET visible=FALSE WHERE id=:pid;"

close_station = "UPDATE stations SET operational = FALSE WHERE id=:stid;"

open_station = "UPDATE stations SET operational = TRUE WHERE id=:stid;"

ban_user = "UPDATE users SET visible = FALSE WHERE id=:uid;"

unban_user = "UPDATE users SET visible = TRUE WHERE id=:uid;"

get_stations = "SELECT * FROM stations WHERE operational = TRUE ORDER BY id DESC;"

get_prices = "SELECT DISTINCT ON (S.station_name) S.station_name, S.id, P.type1_price, P.type2_price, P.type3_price, P.type4_price, P.time FROM prices P, stations S WHERE S.id = P.station_id AND P.visible = TRUE ORDER BY time DESC LIMIT 30;"


#gets latest 30 prices from unique stations
get_prices_2 = "SELECT s.station_name, x.station_id, x.type1_price, x.type2_price, x.type3_price, x.type4_price, x.time \
                FROM (SELECT DISTINCT ON(station_id) station_id, type1_price, type2_price, type3_price, type4_price, time, visible \
                        FROM prices \
                        WHERE visible = TRUE \
                        ORDER BY station_id, time DESC) AS x, stations AS s \
                WHERE x.station_id = s.id \
                ORDER BY x.time DESC\
                LIMIT 30;"

search_prices = ["SELECT DISTINCT ON (S.station_name) S.station_name, S.id, P.type1_price, P.type2_price, P.type3_price, P.type4_price, P.time \
            FROM prices P, stations S \
            WHERE S.id = P.station_id AND P.visible = TRUE AND S.road = :search\
            ORDER BY S.station_name, time DESC;",

            "SELECT DISTINCT ON (S.station_name) S.station_name, S.id, P.type1_price, P.type2_price, P.type3_price, P.type4_price, P.time \
            FROM prices P, stations S \
            WHERE S.id = P.station_id AND P.visible = TRUE AND S.postnr = :search \
            ORDER BY S.station_name, time DESC;",
            
            "SELECT DISTINCT ON (S.station_name) S.station_name, S.id, P.type1_price, P.type2_price, P.type3_price, P.type4_price, P.time \
            FROM prices P, stations S \
            WHERE S.id = P.station_id AND P.visible = TRUE AND S.city = :search\
            ORDER BY S.station_name, time DESC;"]

get_all_prices = "SELECT S.station_name, S.id, P.type1_price, P.type2_price, P.type3_price, P.type4_price, P.time\
           FROM prices P, stations S\
           WHERE S.id = P.station_id\
           ORDER BY time DESC LIMIT 20;"

get_one_price = "SELECT id, station_id, (SELECT station_name FROM stations WHERE id = station_id) AS station, user_id, (SELECT username FROM users WHERE id = user_id) AS username, type1_price, type2_price, type3_price, type4_price, time, visible FROM prices WHERE id = :pid;"

get_avg_today = "SELECT ROUND(AVG(NULLIF(type1_price, 0.0))::numeric,3), \
                        ROUND(AVG(NULLIF(type2_price,0.0))::numeric,3), \
                        ROUND(AVG(NULLIF(type3_price, 0.0))::numeric,3), \
                        ROUND(AVG(NULLIF(type4_price, 0.0))::numeric,3), \
                        NOW() AT TIME ZONE 'Europe/Helsinki' as date \
                        FROM prices \
                        WHERE visible = TRUE AND date_trunc('day', time) = CURRENT_DATE;"

get_avg_daily = "SELECT ROUND(AVG(NULLIF(type1_price, 0.0))::numeric,3) AS type1_avg,\
                        ROUND(AVG(NULLIF(type2_price, 0.0))::numeric,3) AS type2_avg,\
                        ROUND(AVG(NULLIF(type3_price, 0.0))::numeric,3) AS type3_avg,\
                        ROUND(AVG(NULLIF(type4_price, 0.0))::numeric,3) AS type4_avg,\
                        date_trunc('day', time) AS date \
                        FROM prices WHERE visible = TRUE \
                        GROUP BY date_trunc('day', time) \
                        ORDER BY date DESC\
                        LIMIT 30;"

get_avg_monthly = "SELECT ROUND(AVG(NULLIF(type1_price, 0.0))::numeric,3) AS type1_avg, \
                    ROUND(AVG(NULLIF(type2_price, 0.0))::numeric,3) AS type2_avg, \
                    ROUND(AVG(NULLIF(type3_price, 0.0))::numeric,3) AS type3_avg, \
                    ROUND(AVG(NULLIF(type4_price, 0.0))::numeric,3) AS type4_avg, \
                    date_trunc('month', time) AS date\
                    FROM prices WHERE visible = TRUE \
                    GROUP BY date_trunc('month', time) \
                    ORDER BY date DESC\
                    LIMIT 24;"

is_admin = "SELECT COUNT(*)\
           FROM admin_users A, users U \
           WHERE A.user_id=U.id AND U.username=:username;"

is_user = "SELECT COUNT(*) FROM users WHERE username =:username;"

get_user_id = "SELECT id FROM users WHERE username =:username;"

is_banned = "SELECT visible FROM users WHERE username =:username;"

get_user_info = "SELECT id, username, visible, (SELECT COUNT(*) FROM prices WHERE user_id = :id) AS pricecount, (SELECT COUNT(*) FROM chat WHERE sender_id = :id) AS chatcount, joindate FROM users WHERE id = :id;"

get_password = "SELECT password FROM users WHERE username =:username;"

post_chat_message = "INSERT INTO chat (sender_id, message, time) VALUES (:username, :message, NOW() AT TIME ZONE 'Europe/Helsinki');"

#subquery for inverse order of messages
get_chat_messages = "SELECT * \
                  FROM (SELECT C.message, U.username, C.time AS time, U.id \
                        FROM chat C, users U \
                        WHERE U.id = C.sender_id AND U.visible = TRUE \
                        ORDER BY time DESC \
                        LIMIT 10) AS messages\
                ORDER BY messages.time ASC;"

get_requests = "SELECT id, sender_id, (SELECT username FROM users WHERE id = sender_id) AS name, message, date_trunc('day', time) AS date \
        FROM requests \
        WHERE visible = TRUE;"

add_request = "INSERT INTO requests (sender_id, message, visible, time) VALUES (:sender_id, :message, TRUE, NOW() AT TIME ZONE 'Europe/Helsinki');"

hide_request = "UPDATE requests SET visible=FALSE WHERE id=:request_id;"

get_areas = "SELECT DISTINCT city \
        FROM stations \
        WHERE operational = TRUE;"

get_roads = "SELECT DISTINCT road \
        FROM stations \
        WHERE operational = TRUE AND road != '0';"

get_postnrs = "SELECT DISTINCT postnr \
        FROM stations \
        WHERE operational = TRUE;"

get_station_info = "SELECT id, station_name, addr, postnr, city, road, operational \
        FROM stations \
        WHERE id = :station_id;"

get_station_prices = "SELECT id, user_id, date_trunc('day', time) AS date, type1_price, type2_price, type3_price, type4_price \
        FROM prices \
        WHERE station_id = :station_id AND visible = TRUE \
        ORDER BY date DESC, id DESC;"