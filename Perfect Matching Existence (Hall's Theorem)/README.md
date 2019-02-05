# Perfect Matching Existence

*Given a bipartite graph, does a perfect matching exist?*

### Background

Recall that a _**bipartite network**_ is a network $G=(V,E)$ in which we can partition the vertices into two disjoint sets, $V=U\cup W$, such that each edge consists of a pair $(u,w)$ with $u\in U$ and $w\in W$.

A _**matching**_ is a subset of edges such that no two edges share a vertex.

A **_perfect matching_** is a matching that touches every vertex (need $|U|=|W|$ in the bipartite case).

### Hall's Matching Theorem

Let $G=(U\cup W, E)$ be a bipartite graph with $|U|=|W|$. Then a perfect matching of $G$ exists if and only if $|S|\leq |N(S)|$ for all $S\subset W$.

##### Proof

- If a network has a _**constricted set**_, then no perfect matching exists.
  - Given a subset of vertices $S\subset W$, the _**neighbor set**_ N(S) is the set of all neightbors of the elements of $S$. The set $S$ is _**constrited**_ if $|S|\less |N(S)|$.
  - If there exists a set $S\subset W$ such that $|S|\greater |N(S)|$, then a perfect matching does not exist.
- It will suffice to prove the converse: “if a perfect matching does not exist, then there exists a constricting set”
  - If no perfect matching exists, let $M$ be a _**maximum matching**_ that pairs up as many vertices as possible.
  - Let $u\in U$ be a vertex that is _**unmatched**_ by $M$.
  Consider the set of all network paths that start at $u$ and alternate between edges in $M$ and edges not in $M$; call this set $\mathbb P$, the _**alternating paths**_.
  - Claim: if a vertex (other than $u$) is in $\mathbb P$, then so is its matched partner from $M$
  - ...
