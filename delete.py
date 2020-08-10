import psycopg2



def delete(nationalCode):
    try:
        connection = psycopg2.connect(
            user= "postgres",
            password= "8610208400",
            host= "localhost",
            port= "5432",
            database="test"
        )

        cursor = connection.cursor()
        pg_delete =""" DELETE FROM public."customer" WHERE "nationalCode"= %s"""
        cursor.execute(pg_delete, (nationalCode, ))
        connection.commit()
        count = cursor.rowcount
        print("successfully deleted ", count, "rows")

    except(Exception, psycopg2.Error) as error:
        print("Error in deleting the data", error)
        connection = None

    finally:
        if connection !=None:
            cursor.close()
            connection.close()
            print ("postgresql connection is now closed")
