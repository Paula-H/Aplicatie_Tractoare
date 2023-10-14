from domain.tractor import Tractor
from datetime import date


class ServiceTractor:
    def __init__(self,repository_tractor,validator_tractor):
        '''
        Metoda de initializare.
        :param repository_tractor: repository_tractor(clasa)
        :param validator_tractor: validator_tractor(clasa
        '''
        self.__repository_tractor = repository_tractor
        self.__validator_tractor = validator_tractor
        self.__last_repository = []

    def service_read_all_from_file(self):
        '''
        Metoda care acceseaza repo-ul pentru citirea din fisier.
        :return: null
        '''
        self.__repository_tractor.read_all_from_file()


    def service_print_all_tractoare(self):
        '''
        Metoda care returneaza lista cu toate tractoarele din repository.
        :return: lista
        '''
        self.__last_repository.clear()
        self.__last_repository.append(self.__repository_tractor.get_all_tractoare())
        return self.__repository_tractor.get_all_tractoare()

    def service_add_tractor(self,id,denumire,pret,model,data):
        '''
        Metoda care acceseaza validator si repository pentru a introduce un nou tractor in fisier.
        :param id: int
        :param denumire: str
        :param pret: int
        :param model: str
        :param data: str
        :return: null
        '''
        self.__last_repository.clear()
        self.__last_repository.append(self.__repository_tractor.get_all_tractoare())
        tractor = Tractor(id, denumire, pret, model, data)
        self.__validator_tractor.validate(tractor)
        self.__repository_tractor.add_tractor(tractor)

    def service_delete_tractor_by_id(self,id):
        '''
        Metoda care, prin accesarea repository-ului,sterge un tractor din fisier dupa ID.
        :param id: int
        :return:
        '''
        self.__repository_tractor.delete_tractor(id)

    def service_delete_by_decimal(self,decimal):
        '''
        Metoda care sterge un tractor daca printre cifrele pretului acestuia se afla decimal; returneaza contorul pentru
        afisarea din UI.
        :param decimal: int
        :return: contor
        '''
        self.__last_repository.clear()
        self.__last_repository.append(self.__repository_tractor.get_all_tractoare())
        def cauta_cifra(x,decimal):
            while x>0:
                ultima_cifra = x%10
                x = x//10
                if ultima_cifra==decimal:
                    return True
            return False
        lista_tractoare = self.__repository_tractor.get_all_tractoare()
        contor = 0
        for tractor in lista_tractoare:
            pret = tractor.get_tractor_pret()
            if cauta_cifra(pret,decimal) == True:
                id_tractor = tractor.get_tractor_id()
                self.__repository_tractor.delete_tractor(id_tractor)
                contor += 1
        return contor

    def service_filtru(self,text,numar):
        '''
        Metoda care filtreaza lista de tractoare dupa denumire si dupa pret,returnand in final lista filtrata.
        :param text: str
        :param numar: int
        :return: lista_filtrata
        '''
        numar = int(numar)
        lista_filtrata = []
        lista_tractoare = self.__repository_tractor.get_all_tractoare()
        if text != "" and numar!=-1:
            for tractor in lista_tractoare:
                if tractor.get_tractor_denumire()==text and tractor.get_tractor_pret() == numar:
                    lista_filtrata.append(tractor)

        if text == "" and numar != -1:
            for tractor in lista_tractoare:
                if tractor.get_tractor_pret() == numar:
                    lista_filtrata.append(tractor)

        if text != "" and numar == -1:
            for tractor in lista_tractoare:
                if tractor.get_tractor_denumire() == text:
                    lista_filtrata.append(tractor)
        return lista_filtrata

    def service_filtru_and_expired_revision(self,text,numar):
        '''
        Metoda care filtreaza lista de tractoare dupa denumire si dupa pret,returnand in final doar lista cu revizia
        expirata.
        :param text: str
        :param numar: int
        :return: lista_filtrata
        '''
        todays_date = str(date.today())

        lista_filtrata = self.service_filtru(text,numar)

        lista_cu_revizia_expirata = []
        for tractor in lista_filtrata:
            data_revizie = str(tractor.get_tractor_data())
            if todays_date[0:4]> data_revizie[6:10]:
                lista_cu_revizia_expirata.append(tractor)
            if todays_date[0:4] == data_revizie[6:10]:
                if todays_date[5:7]>data_revizie[3:5]:
                    lista_cu_revizia_expirata.append(tractor)
                if todays_date[5:7] == data_revizie[3:5]:
                    if todays_date[8:10]> data_revizie[0:2]:
                        lista_cu_revizia_expirata.append((tractor))

        return lista_cu_revizia_expirata

    def undo(self):
        '''
        Metoda de undo. Scrie in fisier.
        :return:
        '''
        last_repository =  self.__last_repository[0]
        with open(self.__repository_tractor.access_way, "w") as f:
            for tractor in last_repository:
                f.write(tractor.__str__() + "\n")




