from sqlalchemy import select

from database.db import get_session
from database.models import Market


class MarketRepository:

    def __init__(self):
        self.session = get_session()

    def add_db(self, user_id, product, cost):
        add_market = Market(
            user_id=user_id,
            product=product,
            cost=cost
        )

        self.session.add(add_market)
        self.session.commit()

    def show_market(self, user_id):
        return self.session.execute(
            select(Market).where(
                Market.user_id == user_id
            )
        ).scalars().all()

    def dell_market(self, id, user_id):
        item = self.session.execute(
            select(Market).where(
                Market.id == id,
                Market.user_id == user_id
            )
        ).scalar()

        if item:
            self.session.delete(item)
            self.session.commit()

    def drop_market(self, user_id):
        items = self.session.execute(
            select(Market).where(
                Market.user_id == user_id
            )
        ).scalars().all()

        for item in items:
            self.session.delete(item)

        self.session.commit()

    def update_market(self, id, user_id, product, cost):
        item = self.session.execute(
            select(Market).where(
                Market.id == id,
                Market.user_id == user_id
            )
        ).scalar()

        if item:
            item.product = product
            item.cost = cost
            self.session.commit()

    def get_market(self, id, user_id):
        return self.session.execute(
            select(Market).where(
                Market.id == id,
                Market.user_id == user_id
            )
        ).scalar()
