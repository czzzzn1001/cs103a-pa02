#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''

from transactions import Transaction
from category import Category
import sys

transactions = Transaction('tracker.db')
category = Category('tracker.db')


# here is the menu for the tracker app

menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''




# just add some comments to test pushing is ok
def process_choice(choice):

    if choice=='0':
        return
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)

#     elif choice== '4':
#         print('Showing all transactions: ')
#         trans = transactions.select_all()
#         print_transactions(trans)
#     elif choice== '5':
#         print('Adding a new transaction: ')
#         item_no = int(input("item_no: "))
#         amount = int(input("amount: "))
#         categoryItem = input("transaction category: ")
#         date = input("transaction date: ")
#         description = input("transaction description: ")
#         trans = {'item_no':item_no, 'amount':amount, 'category':categoryItem,
#                 'date':date, 'description':description}
#         transactions.add(trans)

        
    elif choice=='4':
        all_trans = transactions.select_all()
        if len(all_trans) == 0:
            print('No transaction recorded.')
        for tran in all_trans:
            print(tran)
    elif choice=="5":
        all_trans = transactions.select_all()
        if len(all_trans) == 0:
            last_one_item_no = 0
        else:
            last_one_item_no = all_trans[-1]["item_no"]
        year = input("Enter year: ")# has to be in YYYY form
        month = input("Enter month: ")#has to be in MM form
        day = input("Enter day: ")# has to be in DD form
        date = year + "-" + month + "-" + day
        amount_enter = input("Enter amount: ")
        amount = int(amount_enter)
        category = input("Enter category: ")
        description = input("Enter description: ")
        trans = {"item_no": last_one_item_no + 1, 'amount': amount, 'category': category, 'date': date, 'description': description}
        transactions.add(trans)
    elif choice=='6':
        all_trans = transactions.select_all()
        print('Select one of the following item number to delete: ')
        if len(all_trans)==0:
            print('Ooops, the database is empty. There\'s nothing to delete.')
        else:
            for tran in all_trans:
                print(tran['item_no'])
            item_number = input('Enter item number: ')
            transactions.delete(item_no=item_number)
            print('Deleted!')
    elif choice=='7':
        all_trans = transactions.select_all()
        print('Summary by date')
        year = input('Which year? ').strip()
        month = input('which month? ').strip()
        day = input('which day? ').strip()
        search_term = year+'-'+month+'-'+day
        print(search_term)
        trans = transactions.summarize_by_date(search_term)
        if len(trans)==0:
            print('No record for that date. Sorry!')
        else:
            for tran in trans:
                print(tran)
    elif choice== '8':
        print('Summarizing transactions by month: ')
        month = input("Enter the month (e.g. 01 for January):   ")
        trans = transactions.summarize_by_month(month)
        print_transactions(trans)

    elif choice== '9':
        print('Summarizing transactions by year: ')
        year = input("Enter the month (e.g. 2021 for 2021):   ")
        trans = transactions.summarize_by_year(year)
        print_transactions(trans)
    elif choice == '10':
        cat = input("Enter the category: ")
        trans = transactions.summarize_by_cate(cat)
        if len(trans)==0:
            print('No record for that date. Sorry!')
        else:
            for tran in trans:
                print(tran)

    elif choice == '11':
        print(menu)
    else:
        print("choice",choice,"not yet implemented")
    choice = input("> ")
    return(choice)


def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')


    print("%-10s %-10s %-10s %-10s %-30s"%(
        'item #','amount','category','date','description'))
    print('-'*60)
    for item in items:
        values = tuple(item.values()) 
        print("%-10d %-10d %-10s %-10s %-30s"%values)

def print_category(cat):
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)


# here is the main call!

toplevel()

