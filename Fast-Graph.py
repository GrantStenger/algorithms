
"""
Adjacency List: For each node, store a list of all other nodes it is adjacent to

To test whether the edge (u,v) exists in an adjacency list, we need to go
through the list of all outgoing edges of u, and see if v is in that list.
That will take Θ(outdegree(u)), which can be much larger. (As we learn about
better implementations of sets later, this becomes faster, but even then, the
time will not go down to constant.)

Listing all outgoing/incoming edges of u is the specialty of adjacency lists.
Since they explicitly store this information, they just have to go through their
Set/List, which takes time Θ(outdegree(u)) or Θ(indegree(u)).

For adjacency lists, we store all incoming and all outgoing edges, so the total
storage requirement is Θ(n + m) (since we also need to store information for all
nodes). Thus, for sparse graphs, adjacency list are much more economical with
space than adjacency matrices, whereas for dense graphs, it doesn’t really
matter too much in terms of memory.
"""
class Graph_Adjacency_List:

    # Initialized the adjacancy list
    def __init__(self):
        self.adjacency_list = []

    # Adds a node with no edges
    def add_node(self):
        self.adjacency_list.append([])

    # Adds an edge from node at index i to node at index j
    # *Need to use interpolation search*
    def add_edge(self, i, j):
        if i >= len(self.adjacency_list) or j >= len(self.adjacency_list):
            raise Exception("Index out of bonds: can't add edge between " +
                            str(i) + " and " + str(j) + " because one or " \
                            + "both of those nodes don't exist.")
        else:
            # Check if edge already exists
            search_result = self.interpolation_search(self.adjacency_list[i], j)
            if type(search_result) is int:
                print("Can't add edge that already exists.")
            else:
                # If the edge does not already exist, insert j into the sorted
                # possition in i's adjacency list
                self.adjacency_list[i].insert(search_result[1], j)
                # Similarly, insert i into the sorted possition in j's list
                i_pos = self.interpolation_search(self.adjacency_list[j], i)
                self.adjacency_list[j].insert(i_pos[1], i)



    def delete_node(self, index):
        pass

    # Delete edge between node at index i and node at index j
    def delete_edge(self, i, j):
        if i >= len(self.adjacency_list) or j >= len(self.adjacency_list):
            raise Exception("Index out of bonds: can't remove edge " \
                            + "between " + str(i) + " and " + str(j) + \
                            " because one or both of those nodes don't " + \
                            "exist.")
        else:
            # Use blazing fast interpolation search to find entries to delete
            search_result = self.interpolation_search(self.adjacency_list[i], j)
            if type(search_result) is int:
                del self.adjacency_list[i][search_result]
            else:
                # The edge to delete was not found
                raise Exception("Edge to delete does not exist.")

            # Also delete i from j's adjacency list
            search_result = self.interpolation_search(self.adjacency_list[j], i)
            if type(search_result) is int:
                del self.adjacency_list[j][search_result]
            else:
                # The edge to delete was not found
                raise Exception("Edge to delete does not exist.")

    def check_edge_exists():
        pass

    def outgoing_edges():
        pass

    def adjacent_nodes():
        pass

    # Recursively search for a value in blazing fast O(log log n)
    def interpolation_search(self, arr, search_val):
        # If the array is empty, return none to signal that the search value
        # was not found, and return 0 to signal where the search val would
        # be inserted to maintain sortedness.
        if len(arr) == 0:
            return None, 0
        return self.interpolation_search_helper(arr, 0, len(arr)-1, search_val)

    # Helper function for interpolation_search()
    def interpolation_search_helper(self, arr, l, r, search_val):
        # If the search_val is not in the array, return none
        # Also return the index the seach_val would be if inserted
        if l == r and arr[l] == search_val:
            return l
        elif l == r and search_val > arr[l]:
                return (None, l+1)
        elif l == r and search_val < arr[l]:
                return (None, l)
        elif search_val < arr[l]:
            return None, l
        elif search_val > arr[r]:
            return None, r+1
        else:
            m = round((l + (r-l)) * (search_val - arr[l]) / (arr[r]-arr[l]))
            if arr[m] == search_val:
                return m
            elif search_val < arr[m]:
                return self.interpolation_search_helper(arr, l, m-1, search_val)
            else:
                return self.interpolation_search_helper(arr, m+1, r, search_val)

