The following are weak stability conditions, but subgraphs DO have cycles.
Which are used in analysis_cycles.ipynb

cycle_analysis_all contains all summarising text files.


File Description:

graphname.pkl
Stored list of stability conditions in the form of tuples of the form, 
assignments,line bundle multidegree data, subgraphs and cycles with translator trees.

graphname.txt
Visual description of pkl data.

graphname_dlist.pkl
a list of dictionaries, one for each stability condition. Where each dict records the cycle on a subgraph with a maximal necklace and the cycles on the other subg with maximal necklaces.

graphname_summary_dlist.pkl
analyses graphname.pkl in analysis_cycles_2.ipynb

graphname_cycle_analysis.txt
Summarises the results of the above.