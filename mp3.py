
from win32com.client import Dispatch
def speak(str):
     spk=Dispatch('SAPI.spvoice')
     spk.speak(str)
speak(input("enter yur name"))



