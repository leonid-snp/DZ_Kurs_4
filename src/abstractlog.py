from abc import ABC, abstractmethod


class AbstractLog(ABC):

    @abstractmethod
    def __str__(self):
        """
           Функция строкового отображения класса
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        Функция подсчета количество продуктов
        """
        pass

    @abstractmethod
    def product(self):
        """
        Функция отображения продукта
        """
        pass
