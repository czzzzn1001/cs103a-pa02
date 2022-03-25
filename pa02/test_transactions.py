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

@pytest.mark.summarize_by_month
def test_summarize_by_month():
    newTran1 = {'item_no': 1, 'amount': 10, 'category': 'food', 'date': '2021-03-15', 'description': 'milk and sparking water'}
    newTran2 = {'item_no': 2, 'amount': 1, 'category': 'cloth', 'date': '2022-03-31', 'description': 'workout t-shirt'}
    newTran3 = {'item_no': 3, 'amount': 2, 'category': 'books', 'date': '2021-07-01', 'description': 'cs book'}
    newTran4 = {'item_no': 4, 'amount': 3, 'category': 'food', 'date': '2022-07-22', 'description': 'some fruits'}
    newTran5 = {'item_no': 5, 'amount': 1, 'category': 'books', 'date': '2022-02-28', 'description': 'three-body'}

    transactions.add(newTran1)
    transactions.add(newTran2)
    transactions.add(newTran3)
    transactions.add(newTran4)
    transactions.add(newTran5)

    selectedTransactions = transactions.summarize_by_month('03')
    assert 2 == len(selectedTransactions)


@pytest.mark.summarize_by_year
def test_summarize_by_year():
    # newTran1 = {'item_no': 1, 'amount': 10, 'category': 'food', 'date': '2021-03-15', 'description': 'milk and sparking water'}
    # newTran2 = {'item_no': 2, 'amount': 1, 'category': 'cloth', 'date': '2022-03-31', 'description': 'workout t-shirt'}
    # newTran3 = {'item_no': 3, 'amount': 2, 'category': 'books', 'date': '2021-07-01', 'description': 'cs book'}
    # newTran4 = {'item_no': 4, 'amount': 3, 'category': 'food', 'date': '2022-07-22', 'description': 'some fruits'}
    # newTran5 = {'item_no': 5, 'amount': 1, 'category': 'books', 'date': '2022-02-28', 'description': 'three-body'}

    # transactions.add(newTran1)
    # transactions.add(newTran2)
    # transactions.add(newTran3)
    # transactions.add(newTran4)
    # transactions.add(newTran5)

    selectedTransactions = transactions.summarize_by_year('2021')
    assert 2 == len(selectedTransactions)


    
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

@pytest.mark.summarize_by_cat
def test_summarize_by_cat():
    tran = transactions.summarize_by_cate('A')
    assert 0 == tran[0]['item_no']
    assert 1 == tran[0]['amount']
    assert 'A' == tran[0]["category"]
    assert "1996-02-11" == tran[0]["date"]
    assert "ABCD" == tran[0]["description"]
