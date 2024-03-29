import datetime

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship, Session

engine = create_engine("postgresql://postgres:root@localhost/niva1")


class Base(DeclarativeBase): pass

class Manufacture(Base):
    __tablename__ = "manufacture"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    discription = Column(String)
    creps=relationship("Crep_ifc", back_populates="manufacture")

class Crep_ifc(Base):
    __tablename__ = "creps"
    id = Column(Integer,primary_key=True, index=True)
    num = Column(Integer)
    sensors=relationship("Sensors_ifc", back_populates="crep")
    manufacture_id=Column(Integer,ForeignKey("manufacture.id"))
    manufacture=relationship("Manufacture", back_populates="creps")




class Sensors_ifc(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    id_dat = Column(Integer)
    value = Column(String)
    # created_date = Column(String)
    create_date = Column(DateTime, default=datetime.datetime.now())
    crep_id = Column(Integer, ForeignKey("creps.id"))
    crep = relationship("Crep_ifc", back_populates="sensors")

Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    # создаем компании
    # manuf = Manufacture(name="Pizda", discription="Da poshlo ono vse v pizdu")
    # db.add(manuf)
    # db.commit()
    for elem in range(1,301):

        microsoft = Crep_ifc(num = elem,manufacture_id=1)

        db.add(microsoft)
        db.commit()