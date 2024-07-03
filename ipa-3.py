'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # from -> to : following?
    if to_member in social_graph[from_member]["following"]:
        from_to = True
    else:
        from_to = False
    
    # to -> from : following?
    if from_member in social_graph[to_member]["following"]:
        to_from = True
    else:
        to_from = False

    if from_to and to_from:
        return "friends"
    elif to_from:
        return "followed by"
    elif from_to:
        return "follower"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    is_winner = False
    winner = ""

    # columns
    for i in range(len(board)):
        col = [row[i] for row in board]
        if col.count("X") == len(board):
            winner = "X"
            is_winner = True
        elif col.count("O") == len(board):
            winner = "O"
            is_winner = True
        else:
            pass
    
    # rows
    for i in board:
        if i.count("X") == len(board):
            winner = "X"
            is_winner = True
        elif i.count("O") == len(board):
            winner = "O"
            is_winner = True
        else:
            pass 

    # decline diagonal
    decline = [board[0][0]]
    i = 1
    while i < len(board):
        decline.append(board[i][i])
        i += 1

    # inline diagonal
    incline = [board[len(board)-1][0]]
    i = 1
    while i < len(board):
        row_ind = len(board) - (i + 1)
        incline.append(board[row_ind][i])
        i += 1

    for i in decline:
        if decline.count("X") == len(board):
            winner = "X"
            is_winner = True
        elif decline.count("O") == len(board):
            winner = "O"
            is_winner = True
        else:
            pass 

    for i in incline:
        if incline.count("X") == 3:
            winner = "X"
            is_winner = True
        elif incline.count("O") == 3:
            winner = "O"
            is_winner = True
        else:
            pass 
    
    if is_winner:
        return winner
    else:
        return "NO WINNER"
  

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    time = 0

    if (first_stop,second_stop) in route_map:
        time = route_map[(first_stop,second_stop)]["travel_time_mins"]
        return time
    else:
        routes = list(route_map.keys()) # list of routes available
        starting_points = [x[0] for x in routes] # list of starting points
        
        leg_index = starting_points.index(first_stop) # finds index of first_stop
        destination = routes[leg_index][1] # finds end point of availble connecting route
        next_route = routes[leg_index] # finds key of next connecting route

        time += route_map[next_route]["travel_time_mins"]

        while destination != second_stop:
            origin = next_route[1] # string of previous destination
            leg_index = starting_points.index(origin) # finds index of previous route's destination
            destination = routes[leg_index][1] # finds end point of availble connecting route
            next_route = routes[leg_index] # finds key of next connecting route

            time += route_map[next_route]["travel_time_mins"]
    
    return time