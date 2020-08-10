import psycopg2


def select ():
    try:
        connection = psycopg2.connect(
            user= "postgres",
            password= "8610208400",
            host= "localhost",
            port= "5432",
            database="test"
        )
        cursor = connection.cursor()
        pg_select = """ SELECT * FROM public."customer" """
        cursor.execute(pg_select)

        print ("select rows from book table ")
        book_records = cursor.fetchall()

        print ("records of books in the table")
        for row in book_records:
            print ("id = ", row[0])
            print ("customerName = ",row[1])
            print ("customerFamily = ",row[2])
            print ("nationalCode = ",row[3])
            print ("------------***--------------", "\n")


    except(Exception, psycopg2.Error) as error:
        print("Error selecting data from table book ", error)
        connection = None


    finally:
        if (connection):
            cursor.close()
            connection.close()
            print ("postgresql connection is now closed")