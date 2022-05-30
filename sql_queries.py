# DROP TABLES

from time import time


songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

"""
QUERY creating table "songplays" with
songplay_id;
start_time;
user_id reference from table ;
level;
song_id reference from table "songs";
artist_id;
session_id;
location;
user_agent
"""
songplay_table_create = ("""
    create table if not exists songplays (
        songplay_id serial, 
        start_time text references time(start_time), 
        user_id integer references users(user_id), 
        level text not null, 
        song_id text references songs(song_id), 
        artist_id text references artists(artist_id), 
        session_id integer not null, 
        location text not null, 
        user_agent text not null
        );
""")


"""
QUERY creating table "users" with
user_id;
first_name;
last_name;
gender;
level
"""
user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
        user_id integer PRIMARY KEY,
        first_name text NOT NULL,
        last_name text NOT NULL,
        gender text NOT NULL,
        level text NOT NULL
    );
""")


"""
QUERY creating table "songs" with
song_id;
title;
artist;
year;
duration
"""
song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
        song_id text PRIMARY KEY,
        title text NOT NULL,
        artist_id text NOT NULL,
        year integer NOT NULL,
        duration integer NOT NULL
    );
""")


"""
QUERY creating table "artists" with
artist_id,
name,
location,
latitude,
longitude
"""
artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists(
        artist_id text PRIMARY KEY,
        name text NOT NULL,
        location text NOT NULL,
        latitude numeric NOT NULL,
        longitude numeric NOT NULL
    );
""")


"""
QUERY creating table "time" with
start_time, 
hour,
day,
week,
month,
year
"""
time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time(
        start_time text PRIMARY KEY,
        hour integer NOT NULL,
        day integer NOT NULL,
        week integer NOT NULL,
        month integer NOT NULL,
        year integer NOT NULL,
        weekday integer NOT NULL
    );
""")

# INSERT RECORDS
"""
1. Insert songplay:
Query to insert corresponding data into table songplays.
"""
songplay_table_insert = ("""
    INSERT INTO songplays(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (default ,%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

"""
2. Insert users:
Query to insert corresponding data into table users. Also do not update data when insert same user_id
"""
user_table_insert = ("""
    INSERT INTO users(user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET LEVEL = EXCLUDED.level;
""")

"""
3. Insert songs:
Query to insert corresponding data into table songs. Also do not update data when insert same song_id
"""
song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

"""
4. Insert artist:
Query to insert corresponding data into table artists. Also do not update data when insert same artist_id
"""
artist_table_insert = ("""
    INSERT INTO artists(artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")

"""
4. Insert time:
Query to insert corresponding data into table time. Also do not update data when insert same start_time
"""
time_table_insert = ("""
    INSERT INTO time(start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id, artists.artist_id
    FROM songs
    INNER JOIN artists ON artists.artist_id = songs.artist_id
    where
        songs.title = %s and
        artists.name = %s and
        songs.duration = %s
    """)

# QUERY LISTS

create_table_queries = [artist_table_create, song_table_create, time_table_create, user_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]