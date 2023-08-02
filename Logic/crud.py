from Domain.prajitura import create_prajitura, get_id
from Logic.file_ops import write_file


def get_by_id(prajituri, id_cautat):
    '''
    Gaseste o prajitura dupa id
    :param prajituri:
    :param id:
    :return: prajtura cu id-ul id sau None daca nu exista
    '''
    for prajitura in prajituri:
        if get_id(prajitura) == id_cautat:
            return prajitura
    return None


def add_prajitura(prajituri, id, nume, descriere, pret, calorii, an_introducere, filename):
    '''

    :param prajituri: lista de prajituri
    :param id:
    :param nume:
    :param descriere:
    :param pret:
    :param calorii:
    :param an_introducere:
    :return: ValueError daca id-ul nu este unic
    '''

    prajitura_existenta = get_by_id(prajituri, id)
    if prajitura_existenta is not None:
        raise ValueError('ID-ul exista deja')

    prajitura = create_prajitura(id, nume, descriere, pret, calorii, an_introducere)

    prajituri.append(prajitura)
    write_file(prajituri, filename)


def update_prajitura(prajituri, prajitura, filename):
    # v1
    # enumerate da tupluri de forma index valoare

    # for i, prajitura_existenta in enumerate(prajituri):
    #     if get_id(prajitura_existenta) == get_id(prajitura):
    #         prajituri[i] = prajitura
    #         break

    # v2
    result = [prajitura_existenta for prajitura_existenta in prajituri if
              get_id(prajitura) != get_id(prajitura_existenta)] + [prajitura]
    write_file(result, filename)
    return result

    # v3
    # delete_prajitura(prajituri, get_id(prajitura))
    # add_prajitura(...) dar sunt multi parametri


def delete_prajitura(prajituri, id_strgere, filename):
    '''
    Sterge o prajitura

    :param prajituri: lista de prajituri
    :param id_strgere: id-ul prajiturii pe care dorim sa o stergem
    :return: o noua lista din care va lipsi prajitura cu id-ul de sters
    :raises: ValueError daca id-ul nu exista
    '''
    prajitura_existenta = get_by_id(prajituri, id_strgere)
    if prajitura_existenta is None:
        raise ValueError('Prajitura cu acest id nu exista')
    #
    # varianta mea zic ca e buna si ea
    #
    # for prajitura in prajituri:
    #     if prajitura['id'] == id_strgere:
    #         prajituri.remove(prajitura)
    #         break

    rezultat = []
    for prajitura in prajituri:
        if get_id(prajitura) != id_strgere:
            rezultat.append(prajitura)
    write_file(prajituri, filename)
    return rezultat
