In this folder I obtain and then analyse cycles on subgraph of the form T \cup e. 

find_cycles:
Desc: We obtain data that from examples. This data contains a list of (subg,cycle,tree) for each stability condition. We store the output in Done_examples.

Analyse_cycles and Analyse_cycles_2:
Descr: We study the examples in Done_examples. In particular focusing on cycles of subgraphs T \up e which contain a maximal necklace.


ISSUES:
- What about Z2 action on cycles, see get_leaves.

Would like to do:
	- plot subgraphs with cycles too.
Cant do currently:
	- Add assignments onto trees at vertices (cant label vertices)
		- Present tree with assignments nicely plotted
Notes:
For graphs in general we should label in a standardised way:
	- Label a max necklace first 1,..,n