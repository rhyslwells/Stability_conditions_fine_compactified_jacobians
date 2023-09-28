Here we outline the Notebooks referenced in the thesis:

Please note these are copies of the files, see Location for path to orginal file in order to run cells.

Name:
   1_Assignment_induced_datum:
Description:
   Gives examples and visualisation of sigma^{A_{\Gamma}}(\Gamma) as we vary A_{\Gamma} for triangle and 2-vine graphs.
Location(can be run in Notebooks):
	"\Graph\Assignment_induced_datum\Assignment_induced_datum.ipynb"
	
Name:
	2_phi_calculator.ipynb
Description:
	We implement the definition of a phi-stability condition and which allows one to generate any phi-stability condition given a graph and a non-degenerate phi.
Location:
	\Stability_Conditions\Graph\phi_investigation\phi_analysis.ipynb

   
Name:
	3_Cycles_to_stability.ipynb
Description: 
	We implement our construction from the thesis to construct a stabilitiy for any given n-cycle. 
Location(can be run in Notebooks):
	"\Graph\genus_1_graphs\Cycles_to_stability.ipynb"

Name:
	4_assignments.ipynb
Description:
	We implement the Algorithm described in section 4.3 and give an exhaustive method to obtain get all stability conditions up to translation for all graphs mentioned in the chapter: Introduction.
Location:
\Stability_Conditions\Graph\graph_stability_conditions\assignments.ipynb


Name: 
	5_assignments_11k3graphs.ipynb
Description:
	We use the genus 1 case to determine all stability conditions up to translation for \Gamma_{11k_3} for $2 \le k_3 \le 8$.
Location:
	/Stability_Conditions/Graph/graph_stability_conditions/assignments_11k3graphs.ipynb
	


Name:
	6_phi_investigation
Description:
	For each stability condition $\sigma_{\Gamma}$ given in 5_assignments.ipynb we construct $P_{ST}^{\sigma_{\Gamma}}$ and ask whether it is empty or not.
Location:
	\Stability_Conditions\Graph\phi_investigation\phi_analysis.ipynb
	
Name:
	7_strong_stability_check.ipynb
Description:
	We check that the 16 weak stability conditions that are not phi-stability conditions for the graph F:=G6M3M14 are strong stability conditions. We do this by checking that pairwise elements of $\sigma_{\Gamma}(\Gamma)$ are chip-firing independant.
Location:
    Stability_Conditions/Graph/phi_investigation/examples/FV_G6M3M14/strong_stability_check.ipynb

Name:
	8_MSA.ipynb
Description:
	We implement the Algorithm state in section 5.1 of the thesis. We then calculate $\tilde{P}_n$ up to $1 \le n\le 6$ and give a decomposition of $|\tilde{P}_n|$ in terms of $|\tilde{P}_{n-1}|$.
Location:
	\Stability_Conditions\MSA\Pn.ipynb


