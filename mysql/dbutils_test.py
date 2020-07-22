from threading import Thread

from datetime import datetime

import time

import pymysql

from DBUtils.PooledDB import PooledDB


# Definition of CrawlInfo

class CrawlInfo:

    def __init__(self, url_in, header_in, body_in, lastVisit_in):
        self.url = url_in

        self.header = header_in

        self.body = body_in

        self.lastVisit = lastVisit_in


# The thread function for MySQL Insert

# This thread will insert records into MySQL table using the connections

# from connection pool

def MySQLInsertThread(threadNum_in, dbConnection_in, crawlInfo_in):
    try:

        print("Thread{} started".format(threadNum_in))

        url = crawlInfo_in.url

        header = crawlInfo_in.header

        body = crawlInfo_in.body

        lastVisit = crawlInfo_in.lastVisit

        # SQL statement to insert into a MySQL database table

        sqlInsert = "INSERT INTO crawled values ('{}','{}','{}','{}')".format(url, header, body, lastVisit)

        # Obtain a cursor object

        mySQLCursor = dbConnection_in.cursor()

        # Execute the SQL stament

        mySQLCursor.execute(sqlInsert)

        # Close the cursor and connection objects

        mySQLCursor.close()

        dbConnection_in.close()

        print("Thread{} exiting".format(threadNum_in))



    except Exception as e:

        print("Exception: %s" % e)

    return


# Information required to create a connection object

dbServerIP = "127.0.0.1"  # IP address of the MySQL database server

dbUserName = "root"  # User name of the MySQL database server

dbUserPassword = ""  # Password for the MySQL database user

databaseToUse = "TestDatabase"  # Name of the MySQL database to be used

charSet = "utf8mb4"  # Character set

cusrorType = pymysql.cursors.DictCursor

Crawl_Info_Count = 10

mySQLConnectionPool = PooledDB(creator=pymysql,
                               # Python function returning a connection or a Python module, both based on DB-API 2

                               host=dbServerIP,

                               user=dbUserName,

                               password=dbUserPassword,

                               database=databaseToUse,

                               autocommit=True,

                               charset=charSet,

                               cursorclass=cusrorType,

                               blocking=False,

                               maxconnections=Crawl_Info_Count)

threadCollection = []

crawlInfoCollection = []

# Create data to insert data into MySQL table

for i in range(Crawl_Info_Count):
    url = "url" + str(i)

    header = "header" + str(i)

    body = "body" + str(i)

    lastVisit = time.strftime('%Y-%m-%d %H:%M:%S')

    crawlInfoCollection.append(CrawlInfo(url, header, body, lastVisit))

# Create threads to insert data into MySQL table


for i in range(Crawl_Info_Count):
    mySQLConnection = mySQLConnectionPool.connection()

    t = Thread(target=MySQLInsertThread, args=(i, mySQLConnection, crawlInfoCollection[i]))

    threadCollection.append(t)

    # Start the db insert thread

    t.start()

    print("Number of database connections in use:{}".format(mySQLConnectionPool._connections))

# Proceed once the other threads are complete

for thread in threadCollection:
    thread.join()