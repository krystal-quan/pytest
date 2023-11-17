param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

def test_generator():
    for params in param_list:
        yield check_em, params[0], params[1]

def check_em(a, b):
    assert a == b