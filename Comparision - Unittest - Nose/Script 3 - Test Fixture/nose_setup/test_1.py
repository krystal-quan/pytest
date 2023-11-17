from nose.tools import with_setup
from conftest import set_up_session, tear_down_session, set_up_connection, tear_down_connection

@with_setup(set_up_session, tear_down_session)
def test_db_save(session):
    """Test db save"""
    print('######## running save')

@with_setup(set_up_session, tear_down_session)
def test_db_delete(session):
    """Test db deletion"""
    print('######## running delete')

def test_non_db():
    """Test non db"""
    print('######## non db test')