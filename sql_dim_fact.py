immig_i94mode = ('''SELECT i.*
                    FROM immig_table i
                    WHERE i.i94mode = 1''')

immig_city_code = ('''SELECT i.*, c.country AS citizenship_country
FROM immig_table i
INNER JOIN countryCodes c
ON i.i94cit = c.code''')

immig_res_code = ('''SELECT i.*, c.country AS residence_country
FROM immig_table i
INNER JOIN countryCodes c
ON i.i94res = c.code''')

immig_port_code = ('''SELECT i.*, p.location AS entry_port, p.state AS entry_port_state
FROM immig_table i 
INNER JOIN i94portCodes p
ON i.i94port = p.code''')

immig_age = ('''SELECT i.*,
                       (2016-i.biryear) AS age 
                FROM immig_table i''')

airport_US = ("""SELECT a.*
                 FROM airports a
                 WHERE a.iso_country IS NOT NULL
                 AND UPPER(TRIM(a.iso_country)) LIKE 'US'""")

airport_len = ("""SELECT a.*
                  FROM airports a
                  WHERE LOWER(TRIM(a.type)) NOT IN ('closed', 'heliport', 'seaplane_base', 'balloonport')
                  AND a.municipality IS NOT NULL
                  AND LENGTH(a.iso_region) = 5""")

immig_fact = ("""SELECT 
                            cicid, 
                            citizenship_country,
                            residence_country,
                            TRIM(UPPER (entry_port)) AS city,
                            TRIM(UPPER (entry_port_state)) AS state,
                            arrival_date,
                            departure_date,
                            age,
                            visa_type,
                            visatype AS detailed_visa_type

                 FROM immig_table """)

time_dim = ("""SELECT DISTINCT i.arrival_date AS date
               FROM immig_table i
               UNION
               SELECT DISTINCT i.departure_date AS date
               FROM immig_table i
               WHERE i.departure_date IS NOT NULL""")

time_extract_time_dim = ("""SELECT di.date,
                                   YEAR(di.date) AS year,
                                   MONTH(di.date) AS month,
                                   DAY(di.date) AS day,
                                   WEEKOFYEAR(di.date) AS week,
                                   DAYOFWEEK(di.date) as weekday, 
                                   DAYOFYEAR(di.date) year_day
                            FROM dim_time_table di
                            ORDER BY date ASC""")

temp_dim = ("""SELECT DISTINCT te.date,
                               te.city,
                               AVG(AverageTemperature) OVER (PARTITION BY te.date, te.City) AS average_temperature, 
                               AVG(AverageTemperatureUncertainty)  OVER (PARTITION BY te.date, te.City) AS average_termperature_uncertainty
               FROM temperature te""")

demographic_dim = ("""SELECT  de.City,
                              de.State, 
                              de.`Median Age` AS median_age, 
                              de.`Male Population` AS male_population, 
                              de.`Female Population` AS female_population, 
                              de.`Total Population` AS total_population, 
                              de.`Foreign-born` AS foreign_born, 
                              de.`Average Household Size` AS average_household_size, 
                              de.`State Code` AS state_code, 
                              de.Race, 
                              de.Count
                      FROM demographics de""")

airport_dim = ("""SELECT TRIM(ar.ident) AS ident,
                         ar.type,
                         ar.name,
                         ar.elevation_ft,
                         SUBSTR(ar.iso_region, 4) AS state,
                         TRIM(UPPER(ar.municipality)) AS municipality,
                         ar.iata_code
                  FROM airports ar""")