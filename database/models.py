from sqlalchemy import Column, Integer, String, Float

from .db import Base, engine


class Market(Base):
    __tablename__ = "market"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    product = Column(String(30), nullable=False)
    cost = Column(Float, nullable=False)


Base.metadata.create_all(bind=engine)
