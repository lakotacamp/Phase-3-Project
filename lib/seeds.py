import random
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base
from models import * 

if __name__ == '__main__':
#    Weapon.__table__.drop(engine)
#    Perks.__table__.drop(engine)
#    Perked_Weapons.__table__.drop(engine)
    Base.metadata.create_all(engine)
    print("Metadata create all")
    with Session(engine) as session:

    #names = ["ShootyMcShootface", "The Big Bloaster", "Ultrakill", "Codename: Murder"]
        ranged_or_melee = ["ranged", "melee"]
        classes = ["Psyker", "Veteran", "Zealot", "Ogryn"]
        for i in range(50):
            new_weapon = Weapons(
                name = f"Weapon{i}",
                type = ranged_or_melee[random.randint(0, 1)],
                subclass = classes[random.randint(0, len(classes)-1)]
            )
            session.add(new_weapon)
            session.commit()



        for i in range(50):
            new_perk = Perks(
                name = f"Perk{i}",
                type = ranged_or_melee[random.randint(0,1)],
                subclass = classes[random.randint(0, len(classes)-1)]
            )
            session.add(new_perk)
            session.commit()

        for i in range(50):
            rando_weap = session.query(Weapons).filter(Weapons.id == random.randint(1,50)).first()
            rando_perk = session.query(Perks).filter(Perks.id == random.randint(1,50)).first()
            new_perked_weapon = Perked_Weapons(
                name = f"Perked Up Weapon {i}",
                weaps_id = rando_weap.id,
                perks_id = rando_perk.id
            )
            session.add(new_perked_weapon)
            session.commit()