import random
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")
        # Create friendships

        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id+ 1, len(self.users.keys()) + 1):
                possible_friendships.append((user_id, friend_id))
                
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            
    def populate_graph_linear(self, num_users, avg_friendships):
            # THIS IS A MORE OPTIMAL ALGORITHM TO GENERATE A RANDOM GRAPH
        # the basic algorithm is actually quite simple 
            # Pick 2 random numbers between 1 and last user ID
            # Try to create that friendship
            # If it succeeds, increment the friendship counter
            # If not, increment a collisions counter
            # Repeat until target friendships are created
        # This is more optimal if the we do not get many collisions
        # We generally will not get TOO many collisions if the graph is not too dense (not a lot of average friendships)
        # However, as the graph density increases, this algorithm essentially ends up generating ALL friendships anyways
        # Which makes it equal to the populate_graph function
        # However, on average this should be better 

        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.addUser(f"User {i+1}")

        target_friendships = (num_users * avg_friendships)
        total_friendships = 0
        collisions = 0
        # Keep trying friendships until we create enough of them
        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
        # The higher this number is, the less performant our runtime was
        print(f"COLLISIONS: {collisions}")


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        queue=Queue()
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue.enqueue([user_id])
        
        while queue.size() > 0:
                # Dequeue a current path
            current_path = queue.dequeue()
            # Get the current vertex from end of path
            current_vertex = current_path[-1]
            if current_vertex not in visited:
                # add vertex to visited_set
                # ALSO add the PATH that brought us to this vertex
                # i.e add a key and value to the visited Dictionary
                #   the key is the current vertex, and the value is the path 
                visited[current_vertex] = current_path

                # queue up all neighbors as paths
                for neighbor in self.friendships[current_vertex]:
                    # make a new copy of the current path
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
