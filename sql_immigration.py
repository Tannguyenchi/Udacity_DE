# Select count distinct cicid columns in immig table
count_dist_cicid = '''SELECT COUNT (DISTINCT i.cicid) as count
                      FROM immig_table i'''

# Select length word in i94port column in immig table
length_character = '''SELECT LENGTH (i.i94port) AS len
                      FROM immig_table i
                      GROUP BY len'''

#
compute_arrival_date = '''SELECT *,
                          date_add(to_date('1960-01-01'), i.arrdate) AS arrival_date 
                          FROM immig_table i'''

# Replace data for i94visa columns
replace_data_visa = '''SELECT *, 
                        CASE 
                        WHEN i.i94visa = 1.0 THEN 'Business' 
                        WHEN i.i94visa = 2.0 THEN 'Pleasure'
                        WHEN i.i94visa = 3.0 THEN 'Student'
                        ELSE 'N/A' END AS visa_type
                       FROM immig_table i'''

# Replace data for depdate columns
replace_data_depdate = '''SELECT *,
                                 CASE 
                                 WHEN i.depdate >= 1.0 THEN date_add(to_date('1960-01-01'), i.depdate)
                                 WHEN i.depdate IS NULL THEN NULL
                                 ELSE 'N/A' END AS departure_date
                          FROM immig_table i'''

# Check the results
check_NA = "SELECT count(*) as count FROM immig_table i WHERE i.departure_date = 'N/A'"

check_DD_AD = '''SELECT COUNT(*) as count
                 FROM immig_table i
                 WHERE i.departure_date <= i.arrival_date'''
check_arr_dep = '''SELECT i.arrival_date, i.departure_date
                   FROM immig_table i
                   WHERE i.departure_date <= i.arrival_date'''
check_AD_DD = '''SELECT *
                 FROM immig_table i
                 WHERE i.departure_date >= i.arrival_date'''

# Check distinct departure dates
check_dep = '''SELECT COUNT (DISTINCT i.departure_date) as count
               FROM immig_table i'''

# Check distinct arrival dates
check_arr = '''SELECT COUNT (DISTINCT i.arrival_date) as count
               FROM immig_table i'''

# Check the common values between the two sets
check_common = '''SELECT COUNT(DISTINCT i.departure_date) as count
                  FROM immig_table i
                  WHERE i.departure_date IN (
                                SELECT DISTINCT i.arrival_date
                                FROM immig_table i
                )'''

# Check the data for the various arrival modes
check_mode = '''SELECT i.i94mode,
                       count(*)
                FROM immig_table i 
                GROUP BY i.i94mode'''

# Check missing values in the age columns
check_age = '''SELECT COUNT(*) as count
               FROM immig_table i
               WHERE i.i94bir IS NULL'''

check_bir = '''SELECT COUNT(i.biryear) as count
               FROM immig_table i
               WHERE i.biryear IS NULL'''

check_biryear = '''SELECT MAX(i.biryear),
                          MIN(i.biryear)
                   FROM immig_table i
                   WHERE i.biryear IS NOT NULL'''

check_biryear_age = '''SELECT COUNT(*) as count
                       FROM immig_table i
                       WHERE i.biryear IS NOT NULL
                       AND i.biryear <= 1936'''
check_fre_biryear = '''SELECT i.biryear,
                              COUNT(*) as count
                       FROM immig_table i
                       WHERE i.biryear IS NOT NULL
                       AND i.biryear <= 1936
                       GROUP BY i.biryear
                       ORDER BY i.biryear ASC'''
check_age_bir = '''SELECT (2016-i.biryear)-i.i94bir AS difference,
                            count(*)  as count
                    FROM immig_table i
                    WHERE i.i94bir IS NOT NULL
                    GROUP BY difference'''
check_gender = '''SELECT i.gender,
                         count(*) as count
                  FROM immig_table i
                  GROUP BY i.gender'''
select_gender = '''SELECT *
                   FROM immig_table i
                   WHERE i.gender IN ('F', 'M')'''

# Check citizenship and residence data
check_cit_null = '''SELECT count(*) as count
                    FROM immig_table i
                    WHERE i.i94cit IS NULL'''

check_res_null = '''SELECT count(*) as count
                    FROM immig_table i
                    WHERE i.i94res IS NULL'''

check_addr_null = '''SELECT count(*) as count
                     FROM immig_table i
                     WHERE i.i94addr IS NULL'''

check_visa_null  = '''SELECT COUNT(*) as count
                      FROM immig_table i
                      WHERE i.visatype IS NULL'''
check_all_visa = '''SELECT i.visa_type,
                           i.visatype,
                           count(*) as count
                    FROM immig_table i
                    GROUP BY i.visa_type, i.visatype
                    ORDER BY i.visa_type, i.visatype'''
check_occup = '''SELECT i.occup, COUNT(*) as n
                 FROM immig_table i
                 GROUP BY i.occup
                 ORDER BY n DESC, i.occup'''

# Check all data
check_all = '''SELECT * FROM immig_table'''