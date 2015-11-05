# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# -----------------------------------------------------------------------------

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know
# what they are doing, having taken our web development class). However, it is
# up to you to create a data structure that manages the game-network information
# and to define several procedures that operate on the network.
#
# In a website, the data is stored in a database. In our case, however, all the
# information comes in a big string of text. Each pair of sentences in the text
# is formatted as follows:
#
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
#
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner
#
# Note that each sentence will be separated from the next by only a period. There will
# not be whitespace or new lines between sentences.
#
# Your friend records the information in that string based on user activity on
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below.
#
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged
# to define any additional helper procedures that can assist you in accomplishing
# a task. You are encouraged to test your code by using print statements and the
# Test Run button.
# -----------------------------------------------------------------------------

# Example string input. Use it to test your code.
example_input = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# -----------------------------------------------------------------------------
# create_data_structure(string_input):
#   Parses a block of text (such as the one above) and stores relevant
#   information into a data structure. You are free to choose and design any
#   data structure you would like to use to manage the information.
#
# Arguments:
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not
#   list B's connections or liked games.
#
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.


def create_data_structure(string_input):
    friends_split = ' is connected to '
    games_split = ' likes to play '
    input_string = [s.strip() for s in string_input.split('.') if s != '']
    # split string into list and filter empty strings
    network = {}
    for line in input_string:
        if friends_split in line:
            username, connections = line.split(friends_split)  # split line into username and connections
            if username not in network:
                network[username] = {'Connections': [], 'Games': []}  # add empty dictionaries if user is not in network
            network[username]['Connections'] = [s.strip() for s in connections.split(',')]

        else:
            username, games = line.split(games_split)  # split line into username and games
            if username not in network:
                network[username] = {'Connections': [], 'Games': []}  # add empty dictionaries if user is not in network
            network[username]['Games'] = [s.strip() for s in games.split(',')]
    return network

# Creates a dictionary of users, their connections, and their favorite games
# from a string using the strip and split methods.

# network = create_data_structure(example_input)
# print network

# ----------------------------------------------------------------------------- #
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        #
# ----------------------------------------------------------------------------- #

# -----------------------------------------------------------------------------
# get_connections(network, user):
#   Returns a list of all the connections that user has
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.


def get_connections(network, user):
    if user in network:
        return network[user]['Connections']
    else:
        return None

# Returns a user's connection list based upon the user parameter specified
# in the function input

# print get_connections(network, 'John')
# print get_connections(network, 'Adam')

# -----------------------------------------------------------------------------
# get_games_liked(network, user):
#   Returns a list of all the games a user likes
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.


def get_games_liked(network, user):
    if user in network:
        return network[user]['Games']
    else:
        return None

# Returns a user's favorite games list based upon the user parameter specified
# in the function input

# print get_games_liked(network, 'John')
# print get_games_liked(network, 'Adam')

# -----------------------------------------------------------------------------
# add_connection(network, user_A, user_B):
#   Adds a connection from user_A to user_B. Make sure to check that both users
#   exist in network.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return:
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.


def add_connection(network, user_a, user_b):
    if (user_a not in network) or (user_b not in network):
        return False
    if user_b not in get_connections(network, user_a):
        get_connections(network, user_a).append(user_b)
    return network

# Adds a connection to a user's connection list after checking that the user
# to be added is not already present in the user's connection list. If either
# of the users specificed in the input are not in the network returns False. If
# the user to be added is already in the user to be checked list returns network
# without changes. Otherwise adds user to be added to user to be checked list
# and returns updated network.

# add_connection(network, 'John', 'Mercedes')
# print add_connection(network, 'John', 'Walter')
# print add_connection(network, 'John', 'Adam')
# print get_connections(network, 'John')

# -----------------------------------------------------------------------------
# add_new_user(network, user, games):
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no
#   connections to begin with.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#   ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return:
#   The updated network with the new user and game preferences added. The new user
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)


def add_new_user(network, user, games):
    if user not in network:
        network[user] = {'Connections': [], 'Games': games}
    return network

# Adds a new user to the network as long as an entry for that user does not
# already exist. Does nothing and returns network as is if the user already
# exists in the network.

# add_new_user(network, 'John', ['FIFA 15'])
# add_new_user(network, 'Adam', ['FIFA 15', 'Dragon Age: Inquisition'])
# print network

