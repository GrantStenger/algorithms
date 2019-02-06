# Algorithms

Notes mainly from ISE 632 Network Flows and Combinatorial Optimization.

I'm currently implementing a fast graph structure to test these algorithms on. In order to have ~blazing fast~ look up of both node/edge existence/weights and all adjacent nodes / outgoing edges, I've used both an adjacency list and adjacency matrix for internal graph representation. The trade offs are increased storage space and slower graph updates. These trade off will make sense for some algorithms and will not for others. For algorithms that rely heavily on graph updates, I will likely use a more effective data structure (i.e. either an adjacency list or an adjacency matrix, depending on my needs). I'm not working with huge datasets in my exploration, so storage space is more or less a nonissue. I've also used interpolation search for all of my lookups which grabs data in Θ(log log n).
