from abc import ABC, abstractmethod

class OrganizationManager(ABC):
    @abstractmethod
    def create():
        pass

    @abstractmethod
    def get_details():
        '''
            Read
        '''
        pass
    
    @abstractmethod
    def update():
        pass

    @abstractmethod
    def delete():
        pass

    @abstractmethod
    def sla():
        pass

    @abstractmethod
    def contract():
        pass


class ResearchSocietyOrganization(OrganizationManager):
    pass

class TechOrganization(OrganizationManager):
    pass

class AppraiserOrganization(OrganizationManager):
    pass

class CommercialOrganization(OrganizationManager):
    pass

class GlobalResearchOrganization(OrganizationManager):
    pass

class HumanResourceOrganization(OrganizationManager):
    pass

class FinancialOrganization(OrganizationManager):
    pass
