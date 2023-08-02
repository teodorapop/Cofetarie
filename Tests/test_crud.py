from Domain.prajitura import create_prajitura, get_id
from Logic.crud import add_prajitura, delete_prajitura, get_by_id


def test_add_prajitura():

    prajituri = []
    p1 = create_prajitura(3, 'p1', 'yummy', 100, 500, 2019)
    add_prajitura(prajituri, 3, 'p1', 'yummy', 100, 500, 2019, 'test_add.txt')
    assert len(prajituri) == 1
    assert get_by_id(prajituri, 3) == p1
    p2 = create_prajitura(5, 'p2', 'yummier', 110, 300, 2021)
    add_prajitura(prajituri, 5, 'p2', 'yummier', 110, 300, 2021, 'test_add.txt')
    assert len(prajituri) == 2
    assert get_by_id(prajituri, 3) == p1
    assert get_by_id(prajituri, 5) == p2

def test_delete_prajitura():

    prajituri = []
    add_prajitura(prajituri, 3, 'p1', 'yummy', 100, 500, 2019, 'test_delete.txt')
    add_prajitura(prajituri, 5, 'p2', 'yummier', 110, 300, 2021, 'test_delete.txt')

    result = delete_prajitura(prajituri, 3, 'test_delete.txt')
    assert get_id(get_by_id(result, 5)) == 5
    assert get_by_id(result, 3) is None

    # nu stergem elementul din prajituri, lista aceea ramane la fel
    # result = delete_prajitura(prajituri, 3555)
    # assert get_id(get_by_id(result, 3)) == 3
    # assert get_id(get_by_id(result, 5)) == 5

