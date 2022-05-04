create_airports = """
CREATE TABLE IF NOT EXISTS public.airports (
    iata_code    VARCHAR PRIMARY KEY,
    name         VARCHAR,
    type         VARCHAR,
    local_code   VARCHAR,
    coordinates  VARCHAR,
    city         VARCHAR,
    elevation_ft FLOAT,
    continent    VARCHAR,
    iso_country  VARCHAR,
    iso_region   VARCHAR,
    municipality VARCHAR,
    gps_code     VARCHAR
);
"""

create_temperature = """
CREATE TABLE IF NOT EXISTS temperature (
    timestamp                      DATE,
    average_temperature            FLOAT,
    average_temperature_uncertainty FLOAT,
    city                           VARCHAR,
    country                        VARCHAR,
    latitude                       VARCHAR,
    longitude                      VARCHAR
);
"""

create_demographics = """
CREATE TABLE IF NOT EXISTS public.demographics (
    city                   VARCHAR,
    state                  VARCHAR,
    media_age              FLOAT,
    male_population        numeric,
    female_population      numeric,
    total_population       numeric,
    num_veterans           numeric,
    foreign_born           numeric,
    average_household_size FLOAT,
    state_code             VARCHAR(2),
    race                   VARCHAR,
    count                  numeric
);
"""

create_immigrations = """
CREATE TABLE IF NOT EXISTS public.immigrations (
    cicid    FLOAT PRIMARY KEY,
    year     FLOAT,
    month    FLOAT,
    cit      FLOAT,
    res      FLOAT,
    iata     VARCHAR(3),
    arrdate  FLOAT,
    mode     FLOAT,
    addr     VARCHAR,
    depdate  FLOAT,
    bir      FLOAT,
    visa     FLOAT,
    count    FLOAT,
    dtadfile VARCHAR,
    entdepa  VARCHAR(1),
    entdepd  VARCHAR(1),
    matflag  VARCHAR(1),
    biryear  FLOAT,
    dtaddto  VARCHAR,
    gender   VARCHAR(1),
    airline  VARCHAR,
    admnum   FLOAT,
    fltno    VARCHAR,
    visatype VARCHAR
);
"""


airport_insert = """
INSERT INTO airports (iata_code, name, type, local_code, coordinates, city, elevation_ft, continent, \
    iso_country, iso_region, municipality, gps_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (iata_code) DO NOTHING"""


demographic_insert = """
INSERT INTO demographics (city, state, media_age, male_population, female_population, total_population, \
num_veterans, foreign_born, average_household_size, state_code, race, count) VALUES (%s, %s, %s, %s, \
%s, %s, %s, %s, %s, %s, %s, %s)"""


immigration_insert = ("""
INSERT INTO immigrations (cicid, year, month, cit, res, iata, arrdate, mode, addr, depdate, bir, visa, count, dtadfile, \
entdepa, entdepd, matflag, biryear, dtaddto, gender, airline, admnum, fltno, visatype) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")


temperature_insert = ("""
INSERT INTO temperature (timestamp, average_temperature, average_temperature_uncertainty, city, country, \
latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s)""")


drop_temperature = "DROP TABLE IF EXISTS weather;"
drop_airports = "DROP TABLE IF EXISTS airports;"
drop_immigrations = "DROP TABLE IF EXISTS immigrations;"
drop_demographics = "DROP TABLE IF EXISTS demographics;"


drop_table_queries = [drop_immigrations, drop_temperature, drop_airports, drop_demographics]
create_table_queries = [create_immigrations, create_temperature, create_airports, create_demographics]
