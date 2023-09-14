from typing import Optional
from pydantic import BaseModel

class Alien(BaseModel):
    id: Optional[int] = None
    name: str
    species: str
    homeWorld: str
    body: str

class Pirate(BaseModel):
    id: Optional[int]= None
    french_name: str
    job: str
    size: str
    birthday: Optional[str] = None
    age: Optional[str] = None
    bounty: Optional[str] = None
    status: Optional[str] = None
    crewId: Optional[int] = None
    fruitId: Optional[int] = None
    secondFruitId: Optional[int] = None

aliens = [
    Alien(id=1, name="Wildmutt", species="Vulpimancer", homeWorld="Vulpin", body="Animalistic"),
    Alien(id=2, name="Heatblast", species="Pyronita", homeWorld="Pyros", body="Fiery Humanoid"),
    Alien(id=3, name="Diamondhead", species="Petrosapien", homeWorld="Petropia", body="Crystalline Humanoid"),
    Alien(id=4, name="XLR8", species="Kineceleran", homeWorld="Kinet", body="Humanoid Velociraptor"),
    Alien(id=5, name="Grey Matter", species="Galvan", homeWorld="Galvan Prime", body="Humanoid Frog"),
    Alien(id=6, name="Four Arms", species="Tetramand", homeWorld="Khoros", body="Four-Armed Humanoid"),
    Alien(id=7, name="Stinkfly", species="Lepidopterran", homeWorld="Lepidopterra", body="Winged Insectoid"),
    Alien(id=8, name="Ripjaws", species="Piscciss Volann", homeWorld="Piscciss", body="Humanoid Anglerfish"),
    Alien(id=9, name="Upgrade", species="Galvanic Mechamorph", homeWorld="Galvan B", body="Technological Humanoid"),
    Alien(id=10, name="Ghostfreak", species="Ectonurite", homeWorld="Anur Phaetos", body="Ghost"),
]