#!/bin/bash 

hadoop jar /home/upsmart/tools/hadoop-2.5.0/share/hadoop/tools/lib/hadoop-streaming-*.jar \
	-D mapred.job.name="diff job " \
	-numReduceTasks 4 \
	-input $1 \
	-output $2  \
	-file $PWD/mapper.py -mapper $PWD/mapper.py \
	-file $PWD/reducer.py -reducer $PWD/reducer.py 