"""
Adjacency Matrix: Store an n × n matrix (two-dimensional array) A. In position
A[u, v], store whether there is an edge from u to v. (This could be a boolean
value, or perhaps an integer storing the length, cost, or other information.)

For adding or removing nodes, an adjacency matrix has a bit more overhead, since
changing the size of a matrix involves a bunch of reallocation and copying. For
many applications that a computer scientist is called upon to solve, changes in
the set of nodes tend to be a bit rarer while other processing is happening.

Testing whether the edge (u,v) exists in the graph is the specialty of adjacency
matrices. It only involves one lookup in a known position of a 2-dimensional
array, and thus takes O(1) time.

To list all outgoing/incoming edges of u for an adjacency matrix, we have to
loop through the entire row (or column) of the node u, and find all the entires
that are 1 or true. This will take Θ(n), which can be much worse if the degrees
are pretty small.

For the adjacency matrix, we need to store an n × n array, which obviously
requires Θ(n2) memory.
"""
class Graph_Adjacency_Matrix:

    def __init__():
        pass

    def add_node():
        pass

    def delete_node():
        pass

    def add_edge():
        pass

    def delete_edge():
        pass

    def check_edge_exists():
        pass

    def outgoing_edges():
        pass

    def adjacent_nodes():
        pass

"""
Implementation of a graph with both an adjacency list and adjacancy matrix for
extra fast lookup.

We saw above that each way of storing a graph has its own advantages and
disadvantages. If memory isn’t too big of a concern (it rarely is — computation
time is the bottleneck much more often than memory nowadays), one possible
approach is to store the entire graph twice internally. When a user queries
whether an edge (u, v) exists, we answer it by using the adjacency matrix, while
when the user queries all neighbors of a node u, we use adjacency lists.
The downside of this approach (besides using twice as much memory) is that it
requires us to execute each update to the graph twice: once on the adjacency
matrix and once on the list. Thus, update operations (such as adding or removing
nodes or edges) will take twice as long as before. However, this may well be
worth it: for many graphs, updates are much less frequent than queries. For
instance, when building a GPS, it is much rarer to have roads or intersections
added to a road network than to look for routes between two locations. Similarly,
in a social network, users add/remove friends much less frequently than reading
their friends’ updates. In those cases, the extra investment in updates is well
worth it to have faster responses in queries.
"""
class Fast_Graph:

    def __init__():
        pass

    def add_node():
        pass

    def delete_node():
        pass

    def add_edge():
        pass

    def delete_edge():
        pass

    def check_edge_exists():
        pass

    def outgoing_edges():
        pass

    def adjacent_nodes():
        pass

    def BFS():
        pass

    def DFS():
        pass

def main():
    graph = Graph_Adjacency_List()
    print(graph.adjacency_list)
    graph.add_node()
    print(graph.adjacency_list)
    graph.add_node()
    print(graph.adjacency_list)
    graph.add_node()
    print(graph.adjacency_list)
    graph.add_edge(1, 0)
    print(graph.adjacency_list)
    graph.add_node()
    print(graph.adjacency_list)
    graph.add_node()
    print(graph.adjacency_list)
    graph.add_edge(1, 4)
    print(graph.adjacency_list)
    graph.add_edge(2, 4)
    print(graph.adjacency_list)
    graph.add_edge(1, 0)
    print(graph.adjacency_list)
    graph.add_node()
    print(graph.adjacency_list)
    # print(graph.adjacency_list)
    graph.delete_edge(0, 1)
    print(graph.adjacency_list)
    # a = [4, 13, 16, 29, 33, 42, 51, 53, 66, 69, 74, 80, 88, 89, 97, 100]
    # print(graph.interpolation_search(a, 68))

if __name__ == "__main__":
    main()
