from dataclasses import dataclass

@dataclass
class Elektrogeraete():
    marke : str =""
    baujahr : int = 1900
    preis:  int = 0
      
    def power_on():
        pass
    
@dataclass
class Hifigerate(Elektrogeraete):
    power : int = 0
    
    def connect():
        pass
    
@dataclass
class Kuehlschraenke(Elektrogeraete):
    energylabel : str = "G"
    
    def power_on()):
        pass

@dataclass
class Stereoverstaerker(Hifigerate):
    power : str = "0"
    
    def volume_up():
        pass

@dataclass
class CDPlayer(Hifigerate):
    color : str
    
    def open_slot():
        pass



