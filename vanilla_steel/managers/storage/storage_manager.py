from abc import ABC, abstractmethod

class StorageManager(ABC):
    @abstractmethod
    def upload():
        pass

    @abstractmethod
    def download():
        pass

    @abstractmethod
    def get_signed_url():
        pass


class B2Storage(StorageManager):
    pass

class S3Storage(StorageManager):
    pass

class GcsStorage(StorageManager):
    pass

class AzureStorage(StorageManager):
    pass

class MinioStorage(StorageManager):
    pass


class StorageFactory:
    def __init__(self):
        pass

    def create_storage(self, company_id):
        factory_name = self.get_used_storage_solution(company_id)
        match factory_name:
            case 'b2':
                return B2Storage
            case 's3':
                return S3Storage
            case 'gcs':
                return GcsStorage
            case 'azure':
                return AzureStorage
            case 'minio':
                return MinioStorage
            case _:
                raise('Not Implemented Error !')
        
    def get_used_storage_solution(self, company_id: str) -> str:
        print(company_id)
        return 'minio'
    
