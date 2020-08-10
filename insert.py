import psycopg2


def insert(customerName, customerFamily, nationalCode):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="8610208400",
            host="localhost",
            port="5432",
            database="test"
        )

        cursor = connection.cursor()

        pg_insert = """ INSERT INTO public."customer"(
                    "customerName","customerFamily","nationalCode")
                    VALUES (%s,%s,%s) """
        inserted_values = (
            customerName,
            customerFamily,
            nationalCode,
        )

        cursor.execute(pg_insert, inserted_values)
        connection.commit()

    except(Exception, psycopg2.Error) as error:
        print("Error connecting to postgresql database", error)
        connection = None

    finally:
        if (connection):
                cursor.close()
                connection.close()
                print("the postgresql connection is now closed ")
