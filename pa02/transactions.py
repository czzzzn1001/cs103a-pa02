import sqlite3
import os
from unicodedata import category

'''
written by Zheng Chu
'''
def to_trans_dict(trans_tuple):
    ''' cat is a category tuple (rowid, name, desc)'''
    trans = {'item_no':trans_tuple[0], 'amount':trans_tuple[1], 'category':trans_tuple[2],'date':trans_tuple[3],'description':trans_tuple[4]}
    return trans

def to_trans_dict_list(trans_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_trans_dict(trans) for trans in trans_tuples]

class Transaction:
    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_no int, amount int,category text,date datetime,description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def add(self,item):
        ''' add a category to the transactions table.
            this returns the item_no of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)"
        ,(item['item_no'],item['amount'],item['category'],item['date'],item['description']))
        con.commit()
        con.close()

    def delete(self,item_no):
        ''' delete an item '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor() 
        cur.execute("DELETE FROM transactions WHERE item_no=(?)",(item_no,))
        con.commit()
        con.close()
        return

    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)


    # date is input string with format of "YYYY-MM-DD"
    def summarize_by_date(self,date):
        ''' select a certain date from the time '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions where date(date)=date(?)",(date,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)


   # important: the input month here should be string type length of 2
   # moreover, if it has one digit, we need to prepend 0 eg. '8'->'08'
   # if it has two, leave it be, otherwise the query will yield nothing
    def summarize_by_month(self,month):
        ''' select a certain month from the time '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions where strftime('%m',date(dd))=(?)",(month,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    # important: the input year should be string type length of 4
    def summarize_by_year(self,year):
        ''' select a certain year from the time '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions where strftime('%Y',date(dd))=(?)",(year,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    def summarize_by_cate(self,category):
        ''' select a certain category from the transactions '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions where category=(?)",(category,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)
        

        

