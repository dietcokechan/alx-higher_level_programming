#!/usr/bin/python3
"""class definition for locked class"""


class LockedClass:
    """prevent user from dynamically creating new instance attr,
    except if the new instance attr is called first_name
    
    Attributes:
        first_name (str): first name"""


    __slots__ = ["first_name"]

    def __init__(self):
        """initialize class"""
        self.first_name = "first_name"
