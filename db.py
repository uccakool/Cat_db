import mysql.connector

import mysql

'''
State your group member name and id here: 
1. 2022103thol - Thol Ucca Kool
2. 2021093 - thong
3. 2022205 - rit
ex: 1. 2023001chea - Joe Chea

'''


# TODO:
# host can be 'localhost' or '127.0.0.1'
# if you are using mamp, password is root
# and port is 8889
# use cat_db as database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="cat_db",
    port="3306"
)

print(mydb)

cursor = mydb.cursor()


def register_cat(cat_info):
    '''
    TODO:
    cat_info is in a form of list ex: ["rose", "f", "Siberian", "2020-03-08", "smart one"], that register_cat function will insert the provided
    list to cats table as an insert record.
    '''
    pass


def get_cats():
    '''
    TODO:
    this function will get all cat from cats table 
    '''
    pass


def get_cat(id):
    '''
    TODO:
    this function will get a single cat data from cat table base on the id parameter
    '''
    pass


def update_cat(cat_info):
    '''
    TODO:
    cat_info is in a form of list ex: [1,"rose", "f", "Siberian", "2020-03-08", "smart one"], that update_cat function will use as 
    an update record for specific cat information where equal to cat_info[0]
    '''
    pass


def remove_cat(id):
    '''
    TODO:
    this function will remove record from cat table base on id parameter.
    '''
    pass
