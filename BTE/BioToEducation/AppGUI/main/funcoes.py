import flet as ft
import os 
import sys 
import layout
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


if root_dir not in sys.path:
    sys.path.append(root_dir)
    
from dataNAlgoritm.algoritm import mainAlgoritm