# -----------------------------------------------------------------------------
# get_secondary_connections(network, user):
#   Finds all the secondary connections (i.e. connections of connections) of a
#   given user.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
#
# NOTE:
#   It is OK if a user's list of secondary connections includes the user
#   himself/herself. It is also OK if the list contains a user's primary
#   connection that is a secondary connection as well.


def get_secondary_connections(network, user):
    if get_connections(network, user) is None:
        return None
    connections = get_connections(network, user)
    result = []
    for person in connections:
        person_to_check = get_connections(network, person)
        for friend in person_to_check:
            if friend not in result:
                result.append(friend)
    return result

# Creates a list of people that a specificed user's connections are themselves
# connected to. If the specified user is not in the network returns None. If
# the specified user has no connections returns an empty list. Otherwise returns
# a list of all the people the specified users connections are connected to.

# print get_secondary_connections(network, 'Adam')
# add_new_user(network, 'Adam', ['FIFA 15', 'Dragon Age: Inquisition'])
# print get_secondary_connections(network, 'John')

# -----------------------------------------------------------------------------
# connections_in_common(network, user_A, user_B):
#   Finds the number of people that user_A and user_B have in common.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.


def connections_in_common(network, user_a, user_b):
    if (get_connections(network, user_a) is None) or (get_connections(network, user_b) is None):
        return False
    lista = get_connections(network, user_a)
    listb = get_connections(network, user_b)
    count = 0
    for person in lista:
        if person in listb:
            count += 1
    return count

# Returns an integer value for the number of connections that two users have
# in common. If either user specified in the input is not in the network returns
# None. Otherwise, creates a list of each users connections and counts the
# values in common.

# print connections_in_common(network, 'John', 'Walter')

# -----------------------------------------------------------------------------
# path_to_friend(network, user_A, user_B):
#   Finds a connections path from user_A to user_B. It has to be an existing
#   path but it DOES NOT have to be the shortest path.
#
# Arguments:
#   network: The network you created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam,
#   who is connected with Zed.
#
# NOTE:
#   You must solve this problem using recursion!
#
# Hints:
# - Be careful how you handle connection loops, for example, A is connected to B.
#   B is connected to C. C is connected to B. Make sure your code terminates in
#   that case.
# - If you are comfortable with default parameters, you might consider using one
#   in this procedure to keep track of nodes already visited in your search. You
#   may safely add default parameters since all calls used in the grading script
#   will only include the arguments network, user_A, and user_B.


def path_to_friend(network, start, end, path=None):
    if (get_connections(network, start) is None) or (get_connections(network, end) is None) or (start == end):
        return None
    if path is None:
        path = []
    path = path + [start]
    if end in get_connections(network, start):
        return path + [end]
    for node in get_connections(network, start):
        if node not in path:
            newpath = path_to_friend(network, node, end, path)
            if newpath:
                return newpath
    return None

# If possible, uses a recursive function to trace a path between two users in
# network. If no such connection exists, returns None.

# Make-Your-Own-Procedure (MYOP)
# -----------------------------------------------------------------------------


def add_game(network, user, game):
    if get_connections(network, user) is None:
        return False
    elif game in get_games_liked(network, user):
        return "%s already likes %s." % (user, game)
    else:
        network[user]['Games'].append(game)
        return get_games_liked(network, user)

from collections import Counter

def top_5_games(network):
    all_games = []
    for user in network:
        all_games.append(network[user]['Games'])
    all_games = sum(all_games, [])
    return Counter(all_games).most_common(5)

# Creates a flat list of all the games in users 'Games' dictionaries. Uses the
# sum function to create a tuple of games and the number of instances of that
# game. Uses the coutner module on that list of tuples to return the top 5 with
# the highest occurence.

# net = create_data_structure(example_input)
# print net
# print get_connections(net, "Debra")
# print get_connections(net, "Mercedes")
# print get_games_liked(net, "John")
# print add_connection(net, "John", "Freda")
# print add_new_user(net, "Debra", [])
# print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
# print get_secondary_connections(net, "Mercedes")
# print connections_in_common(net, "Mercedes", "John")
# print path_to_friend(net, "Ollie", "Jennie")
# print add_game(net, 'John', 'FIFA 15')
# print add_game(net, 'John', 'The Legend of Corgi')
# print add_game(net, 'Adam', 'FIFA 15')
# print top_5_games(net)
