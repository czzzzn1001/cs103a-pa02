# PA02: team-36
### finance tracker - using SQL and pytest
#### running `pylint`:
```
root@LAPTOP-FDTNRE2C:/mnt/c/Users/82107/OneDrive/桌面/cs103a-pa02-team36/pa02# pylint tracker.py
************* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:98:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:119:0: C0301: Line too long (131/100) (line-too-long)
tracker.py:171:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:200:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:216:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:44:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:117:8: W0621: Redefining name 'category' from outer scope (line 39) (redefined-outer-name)
tracker.py:63:0: R0914: Too many local variables (20/15) (too-many-locals)
tracker.py:65:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:68:15: E0601: Using variable 'category' before assignment (used-before-assignment)
tracker.py:63:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:63:0: R0912: Too many branches (26/12) (too-many-branches)
tracker.py:63:0: R0915: Too many statements (83/50) (too-many-statements)
tracker.py:177:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:196:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:201:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:203:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:204:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:206:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:207:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:36:0: W0611: Unused import sys (unused-import)
tracker.py:36:0: C0411: standard import "import sys" should be placed before "from transactions import Transaction" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 7.57/10 (previous run: 5.00/10, +2.57)

root@LAPTOP-FDTNRE2C:/mnt/c/Users/82107/OneDrive/桌面/cs103a-pa02-team36/pa02# pylint transactions.py
************* Module transactions
transactions.py:10:0: C0301: Line too long (141/100) (line-too-long)   
transactions.py:21:34: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:43:26: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:105:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:107:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:108:0: C0305: Trailing newlines (trailing-newlines)
transactions.py:21:9: W0511: FIXME: change types here  (fixme)
transactions.py:34:9: W0511: FIXME: modify insertion here (fixme)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transactions.py:5:0: W0105: String statement has no effect (pointless-string-statement)
transactions.py:17:0: C0115: Missing class docstring (missing-class-docstring)
transactions.py:40:4: R1711: Useless return at end of function or method (useless-return)
transactions.py:96:31: W0621: Redefining name 'category' from outer scope (line 3) (redefined-outer-name)
transactions.py:2:0: W0611: Unused import os (unused-import)
transactions.py:3:0: W0611: Unused category imported from unicodedata (unused-import)

-----------------------------------
Your code has been rated at 7.86/10
```
#### runing `pytest`
```
root@LAPTOP-FDTNRE2C:/mnt/c/Users/82107/OneDrive/桌面/cs103a-pa02-team36/pa02# pytest -v
============================================================================================ test session starts =============================================================================================
platform win32 -- Python 3.9.5, pytest-6.2.5, py-1.9.0, pluggy-1.0.0 -- c:/Users/82107/miniconda3/python.exe
cachedir: .pytest_cache
rootdir: root@LAPTOP-FDTNRE2C:/mnt/c/Users/82107/OneDrive/桌面/cs103a-pa02-team36/pa02#, configfile: pytest.ini
plugins: anyio-3.5.0
collected 11 items

test_category.py::test_to_cat_dict PASSED                                                                                                                                                               [  9%] 
test_category.py::test_add PASSED                                                                                                                                                                       [ 18%]
test_category.py::test_delete PASSED                                                                                                                                                                    [ 27%]
test_category.py::test_update PASSED                                                                                                                                                                    [ 36%]
test_transactions.py::test_select_all PASSED                                                                                                                                                            [ 45%]
test_transactions.py::test_add_transaction PASSED                                                                                                                                                       [ 54%]
test_transactions.py::test_summarize_by_month PASSED                                                                                                                                                    [ 63%]
test_transactions.py::test_summarize_by_year PASSED                                                                                                                                                     [ 72%] 
test_transactions.py::test_delete_transaction PASSED                                                                                                                                                    [ 81%]
test_transactions.py::test_summarize_by_date PASSED                                                                                                                                                     [ 90%]
test_transactions.py::test_summarize_by_cat PASSED                                                                                                                                                      [100%] 

============================================================================================= 11 passed in 1.45s ============================================================================================= 

Script done on 2022-03-24 23:37:34-04:00 [COMMAND_EXIT_CODE="0"]
```

#### running `pythong3 tracker.py`
```
root@LAPTOP-FDTNRE2C:/mnt/c/Users/82107/OneDrive/桌面/cs103a-pa02-team36/pa02# python3 tracker.py

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

> 4
{'item_no': 1, 'amount': 1, 'category': 'A', 'date': '1996-02-11', 'description': 'ABCD'}
{'item_no': 2, 'amount': 2, 'category': 'B', 'date': '1997-03-12', 'description': 'QWER'}
{'item_no': 3, 'amount': 3, 'category': 'C', 'date': '1998-04-13', 'description': 'WASZ'}
> 5
Enter year: 1998
Enter month: 05
Enter day: 14
Enter amount: 4
Enter category: D
Enter description: aodskfs
> 4
{'item_no': 1, 'amount': 1, 'category': 'A', 'date': '1996-02-11', 'description': 'ABCD'}
{'item_no': 2, 'amount': 2, 'category': 'B', 'date': '1997-03-12', 'description': 'QWER'}
{'item_no': 3, 'amount': 3, 'category': 'C', 'date': '1998-04-13', 'description': 'WASZ'}
{'item_no': 4, 'amount': 4, 'category': 'D', 'date': '1998-05-14', 'description': 'aodskfs'}
> 6
Select one of the following item number to delete:
1
2
3
4
Enter item number: 4
Deleted!
> 4
{'item_no': 1, 'amount': 1, 'category': 'A', 'date': '1996-02-11', 'description': 'ABCD'}
{'item_no': 2, 'amount': 2, 'category': 'B', 'date': '1997-03-12', 'description': 'QWER'}
{'item_no': 3, 'amount': 3, 'category': 'C', 'date': '1998-04-13', 'description': 'WASZ'}
> 7
Summary by date
Which year? 1997
which month? 03
which day? 12
1997-03-12
{'item_no': 2, 'amount': 2, 'category': 'B', 'date': '1997-03-12', 'description': 'QWER'}
> 8
Summarizing transactions by month:
Enter the month (e.g. 01 for January):   03


item #     amount     category   date       description
------------------------------------------------------------
2          2          B          1997-03-12 QWER
> 9
Summarizing transactions by year:
Enter the year (e.g. 2021 for 2021):   1998


item #     amount     category   date       description
------------------------------------------------------------
3          3          C          1998-04-13 WASZ
> 10
Enter the category: B
{'item_no': 2, 'amount': 2, 'category': 'B', 'date': '1997-03-12', 'description': 'QWER'}
> 11

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

> 0
bye
root@LAPTOP-FDTNRE2C:/mnt/c/Users/82107/OneDrive/桌面/cs103a-pa02-team36/pa02# exit
exit

```





