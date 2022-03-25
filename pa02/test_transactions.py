import pytest
from transactions import Transaction
from category import Category, to_cat_dict

transactions = Transaction('test_tracker1.db')

@pytest.mark.selectAll
def test_select_all():
    assert 0 == len(transactions.select_all())
    
@pytest.mark.add
def test_add_transaction():
    new_tran = {'item_no': 0,'amount': 1, "category": 'A', "date": "1996-02-11", "description": "ABCD"}
    transactions.add(new_tran)
    assert 1 == len(transactions.select_all())

@pytest.mark.delete
def test_delete_transaction():
    init_len = len(transactions.select_all())
    new_tran = {'item_no': 1018,'amount': 11, "category": 'AA', "date": "1996-02-12", "description": "ABCDE"}
    transactions.add(new_tran)
    transactions.delete(1018)
    assert init_len == len(transactions.select_all())

@pytest.mark.summary_by_date
def test_summarize_by_date():
    new_tran1 = {'item_no': 111,'amount': 1, "category": 'A', "date": "2022-10-18", "description": "ABCDefgh"}
    new_tran2 = {'item_no': 112,'amount': 2, "category": 'B', "date": "2022-10-18", "description": "ABCDEFG"}
    new_tran3 = {'item_no': 113,'amount': 3, "category": 'A', "date": "2022-10-18", "description": "ABCDkownefonwsenif"}
    transactions.add(new_tran1)
    transactions.add(new_tran2)
    transactions.add(new_tran3)
    selected_trans = transactions.summarize_by_date('2022-10-18')
    for tran in selected_trans:
        assert tran['date'] == '2022-10-18'



    
