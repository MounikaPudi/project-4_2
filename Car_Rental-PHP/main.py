from blockchain import Blockchain
from car_sharing import Owner, Car, Customer


def show_balance(cust_balance, owner_balance):
    print("Customer balance: %s" % (cust_balance,))
    print("Owner balance: %s" % (owner_balance,))

def show_rental_cost(cost):
    print("Rental cost: ", cost)

def start():
    blockchain = Blockchain()
    customer = Customer(500)
    owner = Owner(500)
    eth = 50

    show_balance(customer.balance, owner.balance)

    
    owner.deploy(eth, blockchain)

    
    customer.request_book(eth, blockchain)

    
    car = "Ferrari"
    daily_price = 10
    days_no = 3
    owner.add_car_to_rent(daily_price, car)
    customer.pass_number_of_days(days_no)

    
    owner.encrypt_and_store_details(blockchain)
    owner.allow_car_usage()

    
    customer.access_car()

    
    customer.end_car_rental()

    
    owner.withdraw_earnings()
    customer.retrieve_balance()

    show_rental_cost(daily_price*days_no)
    show_balance(customer.balance, owner.balance)


if __name__ == '__main__':
    start()
