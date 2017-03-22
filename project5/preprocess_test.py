import json
import time
import datetime
import numpy as np
from dateutil.parser import *

tags = ['sample1_period1','sample2_period2','sample3_period3','sample4_period1','sample5_period1'
,'sample6_period2','sample7_period3','sample8_period1','sample9_period2','sample10_period3']
start = time.time()

for tag in tags:
	print 'Processing ' + tag

	read_file = 'test_data/' + tag + '.txt'
	write_file = 'test_data/' + tag
	f = open(read_file, 'r')
	g = open(write_file, 'w')


	# Make sure to go back to file head
	f_start = f.tell()
	f.seek(f_start)

	for line in f.readlines():
		tweet = json.loads(line)
		obj = {}
		obj['retweet'] = tweet['metrics']['citations']['data'][0]['citations']
		obj['followers'] = tweet['tweet']['user']['followers_count']
		obj['firstpost_date'] = tweet['firstpost_date']
		obj['author'] = tweet['tweet']['user']['id']
		obj['mention'] = len(tweet['tweet']['entities']['user_mentions'])
		obj['urls'] = len(tweet['tweet']['entities']['urls'])
		obj['user_create'] = tweet['tweet']['user']['created_at']
		obj['user_allposts'] = tweet['tweet']['user']['statuses_count']

		outJson = json.dumps(obj)
		g.write(outJson)
		g.write('\n')

	print "Finish loading tweets: %s sec"%(time.time() - start)