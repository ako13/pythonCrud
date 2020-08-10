import psycopg2

def update (nationalCode , customerName):
    try:
        connection = psycopg2.connect(
            user= "postgres",
            password= "8610208400",
            host= "localhost",
            port= "5432",
            database="test"
        )
        cursor = connection.cursor()

        print ("customer table befor updating ")
        pg_select = """ SELECT *FROM public."customer" WHERE "nationalCode"= %s"""
        cursor.execute(pg_select,(nationalCode, ))
        customr_record = cursor.fetchone()
        print (customr_record)

        pg_update = """Update public."customer" set "customerName"= %s WHERE "nationalCode"= %s"""
        cursor.execute(pg_update,(customerName,nationalCode))
        connection.commit()
        count = cursor.rowcount
        print (count , " successfully updated!")

        print("customer table after updating ")
        pg_select = """ SELECT *FROM public."customer" WHERE "nationalCode" = %s """

        cursor.execute(pg_select,(nationalCode, ))
        customer_record = cursor.fetchone()
        print (customer_record)


    except(Exception, psycopg2.Error) as error:
        print("Error in updating the data", error)
        connection = None


    finally:
        if connection !=None:
            cursor.close()
            connection.close()
            print ("postgresql connection is now closed")
