from errors.validation_error import ValidationError


class ValidatorTractor:
    def __init__(self):
        '''
        Initializarea.
        '''
        pass

    def validate(self,tractor):
        '''
        Metoda care valideaza tractor.
        :param tractor: tractor
        :return: raises ValidationError(errors) sau True
        '''
        errors = ""
        if tractor.get_tractor_id()<0:
            errors += "ID invalid."
        if tractor.get_tractor_denumire()=="":
            errors += "Denumire invalida"
        if tractor.get_tractor_pret()<0:
            errors += "Pret invalid."
        if tractor.get_tractor_model() =="":
            errors += "Model invalid."
        if len(errors)!=0:
            raise ValidationError(errors)
        return True