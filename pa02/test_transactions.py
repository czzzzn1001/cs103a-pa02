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

@pytest.mark.summarize_by_cat
def test_summarize_by_cat():
    tran = transactions.summarize_by_cate('A')
    assert tran == {'item_no': 0,'amount': 1, "category": 'A', "date": "1996-02-11", "description": "ABCD"}
    
