#!/bin/bash 
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar \
	-D mapred.job.name="my test word count" \
	-numReduceTasks 2 \
	-file $PWD/mapper.py -mapper $PWD/mapper.py \
	-file $PWD/reducer.py -reducer $PWD/reducer.py \
	-input /user/hduser/jazz/wordcount.txt -output /user/hduser/jazz/wordcount.output.5

