from errors.repository_error import RepositoryError
from errors.validation_error import ValidationError


class UI:
    def __init__(self,service_tractor):
        self.__service_tractor = service_tractor
        self.__commands = {
            "read_all_from_file":self.__ui_read_all_from_file,
            "print_all_tractoare":self.__ui_print_all_tractoare,
            "add_tractor":self.__ui_add_tractor,
            "delete_tractor":self.__ui_delete_tractor,
            "delete_tractor_by_given_decimal":self.__ui_delete_tractor_by_given_decimal,
            "filter_tractoare":self.__ui_filter_tractoare,
            "filter_tractoare_and_expired_revision":self.__ui_filter_tractoare_and_expired_revision,
            "undo":self.__ui_undo
        }

    def __ui_undo(self):
        if len(self.__params)!=0:
            print("Numar invalid de parametri!")
        else:
            self.__service_tractor.undo()

    def __ui_filter_tractoare_and_expired_revision(self):
        if len(self.__params)!=2:
            print("Numar invalid de parametri!")
        else:
            text=self.__params[0]
            numar = int(self.__params[1])
            lista_cu_revizia_expirata = self.__service_tractor.service_filtru_and_expired_revision(text,numar)
            lista_filtrata = self.__service_tractor.service_filtru(text,numar)
            if len(lista_filtrata)==0:
                print("Nu exista niciun tractor cu specificatiile date.")
            else:
                lista_noua=[]
                for tractor in lista_filtrata:
                    for revizuit in lista_cu_revizia_expirata:
                        if tractor.get_tractor_id() != revizuit.get_tractor_id():
                            lista_noua.append(tractor)
                for tractor in lista_noua:
                    print(tractor)
                for tractor in lista_cu_revizia_expirata:
                    print(f"*{tractor}")


    def __ui_filter_tractoare(self):
        if len(self.__params)!=2:
            print("Numar invalid de parametri!")
        else:
            text=self.__params[0]
            numar = int(self.__params[1])
            lista_filtered = self.__service_tractor.service_filtru(text,numar)
            if len(lista_filtered)==0:
                print("Nu exista niciun tractor cu specificatiile date.")
            else:
                for tractor in lista_filtered:
                    print(tractor)


    def __ui_delete_tractor_by_given_decimal(self):
        if len(self.__params)!=1:
            print("Numar invalid de parametri!")
        else:
            decimal = int(self.__params[0])
            contor = self.__service_tractor.service_delete_by_decimal(decimal)
            print(f"S-au sters {contor} tractoare.")


    def __ui_delete_tractor(self):
        if len(self.__params)!=1:
            print("Numar invalid de parametri!")
        else:
            id = int(self.__params[0])
            self.__service_tractor.service_delete_tractor_by_id(id)


    def __ui_add_tractor(self):
        if len(self.__params)!= 5:
            print("Numar invalid de parametri!")
        else:
            id = int(self.__params[0])
            denumire = self.__params[1]
            pret = int(self.__params[2])
            model = self.__params[3]
            data = self.__params[4]
            self.__service_tractor.service_add_tractor(id,denumire,pret,model,data)

    def __ui_print_all_tractoare(self):
        lista_tractoare = self.__service_tractor.service_print_all_tractoare()
        if len(lista_tractoare) == 0:
            print("Nu exista niciun tractor in repository.")
        else:
            for tractor in lista_tractoare:
                print(tractor)

    def __ui_read_all_from_file(self):
        self.__service_tractor.service_read_all_from_file()

    def run(self):

        #Aici facem consola de operare
        while True:
            command = input(">>>")
            command.strip()
            if command == "":
                continue
                #continua "sa fie True", in ciuda comenzii goale
            if command == "exit":
                return
                #programul iese din loop, proces terminat
            parts = command.split(",")
            command_name = parts[0]
            self.__params = parts[1:]
            if command_name in self.__commands:
                #daca numele de comanda este in dictionar, ca si cheie, atunci:
                try:
                    self.__commands[command_name]()
                except ValueError:
                    #arunca ValueError cand parametrii nu sunt ok, cred
                    print("UI Error: invalid numeric type!")
                except ValidationError as validation_errors:
                    print(f"Validation Error: {validation_errors}")
                except RepositoryError as repository_errors:
                    print(f"Repository Error: {repository_errors}")
            else:
                print("Invalid command!")