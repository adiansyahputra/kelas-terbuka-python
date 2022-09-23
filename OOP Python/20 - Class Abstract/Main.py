"""
abstract class
- merupakan blueprint dari class
- memaksa class untuk mengimplementasikan method
- tidak bisa untuk dibuat objectnya

class biasa
- merupakan blueprint dari object
- bebas boleh di gunakan untuk inheritance atau tidak
"""

# membuat abstract class --> import abc , abc = abstract base class
from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class PushButton(Button):

    def click(self):
        print(f"push button click")


class RadioButton(Button):

    def click(self):
        print(f"radio button click")


tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()
