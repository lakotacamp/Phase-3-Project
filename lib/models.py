from sqlalchemy import ForeignKey, Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, validates

Base = declarative_base()

class Weapons(Base):
    __tablename__= "weaps"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    type = Column(String)
    subclass = Column(String)
    perked_weaps = relationship("Perked_Weapons", back_populates="weaps")

    def __repr__(self):
        return repr(f"{self.name}")

class Perks(Base):
    __tablename__= "perks"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    type = Column(String)
    subclass = Column(String)
    perked_weaps = relationship("Perked_Weapons", back_populates="perks")

    def __repr__(self):
        return repr(f"{self.name}")

class Perked_Weapons(Base):
    __tablename__ = "perked_weapons"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    weaps_id = Column(Integer, ForeignKey("weaps.id"))
    weaps = relationship("Weapons", back_populates="perked_weaps")
    perks_id = Column(Integer, ForeignKey("perks.id"))
    perks = relationship("Perks", back_populates="perked_weaps")

    def __repr__(self):
        return repr(f"{self.name}")


engine = create_engine("sqlite:///darktide_builder.db")




'''
class Weapon(Base):
    __tablename__ = "weapons"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    inventory_weapons = relationship("Inventory_weapon", back_populates="weapon")
    build_weapons = relationship("Build_weapons", back_populates="weapon")
    list_weapons = relationship("List_weapon", back_populates="weapon")

    def __repr__(self):
        return repr(f"{self.name}")
    
class Inventory_weapon(Base):
    __tablename__ = "inventory_weapons"
    id = Column(Integer, primary_key = True)
    weapon_id = Column(Integer, ForeignKey("weapons.id"))
    weapon = relationship("Weapon", back_populates= "inventory_weapons")
    quantity = Column(Integer)

    def __repr__(self):
        return f"{self.quantity} {self.weapon}"

class List_weapon(Base):
    __tablename__ = "list_weapons"
    id = Column(Integer, primary_key = True)
    weapon_id = Column(Integer, ForeignKey("weapons.id"))
    weapon = relationship("Weapon", back_populates= "list_weapons")
    missing_list_id = Column(Integer, ForeignKey('missing_lists.id'))
    missing_list = relationship("Missing_list", back_populates="list_weapons")
    quantity = Column(Integer)

    def __repr__(self):
        return f"{self.quantity} {self.weapon.name}"
    
class Missing_list(Base):
    __tablename__ = "missing_lists"

    id = Column(Integer, primary_key = True)
    mission_id = Column(Integer, ForeignKey('missions.id'))
    mission = relationship("Mission", back_populates="missing_list")
    list_weapons = relationship("List_weapon", back_populates="missing_list")

    def pretty(self):
        string = ""
        for list_weapon in self.list_weapons:
            string += str(list_weapon)+ "\n"
        return f"Weapons Required for {self.mission.mission_name}\n----------------------------------------------\n{string}"
    def __repr__(self):
        return f"{self.list_weapons}"
    
class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key = True)
    mission_name = Column(String)
    missing_list = relationship("Missing_list", back_populates="mission")
    team_comps = relationship("Team_comp", back_populates="mission")

    def __repr__(self):
        return f"Mission Assignment: {self.mission_name}"

class Team_comp(Base):
    __tablename__ = "team_comps"

    id = Column(Integer, primary_key = True)
   # day = Column(String)
    team_comp_name = Column(String)
    mission_id = Column(Integer, ForeignKey('missions.id'))
    mission = relationship("Mission", back_populates="team_comps")
    team_comp_builds = relationship("Team_comp_build", back_populates="team_comp")

# I am leaving gra_date(self): out for right now
# Same with date(self)


    def __repr__(self):
        return f"{self.team_comp_name}: {self.team_comp_builds}"

# join table for team comp and character build
class Team_comp_build(Base):
    __tablename__ = "team_comp_builds"

    id = Column(Integer, primary_key = True)
    team_comp_id = Column(Integer, ForeignKey("team_comps.id"))
    team_comp = relationship("Team_comp", back_populates="team_comp_builds")
    character_build_id = Column(Integer, ForeignKey("character_builds.id"))
    character_build = relationship("Character_build", back_populates="team_comp_builds")

    def __repr__(self):
        return f"{self.character_build.name}"

class Character_build(Base):
    __tablename__ = "character_builds"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    instructions = Column(String)
    type = Column(String)
    cuisine = Column(String)
    team_comp_builds = relationship("Team_comp_build", back_populates="character_build")
    build_weapons = relationship("Build_weapon", back_populates="character_build")

    def pretty_ingredients(self):
        ingredient_list =""
        for ingredient in self.build_weapons:
            ingredient_list+=str(ingredient) + "\n"
        return ingredient_list
    
    def __repr__(self):
        return (f"{self.name}\n---------------------------------------------------\n({self.cuisine} {self.type})\n\n{self.pretty_ingredients()}\n\n{self.instructions}\n")
    
class Build_weapon(Base):
    __tablename__ = "build_weapons"

id = Column(Integer, primary_key = True)
character_build_id = Column(Integer, ForeignKey("character_builds.id"))
character_build = relationship("Character_build", back_populates="ingredient_items")
weapon_id = Column(Integer, ForeignKey("weapons.id"))
weapon = relationship("Weapon", back_populates="build_weapons")
quantity = Column(Integer)

def __repr__(self):
    return f"{self.quantity} {self.item.name}"
'''