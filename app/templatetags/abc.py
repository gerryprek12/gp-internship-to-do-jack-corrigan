"""
This file contains a helper function that allowed Priority to be handled properly.
It is used to access the PRIORITY_OPTIONS dictionary and return the key for a specified value
"""

from django import template

register = template.Library()

def element(bar,value):
    return bar[value]

register.filter("element",element)