from abc import  abstractmethod


class ActionsDataBase:

    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass

    @abstractmethod
    def select(self, obj):
        pass
