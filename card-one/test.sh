cat one_test.txt  | ./mapper.py | sort -k1,1 | ./reducer.py 
