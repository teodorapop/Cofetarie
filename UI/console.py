from Domain.prajitura import to_str, get_id, create_prajitura, get_nume, get_descriere, get_pret, get_calorii, \
    get_an_introducere
from Logic.crud import add_prajitura, delete_prajitura, update_prajitura, get_by_id
from Logic.file_ops import write_file
from Logic.operations import reducere_calorii_by_string, get_praji_with_max_calorii_by_year, \
    sumele_preturilor_pentru_fiecare_an, get_prajituri_si_raport_pret_calitate


def print_menu():
    print('1. CRUD - Create, Read, Update, Delete')
    print('2. Operatii')
    print('u. Undo')
    print('x. Iesire')


def run_crud(prajituri, undo_list):
    def handle_adaugare(prajituri, undo_list):
        try:
            id = input('Dati id-ul: ')
            nume = input('Dati numele: ')
            descriere = input('Dati descrierea: ')
            pret = float(input('Dati pretul: '))
            calorii = int(input('Dati caloriile: '))
            an_introducere = int(input('Dati anul introducerii: '))

            before_add = prajituri[:]  # s ar putea sa fie nevoie de deepcopy in unele cazuri
            add_prajitura(prajituri, id, nume, descriere, pret, calorii, an_introducere, 'prajituri.txt')

            undo_list.append(before_add)

            print('Prajitura a fost adaugata!')
        except ValueError as ve:
            print('Eroare: ', ve, ', reincearca!')

    def handle_stergere(prajituri, undo_list):
        try:
            id_stergere = input("Dati id-ul prajiturii de sters: ")

            # variabila locala, nu modifica prajiturile date ca parametru
            new_prajituri = delete_prajitura(prajituri, id_stergere, 'prajituri.txt')

            undo_list.append(prajituri)  # deepcopy unele cazuri
            prajituri = new_prajituri
            print('Prajitura a fost stearsa.')
        except ValueError as ve:
            print('Eroare: ', ve, ', reincearca!')
        return prajituri

    def handle_modificare(prajituri, undo_list):
        id = input('Dati id-ul: ')
        prajitura_existenta = get_by_id(prajituri, id)

        nume = input('Dati numele sau lasati gol pt a nu se schimba: ')
        if nume == '':
            nume = get_nume(prajitura_existenta)

        descriere = input('Dati descrierea sau lasati gol: ')
        if descriere == '':
            descriere = get_descriere(prajitura_existenta)

        pret = input('Dati pretul sau lasati gol: ')
        if pret == '':
            pret = get_pret(prajitura_existenta)
        else:
            pret = float(pret)

        calorii = input('Dati caloriile sau lasati gol: ')
        if calorii == '':
            calorii = get_calorii(prajitura_existenta)
        else:
            calorii = int(calorii)

        an_introducere = input('Dati anul introducerii sau lasati gol: ')
        if an_introducere == '':
            an_introducere = get_an_introducere(prajitura_existenta)
        else:
            an_introducere = int(an_introducere)

        prajitura_noua = create_prajitura(id, nume, descriere, pret, calorii, an_introducere)
        prajituri = update_prajitura(prajituri, prajitura_noua, 'prajituri.txt')

        print('Prajitura a fost modificata!')

        return prajituri

    def handle_show_all(prajituri):
        for p in prajituri:
            print(to_str(p))

    while True:
        print('1. Adaugare')
        print('2. Stergere')
        print('3. Modificare')
        print('a. Afisare toate')
        print('b. Back')
        op = input('Alegeti optiunea: ')
        if op == '1':
            handle_adaugare(prajituri, undo_list)
        elif op == '2':
            prajituri = handle_stergere(prajituri, undo_list)
        elif op == '3':
            prajituri = handle_modificare(prajituri, undo_list)
        elif op == 'a':
            handle_show_all(prajituri)
        elif op == 'b':
            break
        else:
            print('Optiune invalida !')
    return prajituri


def run_operatii(prajituri):
    def handle_reducere_calorii(prajituri):
        string_dat = input('Dati stringul de cautare: ')
        reducere = float(input('Reducere: '))

        reducere_calorii_by_string(prajituri, string_dat, reducere)

    def handle_prajituri_incepand_cu_an_dat(prajituri):
        an = int(input('Dati anul: '))
        for prajitura in prajituri:
            if int(get_an_introducere(prajitura)) >= an:
                print(to_str(prajitura))

    def handle_calorii_maxime_per_an(prajituri):
        rezultat = get_praji_with_max_calorii_by_year(prajituri)
        # ia fiecare cheie din anul rezultat
        for an in rezultat:
            print('Prajitura cu caloriile maxime din anul {} este: {}'.format(an, get_nume(rezultat[an])))

    def handle_ordonare_prajituri_dupa_raport_pret_calorii(prajituri):
        rezultat = get_prajituri_si_raport_pret_calitate(prajituri)
        sorted_rezultat = sorted(rezultat.items(), key=lambda x: x[1])
        for nume, raport in sorted_rezultat:
            print('Prajitura {} are raportul pret/calorii: {}'.format(nume, raport))

    def handle_sumele_preturilor_pentru_fiecare_an(prajituri):

        rezultat = sumele_preturilor_pentru_fiecare_an(prajituri)

        sorted_rezultat = sorted(rezultat.items(), key=lambda x: x[0])

        for an, suma in sorted_rezultat:
            print('In anul {} suma preturilor este {}'.format(an, suma))


    while True:
        print('1. Reducere calorii')
        print('2. Afisare prajituri incepand cu un an dat')
        print('3. Afisare cu calorii maxime per an')
        print('4. Afisare ordonate dupa raport pret / calorii')
        print('5. Afisarea sumei preturilor pentru fiecare an')
        print('b. Back')
        op = input('Alegeti optiunea: ')
        if op == '1':
            handle_reducere_calorii(prajituri)
        elif op == '2':
            handle_prajituri_incepand_cu_an_dat(prajituri)
        elif op == '3':
            handle_calorii_maxime_per_an(prajituri)
        elif op == '4':
            handle_ordonare_prajituri_dupa_raport_pret_calorii(prajituri)
        elif op == '5':
            handle_sumele_preturilor_pentru_fiecare_an(prajituri)
        elif op == 'b':
            break
        else:
            print('Optiune invalida !')


def run_undo(undo_list):
    if len(undo_list) > 0:
        return undo_list


def run_console(prajituri, undo_list):
    while True:
        print_menu()
        op = input('Alegeti optiunea: ')

        if op == '1':
            prajituri = run_crud(prajituri, undo_list)
        elif op == '2':
            run_operatii(prajituri)
        elif op == 'u':
            undone = run_undo(undo_list)
            if undone is not None:
                prajituri = undone
                write_file(prajituri)  # TODO mutata pe logic
        elif op == 'x':
            break
        else:
            print('Optiune invalida !')
    return prajituri
