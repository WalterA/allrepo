from configparser import ConfigParser
import psycopg2

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db

conn = None

def connect():
    """ Connect to the PostgreSQL database server """
    global conn
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        return cur
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

def write_in_db(cur, sql_insert):
    global conn
    try:
        cur.execute(sql_insert)
        conn.commit()
        return 0
    except (Exception, psycopg2.DatabaseError) as error:
        sError = str(error)
        if sError.startswith("duplicate key value "):
            print("Duplicate key, vado avanti")
            conn.rollback()
            return -2
        print(sError)
        return -1

def read_in_db(cur, sql_select):
    try:
        cur.execute(sql_select)
        return cur.rowcount
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return -1

def read_next_row(cur):
    try:
        row = cur.fetchone()
        return True, row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False, None

def close(cur):
    global conn
    try:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
