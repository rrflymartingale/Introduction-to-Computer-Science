def create_data_structure(string_input):
	if string_input=='':return {}
	network={}
	string_input=string_input.split('.')
	s=string_input[:-1]
	n=len(s)
	for j in range(0,n,2):
		network[s[j].split('is connected to')[0].split()[0]]=[[i.strip() for i in s[j].split('is connected to')[1].split(',')],[i.strip() for i in s[j+1].split('likes to play')[1].split(',')]]
	return network 	
	
def get_connections(network, user):
	if user not in network:return None
	return network[user][0]
	
def get_games_liked(network,user):
	if user not in network:return None
	return network[user][1]
	
def add_connection(network, user_A, user_B):
	if user_A not in network:return False
	if user_B not in network:return False
	if user_B in network[user_A][0]:return network
	else:
		network[user_A][0].append(user_B)
		return network
		
def add_new_user(network, user, games):
	if user in network:return network
	else:
		network[user]=[[],games]
		return network
		
def get_secondary_connections(network, user):		
	if user not in network:
		return None
	first_connection=network[user][0]
	output=[]
	if first_connection:
		for i in first_connection:
			output=output+network[i][0]	
	else:return []
	
def connections_in_common(network, user_A, user_B):
	if user_A not in network or user_B not in network:return False
	connectionA=get_connections(network,user_A)
	connectionB = get_connections(network,user_B)
	output=[]
	for i in connectionA:
		if i in user_B:
			output.append(i)
	return len(output)
	
def path_to_friend(network, user_A, user_B):
	if user_A not in network or user_B not in network:return None
	outout=[]
	first_connection=network[user_A][0]
	if user_B in first_connection:
		return output.append(user_A,user_B)
	else:	
		for i in first_connection:
			output.append(user_A)
			return output+path_to_friend(network, i, user_B)
			
def top5_games(network):
	output={}
	for p in network:
		game_list=network[p][1]
		for i in game_list:			
			output[i]=0
	for p in network:
		game_list=network[p][1]
		for i in game_list:			
			output[i]=output[i]+1
