#!/usr/bin/python3
"""BaseModel module for AirBnB clone.
    Defines all commmon attribute/methods for other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all AirBnB models."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel Instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return the string represention of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute
        updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all key/values
        of __dict__ of the instance.
        """
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
        return res
