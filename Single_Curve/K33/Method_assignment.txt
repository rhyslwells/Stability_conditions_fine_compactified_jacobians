Here we describe a method, for any graph, to obtain a single assignment (unique assignment for each tree) which can be checked, by adding break divisors, if it is also a a stability condition.

Let $G$ be a graph with no separating edges or vertices, and $\tilde{G}$ be the set of subgraphs of $G$, of the the form $T \cup e$ for $T \in \mathcal{ST}(G)$ and $e \in G \setminus T$. For any $T \cup e$, we refer to the subnecklace of $T \cup e$ as the the largest cyclic subgraph.

The following method proceeds by exhuastively searching (by choosing an appropriate cycle for the subnecklace of some $T \cup e$) and then adding assignments for each tree to a set of assignments we know which work. The output will be an assignment $M$ of the size $k_G$ and forwhich $|Ass(T)|=1$ for all $T$.

Initialisation:
1) Let $M=[]$ (which records sets of pairs (tree,assignment)).
1.1) Choose a tree T of G and let $Ass(T)=\underline{0}$, add $(T,Ass(T))$ to $M$.

2) Now iterate through trees $T'$ which are in $M$ (there is no need to repeat trees). And apply the method below to each.

Method:

1) Consider (T',Ass(T')) in M.
    2) Consider all $G_0 \in \tilde{G}$ that contain $T'$.
    3) For each $G_0$ consider the subnecklace (The subnecklace can be modeled by In, we will use the genus 1 calculation).
        
        4) Choose a cycle $\tau$ for In (if it does not provide unique assignments return to this step).
        
            5) Using $\tau$ get all (T,Ass(T)) pairs for In (genus $1$ method to calculate assignments).
            
            6) Note the tree of In that is the same as T'(but without vertices outside of the subnecklace) will have Ass(T)=0.
        
            6) For T of In add back edges of $G_0$ not in the subnecklace. And then relabel T of In to T of the subnecklace of subg.
        
            6) Extend Ass(T) of $I_n$ to non-tranlsated Ass(T) on $G_0$ by adding 0 to the vertices of subg not in the subnecklace.
        
            7) Tranlsate the extended but non-tranlsated Ass(T), by Ass(T').
        
            7) Add (T,Ass(T)) to $M$. Increasing the size of $|Ass(T)|$ if necessary.
        
            8) Check if, for $M$ we have $|Ass(T)|=1$ for all $T$ to which we know. If not choose another cycle.
            
    9)If $|M|=k(\Gamma)$ end and return $M$.
    
10) Return to step 1) and choose a different tree in M.