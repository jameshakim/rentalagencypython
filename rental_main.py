import pickle


def program_start(items):
    """(str) -> None
    The user is asked if they are customer or admin.
    >>> program_start(customer)
    Would you like to rent or return?
    >>> program_start(admin)
    What is your username and password?
    >>> program_start(custimir)
    Please retype that.
    """

    start = input("Are you a Customer or Admin? ")
    if start == "Customer":
        cus_name = input("What is your name?")
        rent_return = input("Hey " + cus_name +
                            " would you like to rent or return? ")
        if rent_return == "rent":
            rent(items)
        else:
            rent_return == "return"
            return_item(items)
    elif start == "Admin":
        admin_options()


def admin_options():
    """(str) -> None
    The admin is asked if they would like to add or remove items or view the transaction file or revenue history.
    >>> admin_options(remove)
    Item is removed.
    >>> admin_options(add)
    Item is added.
    >>> admin_options(view transaction)
    Display transaction.
    >>> admin_options(view revenue history)
    Display revenue history.
    """
    ask_admin = input(
        "Would you like to add an item, remove an item, view transaction file, or view revenue history? "
    )
    if ask_admin == 'add':
        add_item(items)
        # add item to inventory
    elif ask_admin == 'remove':
        remove_item(items)
        # remove an item from the inventory
    elif ask_admin == 'view t':
        show_trans()
    # display transaction file


    # display revenue history
def rent(items):
    """(str) -> (int)
    The user is asked what item they would like to rent.
    >>> rent(flood lights, 1)
    You're total is $26.
    >>> rent(chainsaw, 2)
    You're total is $80.
    >>> rent(6' ladder, 3)
    You're total is $51.
    """
    print(items)

    start_rent = input("What item would you like to rent?")
    if start_rent == "6ft ladder":
        rent_start(items, start_rent)
    if start_rent == "12ft ladder":
        rent_start(items, start_rent)
    if start_rent == "drill":
        rent_start(items, start_rent)
    if start_rent == "chainsaw":
        rent_start(items, start_rent)
    if start_rent == "table saw":
        rent_start(items, start_rent)
    print(items)

    print("Thank you for renting our " + start_rent)
    f = open('transactions.txt', 'w')
    f.write("Customer rented 1 " + start_rent + " for " + str(items[start_rent]
                                                              ['rent']))
    f.close()


def rent_start(items, start_rent):
    items[start_rent]["quantity"] -= 1
    return items[start_rent]["quantity"]


def return_item(items):
    """(str, int) -> None
    The user is asked what item they would like to return and how many days they rented the item.
    >>> return_item(flood lights, 3)
    Thank you for returning the flood lights ... your total is $105.
    >>> return_item(chainsaw, 1)
    Thank you for returning the chainsaw ... your total is $35.
    >>> return_item(drill, 2)
    Thank you for returning the drills ... your total is $40.
    """

    start_return = input("What would you like to return? ")
    if start_return == "6ft ladder":
        items["6ft ladder"]["quantity"] += 1
    if start_return == "12ft ladder":
        items["12ft ladder"]["quantity"] += 1
    if start_return == "drill":
        items["drill"]["quantity"] += 1
    if start_return == "chainsaw":
        items["chainsaw"]["quantity"] += 1
    if start_return == "table saw":
        items["table saw"]["quantity"] += 1

    print(items)

    print("Thank you for returning our " + start_return)


def open_trans(filename, start_return):
    f = open(filename, 'w')
    f.write("Customer returned 1 " + start_return)
    f.close()


def remove_item(items):
    """(str, int) -> None
    The user is asked what item they would like to delete from the file.
    >>> remove_item(chainsaw, 1)
    You just remove 1 chainsaw from the inventory.
    >>> remove_item(floodlights, 4)
    You just removed 4 floodlights from the inventory.
    >>> remove_item(drill, 2)
    You just removed 2 floodlights from the inventory.
    """

    start_remove = input("What item would you like to remove?")
    if start_remove == "6ft ladder":
        items["6ft ladder"]["quantity"] -= 1
    if start_remove == "12ft ladder":
        items["12ft ladder"]["quantity"] -= 1
    if start_remove == "drill":
        items["drill"]["quantity"] -= 1
    if start_remove == "chainsaw":
        items["chainsaw"]["quantity"] -= 1
    if start_remove == "table saw":
        items["table saw"]["quantity"] -= 1

    print(items)


def add_item(items):
    """(str, int) -> None
    The user is asked what item they would like to add to the file.
    >>> add_item(table saw, 3)
    You just added 3 table saws to the inventory.
    >>> add_item(6' ladder, 4)
    You just added 4 6' ladders to the inventory.
    >>> add_item(12' ladder, 1)
    You just added 1 12' ladder to the inventory.
    """

    start_add = input("What would you like to add? ")
    if start_add == "6ft ladder":
        items["6ft ladder"]["quantity"] += 1
    if start_add == "12ft ladder":
        items["12ft ladder"]["quantity"] += 1
    if start_add == "drill":
        items["drill"]["quantity"] += 1
    if start_add == "chainsaw":
        items["chainsaw"]["quantity"] += 1
    if start_add == "table saw":
        items["table saw"]["quantity"] += 1

    print(items)


def show_trans():
    """
    The user will display the transaction file.
    >>> show_trans('Show transaction file')
    *display file'
    """
    with open('transactions.txt') as fp:
        for line in fp:
            print(line)


def dump_data(items):
    with open('data.pickle', 'wb') as fin:
        pickle.dump(items, fin)


def load_data():
    with open('data.pickle', 'rb') as fin:
        return pickle.load(fin)


def update_history(item, trans_type):
    with open("trans_h.p", "rb") as fin:
        l = pickle.load(fin)
        l.append([item, trans_type])
        with open("trans_h.p", "wb") as fin:
            pickle.dump(l, fin)


def init_trans():
    with open("trans_h.p", "wb") as fin:
        pickle.dump([], fin)


if __name__ == '__main__':
    items = {
        "6ft ladder": {
            "quantity": 1,
            "rent": 10,
            "value": 70
        },
        "12ft ladder": {
            "quantity": 2,
            "rent": 15,
            "value": 100
        },
        "drill": {
            "quantity": 4,
            "rent": 20,
            "value": 150
        },
        "chainsaw": {
            "quantity": 3,
            "rent": 45,
            "value": 350
        },
        "table saw": {
            "quantity": 1,
            "rent": 50,
            "value": 400
        }
    }

    program_start(items)

    data = load_data()
    program_start(data)
    dump_data(data)