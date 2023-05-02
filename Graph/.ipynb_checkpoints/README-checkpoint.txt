Let $G$ be a graph with no separating edges or vertices, and $\tilde{G}$ be the set of subgraphs of $G$, of the the form $T \cup e$ for $T \in \mathcal{ST}(G)$ and $e \in G \setminus T$.

Here we describe a method to get Assignments for any graph (using $\theta$ map)

1) Let $M=[]$ (records the pairs (tree,assignment)=(T,Ass(T))) we will build this set up.

2) Choose a tree of G and take the let $Ass(T)=\underline{0}$ on it, add this to $M$.

3) For counter Run Exhaustive_Method below for M[counter] for $T$. (counter remembers which pairs of M we have done (appending))

Exhaustive_method

    1) Consider M[counter]==(T,Ass(T))
    2) Consider all $G_0 \in \tilde{G}$ that contain $T$.
    3) For each $G_0^{'}$ consider the subnecklace.
        4) Choose a cycle $\tau$ for this subnecklace (genus $1$ method to calculate assignments).
        
        5) Using $\tau$ get all (Tree,assingment) pairs for In and relabel Tree of In to trees of the subnecklace of subg.
        
        6) extend assingments for $I_n$ to non-tranlsated $Ass(T^{'})$ for all $T^{'} \in \mathcal{ST}(G_0^{'})$. Then tranlsate 
        $Ass(T^{'})$ by $Ass(T)$.
        
        7) Consider $(T^{'},Ass(T^{'}))$ append to $M$ with respect to $T^{'}$. Increasing the size of $|Ass(T^{'})|$ if 
        necessary.
        8) Check if, for $M$ we have $|Ass(T)|=1$ for all $T$. if not we need to choose anothe cycle.
    9)If $|M|=k(\Gamma)$ end and return $M$.#
    
10) Else take counter+=1 and rerun Exhaustive_method

11) Output will be $M$ of the correct size and which $|Ass(T)|=1$ for all $T$. It remains to put into the correct order then apply w_stability.

More details: 

    4) 
    - Given a n cycle can get a set of assignments and trees for $I_n$. (DONE)
    - This gives us (assignment,tree) data for trees that make up the subnecklace. (DONE)
    5)
    - We relabel the (assignment,tree) data of $I_n$ so that it corresponds to the subnecklace of the subgraph (TODO)
    - For the trees we add back the tails of the subgraph relative to the subnecklace. (TODO)
    
    6)
    - For the assignments we extend by 0 on tail vertices to get temporary assignment. (DONE)
    - Then translate the temporary assignments by the known assignment on the common tree given by $M[counter]. (DONE)
    7) 
    - Append this new data.
    8)
    - Ask if that cycle is a good choice.
    11) 
    -Method that take Ass_gamma and orders trees to we can check total size. (DONE)