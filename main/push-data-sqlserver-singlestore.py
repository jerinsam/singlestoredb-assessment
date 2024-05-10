 
import singlestoredb
import pyodbc

## SQL SERVER CONNECTION ##
def sql_server_connect(pServer, pDb, pUserNm, pPwd):

    connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={pServer};DATABASE={pDb};UID={pUserNm};PWD={pPwd};encrypt=no;'
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor() 
    return cursor,conn

## SINGLE_STORE DB CONNECTION ##
def single_store_connect(pHost, pPort, pUser, pPassword, pDatabase):
  
    conn = singlestoredb.connect(host=pHost, port=pPort, user=pUser ,password= pPassword , database=pDatabase)
    cursor = conn.cursor()
    return cursor,conn

def mainFunc():

    ####### Read Data from Source #######

    sqlServer = '10.10.14.85'
    sqlServerDb = 'TRYIT'
    sqlServerUsername = 'js'
    sqlServerPassword = 'js'
    sqlServerQuery = "Select * from [dbo].[test_data_singlestore]"
    
    ## Connect to SQL Server ##
    sqlServerCursor, sqlServerConn = sql_server_connect(sqlServer, sqlServerDb, sqlServerUsername, sqlServerPassword) 
    
    ## Fetch SQL Server Data ##
    sqlServerCursor.execute(sqlServerQuery)
    sqlServerDataRows = sqlServerCursor.fetchall()
    
   

    # ## Print Data Rows: For Testing ##
    # for pt in sqlServerDataRows:
    #     print(pt)


    ####### Write Data to Destination #######
    singleStoreHost = '127.0.0.1'
    singleStorePort = '3306'
    singleStoreDb = 'test_ss'
    singleStoreUsername = 'root'
    singleStorePassword = 'jerin' 

    ## Connect to SingleStoreDB ##
    singleStoreCursor, singleStoreConn = single_store_connect(singleStoreHost,singleStorePort,singleStoreUsername,singleStorePassword,singleStoreDb)
    
    ## Truncate Table ##
    singleStoreCursor.execute('TRUNCATE TABLE test_dataload')

    ## Push Data to SingleStore ##
    for row in sqlServerDataRows:
        # print(type(row))
        singleStoreCursor.execute("INSERT INTO test_dataload VALUES (%s, %s)", list(row))

    ## Commit the Changes ##
    ## singleStoreCursor.commit() ---- Note** - SingleStore Auto Commits the inserted values.

    ##Close SingleStoreDB Connections and Curson ##
    singleStoreCursor.close()
    singleStoreConn.close()

    ## Close SQL Server Connection ##
    sqlServerCursor.close()
    sqlServerConn.close()

if __name__ == '__main__':
    mainFunc()