### about 

求两个文件的差分 diff

1. 标记两个差分文件为A，B

两个文件的key相同进入一个reduce里，检查是否只有其中的一个value
		
	card1,A
	card1,B
	
	card1,A

  	--------------

	card1,A
		
#### local.run

	cat t1.csv | ./local.run
