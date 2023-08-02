from Domain.prajitura import get_nume, get_calorii, set_calorii, get_an_introducere, get_pret


def reducere_calorii_by_string(prajituri, string_de_cautare, reducere):
    '''

    :param prajituri:
    :param string_de_cautare:
    :param reducere:
    :return:
    '''

    for prajitura in prajituri:
        if string_de_cautare in get_nume(prajitura):
            calorii = get_calorii(prajitura) - reducere
            set_calorii(prajitura, calorii)


def get_praji_with_max_calorii_by_year(prajituri):
    '''

    :param prajituri:
    :return: un dictionar cu cheile fiind anii si valorile prajiturile cu nr ma de calorii din fiecare an
    '''

    result = {}
    for prajitura in prajituri:
        an = get_an_introducere(prajitura)
        if an in result:
            if get_calorii(prajitura) > get_calorii(result[an]):
                result[an] = prajitura
        else:
            result[an] = prajitura
    return result


def raport_pret_calitate(prajitura):
    '''

    :param prajitura:
    :return:
    '''

    raport = get_pret(prajitura) / get_calorii(prajitura)
    return raport


def get_prajituri_si_raport_pret_calitate(prajituri):
    '''

    :param prajituri:
    :return:
    '''
    result = {}
    for prajitura in prajituri:
        nume = get_nume(prajitura)
        result[nume] = raport_pret_calitate(prajitura)
    return result


def sumele_preturilor_pentru_fiecare_an(prajituri):
    '''

    :param prajituri:
    :return:
    '''

    result = {}
    for prajitura in prajituri:
        an = get_an_introducere(prajitura)
        if an in result:
            result[an] = result[an] + get_pret(prajitura)
        else:
            result[an] = get_pret(prajitura)
    return result
