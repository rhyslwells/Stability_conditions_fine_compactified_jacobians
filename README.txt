This package has been created by Rhys Wells. It contains analysis of stability conditions for fine compactified jacobians for single and universal curve cases (See Papers).

Both cases we construct non-trival examples. And conduct analysis of the results of which are discussed in Rhys's PhD thesis "Combinatorics of stability conditions of Fine Compactified Jacobians" (See Papers).

------------------------------------------------------------------

In Single curve:

We follow definition ref in the "Nicolas new paper" (See Paper). We produce small examples of stability conditions in genus 2, and conduct analysis on the associated phi stability space. Additionally we give a method to construct any genus 1 stability conditions from a cycle described in "Geometry of genus one fine Compactified Jacobians" (See Papers).

In Universal curve:

We construct the set of mildly superadditive functions, Pn, up to n=5, as described in "Geometry of genus one fine Compactified Jacobians" (See Papers). And conduct analysis on Pn by following Proposition 2.12 in the above paper.

------------------------------------------------------------------

Each folder contains a Readme describing the most relevant script.

If you are interested in helping, here are a few issues I think would be productive to investigate:

	- Construct the class for stability conditions in "Single Curve".

	- Implement a method to get any genus 2 stability condition, using ideas of "higher_genus_2_graphs".

	- Improve the computation speed of obtaining Pn for n more than 5, possibly using Cpp.

If you have questions or suggestions or if you find bugs, let me know.

rhys.wells@liverpool.ac.uk

------------------------------------------------------------------

Folder:Introduction
Description: Introduces stability conditions. Give examples of pictures of changing top set of sigma(\Gamma).

Folder:genus_1_graphs
Description:Gives stability condntions for genus 1 graphs from a cycle.

Folder: higher_genus_2_graphs
Description:Gets all stability conditions for graphs with middle edge of genus 2 for (5-7)vertices.

Folder:low_genus_2_graphs
Description:Gets all stability conditions for graphs with middle edge of genus 2 up to 4 vertices.

Folder:Top Level overlap
Description:Examples of inclusion exclusion intersection numbers of patches of sginma(\Gamma).