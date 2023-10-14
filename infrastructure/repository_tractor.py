from domain.tractor import Tractor
from errors.repository_error import RepositoryError


class RepositoryTractor:
    def __init__(self,access_way):
        '''
        Functia de initializare.
        :param access_way: str
        '''
        self.access_way = access_way
        self.__tractoare = {}


    def read_all_from_file(self):
        '''
        Functia cu care citim din fisier.
        :return: null
        '''
        with open(self.access_way,"r") as f:
            self.__tractoare.clear()
            lines = f.readlines()
            for line in lines:
                line.strip()
                if line != "" and line !="\n":
                    parts = line.split(",")
                    id = int(parts[0])
                    denumire = parts[1]
                    pret = int(parts[2])
                    model = parts[3]
                    data = parts[4]
                    tractor = Tractor(id,denumire,pret,model,data)
                    self.__tractoare[id] = tractor

    def write_all_to_file(self):
        '''
        Functia cu care scriem in fisier.
        :return: null
        '''
        with open(self.access_way, "w") as f:
            for tractor in self.__tractoare.values():
                f.write(tractor.__str__()+ "\n")

    def add_tractor(self,tractor):
        '''
        Functia CRUD cu care adaugam un tractor in fisier.
        :param tractor: tractor
        :return: null
        '''
        self.read_all_from_file()
        if tractor.get_tractor_id() in self.__tractoare:
            raise RepositoryError("Tractorul exista deja in repository.")
        self.__tractoare[tractor.get_tractor_id] = tractor
        self.write_all_to_file()



    def get_all_tractoare(self):
        '''
        Functia CRUD care returneaza lista cu tractoare.
        :return: lista_tractoare
        '''
        self.read_all_from_file()
        lista_tractoare = []
        for id_tractor in self.__tractoare:
            lista_tractoare.append(self.__tractoare[id_tractor])
        return lista_tractoare

    def search_tractor(self,id_tractor):
        '''
        Functia CRUD care returneaza un tractor dupa ID.
        :param id_tractor: int
        :return: tractor
        '''
        self.read_all_from_file()
        if id_tractor not in self.__tractoare:
            raise RepositoryError("Tractorul pe care incercati sa il cautati nu exista.")
        tractor = self.__tractoare[id_tractor]
        return tractor


    def delete_tractor(self,id_tractor):
        '''
        Functia CRUD care sterge un tractor dupa ID.
        :param id_tractor: int
        :return: null
        '''
        self.read_all_from_file()
        if id_tractor not in self.__tractoare:
            raise RepositoryError("Tractorul pe care incercati sa il stergeti nu exista.")
        del self.__tractoare[id_tractor]
        self.write_all_to_file()

