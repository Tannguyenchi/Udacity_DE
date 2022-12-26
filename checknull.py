def Check(spark_test, tables):
    """
    This function performs null value checks on specific columns of the table.
    Parameters:
        - spark_test: spark context where data quality checks will be performed
        - table: Dictionary containing pairs (tables, columns) specifying for each table, which columns should be checked for null values.
    """  
    for table in tables:
        print(f"Data quality check on table {table} starting...")
        for column in tables[table]:
            sql = f"""SELECT COUNT(*) as nbr FROM {table} WHERE {column} IS NULL"""
            returnedVal = spark_test.sql(sql)
            if returnedVal.head()[0] > 0:
                raise ValueError(f"Data quality check failed! Found NULL values in {column} column!")
        print(f"Table {table} passed.")