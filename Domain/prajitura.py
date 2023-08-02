def create_prajitura(id, nume, descriere, pret, calorii, an_introducere):
    return {
        'id': id,
        'nume': nume,
        'descriere': descriere,
        'pret': pret,
        'calorii': calorii,
        'an_introducere': an_introducere
    }


def get_id(prajitura):
    return prajitura['id']


def get_nume(prajitura):
    return prajitura['nume']


def get_descriere(prajitura):
    return prajitura['descriere']


def get_pret(prajitura):
    return prajitura['pret']


def get_calorii(prajitura):
    return prajitura['calorii']


def set_calorii(prajitura, calorii):
    prajitura['calorii'] = calorii


def get_an_introducere(prajitura):
    return prajitura['an_introducere']


def to_str(prajitura):
    return f'Prajitura cu id {get_id(prajitura)} {get_nume(prajitura)} - {get_descriere(prajitura)[:25]}, ' \
           f'pretul = {get_pret(prajitura)} are {get_calorii(prajitura)} calorii, anul introducerii: ' \
           f'{get_an_introducere(prajitura)}'
