from datetime import date


class Good:
    def __init__(self, good_id: int, name: str, price: float):
        self.good_id = good_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"good_id: {self.good_id}, name: {self.name}, price: {self.price}"


class Order:
    def __init__(self, order_id: int, order_date, client_id: int):
        self.id = order_id
        self.order_date = order_date
        self.client_id = client_id
        self.goods = []

    def add_good(self, good: Good):
        self.goods.append(good)

    def get_price(self):
        result = 0
        for good in self.goods:
            result += good.price
        return result

    def __str__(self):
        goods = ""
        for good in self.goods:
            goods += str(good) + "; "
        return f"order_id: {self.id}, order_date: {self.order_date}, client_id: {self.client_id}" \
               f", goods: ({goods})" \
               f", price: {self.price}"

    price = property(get_price)


class OrderRepository:
    def __init__(self):
        self.order_list = []

    def add_order(self, order: Order):
        self.order_list.append(order)

    def get_order(self, order_id: int):
        for order in self.order_list:
            if order.id == order_id:
                return order

    def list_n_latest_orders(self, n_latest: int = None):
        if n_latest is None or n_latest > len(self.order_list):
            return self.order_list
        else:
            return self.order_list[-n_latest:]

    def delete_order(self, order_id: int):
        for num, order in enumerate(self.order_list):
            if order.id == order_id:
                self.order_list.pop(num)


# create goods
good1 = Good(1, 'Keyboard', 11)
good2 = Good(2, 'Mouse', 5)
good3 = Good(3, 'Mouse pad', 2)
# get date
d = date.today()
# create order1 and add 2 goods
order1 = Order(1, d, 1)
order1.add_good(good1)
order1.add_good(good2)
assert order1.price == 16
# create order2 and add 3 goods
order2 = Order(2, d, 2)
order2.add_good(good1)
order2.add_good(good2)
order2.add_good(good3)
assert order2.price == 18
# create order3 and add 2 goods
order3 = Order(3, d, 3)
order3.add_good(good2)
order3.add_good(good3)
assert order3.price == 7
# create repo1
repo1 = OrderRepository()
repo1.add_order(order1)
assert repo1.get_order(1) == order1
assert repo1.get_order(2) is None
# add two more orders to repo1
repo1.add_order(order2)
repo1.add_order(order3)
assert repo1.list_n_latest_orders(2) == [order2, order3]
assert repo1.list_n_latest_orders() == [order1, order2, order3]
# delete order2
repo1.delete_order(2)
assert repo1.order_list == [order1, order3]
