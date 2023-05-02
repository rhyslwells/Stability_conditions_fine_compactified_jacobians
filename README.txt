This package has been created by Rhys Wells. It contains analysis of stability conditions of generalised break divisors on a graph and mildly superadditive functions (See Papers).

In both cases we construct non-trival examples and conduct analysis of the results of which are discussed in Rhys's PhD thesis "Combinatorics of stability conditions of generalised break divisors" (See Papers).

------------------------------------------------------------------

In Graph:

We produce examples of such stability conditions, in genus 2 especially, and conduct analysis on the associated phi stability space. Additionally we give a method to construct any genus 1 stability conditions from a cycle.

In MSA:

We construct the set of mildly superadditive functions up to translation, Pn, up to n=6 (See Papers). And conduct analysis on Pn.
------------------------------------------------------------------

If you are interested in helping, here are a few issues I think would be productive to investigate:

	- Construct a class for the notion of a stability conditions for any graph for a prescribed set of assignments. Finding good choices of assignments is the hard part.

	- Implement a fast method to get all stability condition for a graph.
	
	- Check if $\sigma_{\Gamma}(\Gamma)$ is always a complete set of representatives for the chip-firing action on the graph.

If you have questions or suggestions or if you find bugs, let me know.

rhyslwells@outlook.com

------------------------------------------------------------------

Files of Note (chronological order of appearance in thesis):

Folder: introduction
Description: Introduces stability conditions. Give examples of pictures showing $sigma_{\Gamma}^{A}(\Gamma)$ as $A$ varies.
Main file: \Stability_Conditions\Graph\BasicExamples.ipynb

Folder: genus_1_graphs
Description: Gives stability condntions for genus 1 graphs from a cycle.
Main file: \Stability_Conditions\Graph\genus_1_graphs\Cycles_to_weakstab.ipynb"

Folder: circular_intersect
Description: Examples of inclusion exclusion intersection numbers of patches of sigma(\Gamma) as vary divisor on tree.
Main file: \Stability_Conditions\Graph\circular_intersect\Overlap_Analysis.ipynb

Folder: graph_stability_conditions
Description: Using an exhaustive method get all weak stability conditions up to translation. For GNkM1 graphs we extend the genus 1 case. 
Main files: 
\Stability_Conditions\Graph\graph_stability_conditions\assignments.ipynb
\Stability_Conditions\Graph\graph_stability_conditions\wsc_k_edge_g_1.ipynb"

Folder: phi_investigation
Description: Investigate what phi determine the weak stability conditions.
Main file: \Stability_Conditions\Graph\phi_investigation\phi_analysis.ipynb

Folder: find_cycles
Description: Obtain and then analyse cycles on subgraphs of the form T \cup e for a given weak stability condition.
Main files:
 \Stability_Conditions\Graph\find_cycles\find_cycles.ipynb
\Stability_Conditions\Graph\find_cycles\analyse_cycles.ipynb

Folder: MSA
Description: Calculate Pn up to n=6
Main file: \Stability_Conditions\MSA\Pn.ipynb




