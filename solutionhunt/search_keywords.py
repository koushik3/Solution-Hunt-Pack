#return = list of (search_keyword, results_list)
#
from gsearch.googlesearch import search

def search_keywords(key_list, type):
	N = len(key_list)
	key_list=[ 'solution scoutingit', 'keyword list', 'search', 'information.the end user' , 'relevance ’', 'tool', 'solution scouting.the list', '95% accuracy expected.it', 'keyword', 'performed.the end user', 'tool /application', 'controlledthe search', 'challenge uploaded', '‘ extent',  'information', 'web.the information']
	N = len(key_list)
	
	if(type == 1):
		results = []
		for j in range(0, N, 3):
			search_query = str(key_list[j])+' '+str(key_list[(j+1)%N])+' '+str(key_list[(j+2)%N])
			res = search(search_query, num_results = 5)
			res_tup = (search_query, res)
			results.append(res_tup)
			break
	elif(type == 2):
		results = []
		for j in range(0, N, 3):
			search_query0 = str(key_list[j])+' '+str(key_list[(j+1)%N])
			search_query1 = search_query0 +' '+ str(key_list[(j+2)%N])
			search_query2 = search_query1 +' '+ str(key_list[(j+3)%N])

			res_tup0 = (search_query0, search(search_query0, num_results = 5))
			res_tup1 = (search_query1, search(search_query1, num_results = 5))
			res_tup2 = (search_query2, search(search_query2, num_results = 5))
			
			results.append(res_tup0)
			results.append(res_tup1)
			results.append(res_tup2)
	elif(type == 3):
		results = []
		for j in range(0, N, 3):
			search_query0 = str(key_list[j])
			search_query1 = search_query0 +' '+	str(key_list[(j+1)%N])
			search_query2 = search_query0 +' '+ str(key_list[(j+2)%N])
			search_query3 = search_query1 +' '+ str(key_list[(j+3)%N])
			search_query3 = search_query1 +' '+ str(key_list[(j+4)%N])
			
			res_tup0 = (search_query0, search(search_query0, num_results = 5))
			res_tup1 = (search_query1, search(search_query1, num_results = 5))
			res_tup2 = (search_query2, search(search_query2, num_results = 5))
			res_tup3 = (search_query3, search(search_query3, num_results = 5))
			res_tup4 = (search_query4, search(search_query4, num_results = 5))

			results.append(res_tup0)
			results.append(res_tup1)
			results.append(res_tup2)
			results.append(res_tup3)
			results.append(res_tup4) 
	print(results)
	return results

print (search_keywords(['A', 'B', 'C', 'D', 'E'], 1))