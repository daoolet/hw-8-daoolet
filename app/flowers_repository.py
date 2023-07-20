from attrs import define

from sqlalchemy import Boolean, Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, Session

from .database import Base


class Flower(Base):
    __tablename__ = "flowers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    count = Column(Integer)
    cost = Column(Integer)


@define
class FlowerCreate:
    name: str
    count: int
    cost: int


class FlowersRepository:

    # необходимые методы сюда
    def get_all(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Flower).offset(skip).limit(limit).all()
    
    def get_by_id(self, db: Session, flower_id: int):
        return db.query(Flower).filter(Flower.id == flower_id).first()

    def save_flower(self, db: Session, new_flower: FlowerCreate):
        db_flower = Flower(name=new_flower.name, count=new_flower.count, cost=new_flower.cost)
        db.add(db_flower)
        db.commit()
        db.refresh(db_flower)
        return db_flower
    
    def update_flower(self, db: Session, flower_id: int, new_flower: FlowerCreate):
        db_flower = db.query(Flower).filter(Flower.id == flower_id).first()
        db_flower.name = new_flower.name
        db_flower.count = new_flower.count
        db_flower.cost = new_flower.cost
        db.commit()
        return True
    
    def delete_flower(self, db: Session, flower_id: int):
        db_flower = db.query(Flower).filter(Flower.id == flower_id).first()
        db.delete(db_flower)
        db.commit()
        # db.refresh(db_flower)
        return True

    # def add_cart_flowers(self, new_cart_flower: Flower):
    #     self.cart_flowers.append(new_cart_flower)

    # def get_cart_flowers(self):
    #     return self.cart_flowers
    # конец решения
