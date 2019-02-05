---
author:
- Grant Stenger
date: 'January 18, 2019'
title: 'ISE 632 Problem Set \#1'
---

1.  **Prove that at least one of $G$ and $\overline{G}$ is connected.**
    Assume $G$ is disconnected. It follows that there are at least two
    subgraphs $G_{1}$ and $G_{2}$ that collectively form $G$ that have
    no connections between each other. Consider arbitrary vertices
    $v_{1}$ in $G_{1}$ and $v_{2}$ in $G_{2}$. By construction, $v_{1}$
    has no edges to any vertices in $G_{2}$. Similarly, $v_{2}$ has no
    edges to any vertices in $G_{1}$. It follows that $v_{1}$ will be
    connected to every vertex in $\overline{G}_{2}$ and $v_{2}$ will be
    connected to every vertex in $\overline{G}_{1}$ including $v_{1}$.
    Therefore, because every vertex in $\overline{G}_{1}$ is connected
    to $v_{2}$ and every vertex in $\overline{G}_{2}$ is connected to
    $v_{1}$ and $v_{1}$ is connected to $v_{2}$, there must be a path
    between any two vertices in $\overline{G}$ through $v_{1}$ and/or
    $v_{2}$. Hence, the complement of any arbitrary disconnected graph
    must be connected. Thus, at least one of $G$ and $\overline{G}$ is
    connected. $\blacksquare$

2.  **Prove that there always exists a perfect matching consisting of
    line segments between the members of a set of $n$ distinct red
    points and the members of a set of $n$ distinct blue points such
    that no edges cross each other.**

    1.  Call $S$ the set containing the final edges that will comprise
        the solution set. $S$ is initially empty.

    2.  Given a set of $k$ distinct red points and $k$ blue points,
        consider the set of all possible edges connecting a red to a
        blue point. From this set of edges, it is always possible to
        find an 'outside edge' which is not intersected. This can be
        shown inductively.

        1.  Consider two red and two blue points. There trivially exist
            two non-intersected 'outside edges' that connect a red and
            blue point. Thus, the base case is proven.

        2.  For the inductive step, consider a set of $k-1$ red and
            $k-1$ blue points with at least one non-intersected 'outside
            edge'. Arbitrarily add a new blue and red point and make the
            necessary new connections. If the previous 'outside edge' is
            not intersected, the condition still holds. If the new red
            and blue points do intersect the 'outside edge', connecting
            the outermost new point with its opposite color from the
            previous outside edge forms a new outside edge. Thus, if a
            $k-1$ set has an outside edge any $k$ set also has one, and
            the inductive step is proven.

        3.  Hence, it has been inductively shown that there is always an
            'outside edge' which is not intersected.

    3.  Add this 'outside edge' to $S$ and repeat steps b and c on the
        subset of $k-1$ red points and $k-1$ blue points which do not
        include the vertices of the removed 'outside edge' until only a
        red and a blue point remain.

    4.  The edge created from these last two points will not intersect
        any other edges because we have repeatedly selected edges which
        cannot possibly be intersected by any other edges in their
        subset. This remained invariant until no edges remained. Hence,
        it is proven that there always exists a perfect matching
        consisting of line segments between members of $n$ blue and red
        points such that no edges cross each other. $\blacksquare$

3.  **Prove that the edges of a regular bipartite network ${\cal G}_{d}$
    where all nodes have degree $d\geq1$ can be decomposed into $d$
    disjoint perfect matchings.** Note Hall's Matching Theorem: Let
    $G=(U\cup W,E)$ be a bipartite graph with $|U|=|W|$. Then a perfect
    matching of $G$ exists if and only if $|S|\leq|N(S)|$ for all
    $S\subset W$. Because ${\cal G}_{d}$ is a regular bipartite network,
    $|S|=|N(S)|$ for all $S\subset W$ by definition. It follows that a
    perfect matching exists. Removing this perfect matching decreases
    each node's degree by exactly 1. The new regular bipartite network
    ${\cal G}_{d-1}$ also contains a perfect matching by Hall's Theorem.
    It is clear that we can inductively remove a perfect matching from
    each subgraph resulting in $d$ distinct perfect matchings.
    $\blacksquare$

4.  **Can Figure 1 be tiled with $2\times1$ rectangles?** Paint the
    figure in a checkerboard fashion. Notice the highlighted region in
    Figure 1. Each time a rectangle is placed, it must lay on both a
    blue and a black square. Notice that there are 11 blue squares in
    this region and only 10 black squares which can be matched with
    them. By pigeonhole principle, it is impossible for all 11 blue
    squares to be tiled by rectangles which must simultaneously cover a
    unique adjacent black square. Thus, it is impossible to tile this
    figure with $2\times1$ rectangles. $\blacksquare$

5.  **True or False Gale-Shapley Problems**

    1.  It is true that an instance of the stable marriage problem has a
        unique stable matching if and only if the version of the
        Gale-Shapley algorithm where the man proposes and the version
        where the woman proposes both yield the exact same matching.

        1.  **Proof that, if both versions yield the same matching, then
            the instance of the stable matching problem has a unique
            stable matching:** When the men propose, every execution of
            the Gale-Shapley algorithm results in every man being paired
            with his best valid partner. Similarly, every woman is
            paired with her least favorite valid partner. The proof of
            this is well known. Conversely, when the women propose,
            every execution results in every woman being paired with her
            best valid partner and every man being paired with his least
            favorite valid partner. If both the men-proposing and
            women-proposing versions yield the same matching, every man
            must simultaneously be paired with his best valid option and
            worst valid optionand likewise for the women. Because each
            ranking is distinct and ordered, there must only be one
            valid option per man and woman. Thus, this instance of the
            stable matching problem has only one unique solution.

        2.  **Proof that if an instance of the stable marriage problem
            has a unique stable matching, then both versions yield the
            same matching:** Assume for contradiction that an instance
            of the stable marriage problem has one unique stable
            matching and that running the men-propose and women-propose
            versions of the algorithm results in two different
            matchings. Because the Gale-Shapley algorithm always results
            in stable matches, the men-propose and women-propose
            matchings must be stable matches. However, by assumption,
            there is only one stable matching. Thus, if an instance of
            the stable marriage problem has a unique stable matching, it
            must be that both the men-propose and women-propose versions
            of the algorithm result in the same matching. $\blacksquare$

    2.  Consider an instance of the stable marriage problem where there
        is one man $m$ who is every woman's least favorite, and one
        woman $w$ who is every man's least favorite. Assume for
        contradiction that the Gale-Shapley algorithm does not match $m$
        with $w$. This means $m$ is matched with a woman $w'$ who he
        prefers to $w$. Assuming there are an equal number of men and
        women, there must be a man $m'$ who either asks $w'$ to be
        engaged before $m$ proposes to her or after. Regardless, because
        $w'$ prefers any man to $m$, she accepts $m'$'s proposal and
        rejects $m$. However, this is a contradiction, because by
        assumption $m$ is matched to woman $w'$. Thus, the Gale-Shapley
        algorithm must match $m$ with $w$. $\blacksquare$

![Region to tile](/Users/Home/Desktop/ISE632HW1Fig1)
