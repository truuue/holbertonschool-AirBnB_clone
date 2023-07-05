#!/usr/bin/pyhon3
"""
Parent class that will inherit
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """Initializes all attributes
        """
        if not kwargs:  # Si aucun argument nommé n'a été passé
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()  # Permet de crée un nouvel objet
            # datetime représentant la date et l'heure actuelles, et l'assigne
            # à l'attribut created_at
            self.updated_at = self.created_at
            # donne la même valeur que created_at à l'attribut updated_at
        else:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    dataTime = "%Y-%m-%dT %H:%M:%S.%f"
                    val = datetime.strptime(kwargs[key], dataTime)
                    # Convertit la valeur de 'created_at' ou 'updated_at'
                    # en objet datetime en utilisant le format spécifié

                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        """
        method for named
        """
        nameClass = self.__class__.__name__
        return ("[{}] ({}) {}".format(nameClass, self.id, self.__dict__))

    def save(self):
        """updates last update time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns dict with all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
