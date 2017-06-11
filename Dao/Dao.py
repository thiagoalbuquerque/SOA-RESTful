import psycopg2
from abc import ABC, abstractmethod


class DAO(ABC):
    @property
    def get_connection(self):
        con = psycopg2.connect(host='localhost', database='Restful',
                               user='postgres', password='admin')
        return con

    @abstractmethod
    def insert(self, args):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def update(self, args):
        pass

    @abstractmethod
    def delete(self, args):
        pass