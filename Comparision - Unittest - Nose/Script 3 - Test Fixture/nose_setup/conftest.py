from setup_classes import Session, Connection


def set_up_session():
    s = Session()
    return s
    
def tear_down_session(s):
    s.close()



def set_up_connection():
    conn = Connection()
    return conn
    
def tear_down_connection(conn):
    conn.close()