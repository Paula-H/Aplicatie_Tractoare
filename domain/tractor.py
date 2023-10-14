class Tractor:
    def __init__(self,id,denumire,pret,model,data):
        '''
        Functia de initializare.
        :param id: int
        :param denumire: str
        :param pret: int
        :param model: str
        :param data: str
        '''
        self.__id = int(id)
        self.__denumire = denumire
        self.__pret = int(pret)
        self.__model = model
        self.__data = data

    def get_tractor_id(self):
        '''
        Getter care returneaza id-ul tractorului.
        :return: self.__id
        '''
        return self.__id

    def get_tractor_pret(self):
        '''
        Getter care returneaza pretul tractorului.
        :return: self.__pret
        '''
        return self.__pret

    def get_tractor_denumire(self):
        '''
        Getter care returneaza denumirea tractorului.
        :return: self.__denumire
        '''
        return self.__denumire

    def get_tractor_model(self):
        '''
        Getter care returneaza modelul tractorului.
        :return: self.__model
        '''
        return self.__model

    def get_tractor_data(self):
        '''
        Getter care returneaza data de expirare a reviziei a tractorului.
        :return: self.__data
        '''
        return self.__data

    def __str__(self):
        '''
        Functia de afisare.
        :return: string
        '''
        return f"{self.__id},{self.__denumire},{self.__pret},{self.__model},{self.__data}"