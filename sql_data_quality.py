check_time_dim = """SELECT COUNT(ti.*) as count
                    FROM dim_time ti"""

check_time_dim_distinct_date = """SELECT COUNT(DISTINCT ti.date) as count
                                  FROM dim_time ti"""

check_time_dim_all_data = """SELECT DISTINCT ti.date as date
                             FROM dim_time ti
                             MINUS
                                (SELECT DISTINCT i.arrival_date AS date
                                FROM immig_table i
                                UNION
                                SELECT DISTINCT i.departure_date AS date
                                FROM immig_table i
                                WHERE i.departure_date IS NOT NULL)"""

check_immig_fact = """SELECT count(i.*) as count
                      FROM fact_immigration i"""

check_immig_fact_distinct = """SELECT COUNT(DISTINCT i.city, i.state) as count
                               FROM fact_immigration i"""

check_immig_fact_distinct_cicid = """SELECT count(distinct i.cicid) as count
                                     FROM fact_immigration i"""

check_immig_fact_all_data = """SELECT COUNT(*) as count
                               FROM
                                  (
                                      SELECT DISTINCT i.city, i.state
                                      FROM fact_immigration i
                                      ) fi
                               INNER JOIN
                                  (
                                      SELECT DISTINCT a.municipality, a.state
                                      FROM dim_airports a
                                      ) da
                               ON fi.city = da.municipality
                               AND fi.state = da.state"""

check_immig_fact_all_data2 = """SELECT COUNT(*) as count
                                FROM
                                (
                                    SELECT DISTINCT i.city, i.state
                                    FROM fact_immigration i
                                    ) fi
                                INNER JOIN
                                (
                                    SELECT DISTINCT d.City, d.state_code
                                    FROM dim_demographics d
                                    ) da
                                ON fi.city = da.City
                                AND fi.state = da.state_code"""

check_immig_fact_all_data3 = """SELECT COUNT(*) as count
                                FROM fact_immigration
                                WHERE CONCAT(city, state) IN (
                                    SELECT CONCAT(fi.city, fi.state)
                                    FROM
                                    (
                                        SELECT DISTINCT city, state
                                        FROM fact_immigration
                                        ) fi
                                    INNER JOIN
                                    (
                                        SELECT DISTINCT municipality, state
                                        FROM dim_airports
                                        ) da
                                    ON fi.city = da.municipality
                                    AND fi.state = da.state
                                    )"""

check_demographics_dim = """SELECT count(d.*) as count
                            FROM dim_demographics d"""

check_demographics_dim_distinct = """SELECT COUNT(DISTINCT city, state, race) as count
                                 FROM dim_demographics"""

check_airports_dim = """SELECT count(*) as count
                        FROM dim_airports"""

check_airports_dim_distinct_ident = """SELECT COUNT(DISTINCT a.ident) as count
                                       FROM dim_airports a"""

check_temperature_dim = """SELECT count(te.*) as count
                           FROM dim_temperature te"""

check_temperature_dim_distinct = """SELECT COUNT(DISTINCT te.date, te.city) as count
                                    FROM dim_temperature te"""

