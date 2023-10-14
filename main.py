from infrastructure.repository_tractor import RepositoryTractor
from business.service_tractoare import ServiceTractor
from validation.validator_tractor import ValidatorTractor
from presentation_layer.UI import UI

def main():
    access_way = "tractor.txt"
    repository_tractor = RepositoryTractor(access_way)
    validator_tractor = ValidatorTractor()
    service_tractor = ServiceTractor(repository_tractor,validator_tractor)
    console= UI(service_tractor)
    console.run()

main()