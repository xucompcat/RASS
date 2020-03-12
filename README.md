# RASS
---

## Description
RASS (Random Assembly Stocastic Search) is a Python program for facilitating a stochastic search for any type of molecular structure. 
This approach refines Saunders' seminal <a href='http://onlinelibrary.wiley.com/doi/10.1002/jcc.10407/abstract'>"Kick"</a> procedure, but adds restrictions on 
what constitutes an acceptable candidate structure.  These restrictions are that no pair of atoms in a 
candidate structure can exhibit distances less than the sum of their combined covalent radii, and that
each atom in a candidate structure must be connected to every other atom by a network of bonds (where
bonds are defined based on atomic covalent radii).  These restrictions are enforced during RASS's unique candidate structure assembly process.  
<br>
Compared to Saunders' original Kick method, RASS delivers substantial improvements
in search efficiency due to its truncation of the molecular configuration space searched to
regions on the potential energy surface which are chemically relevant.  In the present implementation, RASS is designed to interface
with the Gaussian09 package for performing ab initio quantum chemistry optimizations.  However, if use
of another optimization package is desired, this code can be used simply
for candidate structure geometry initialization.
<br>
<br>




## Author: W. C. McKee on Behalf of the Xu Group at LSU
* <a href="https://github.com/chadm9">W. C. McKee's GitHub</a>
* <a href="https://www.linkedin.com/in/w-chad-mckee-88939163/">W. C. McKee's LinkedIn</a>
* <a href="https://compucat.lsu.edu/">Xu Group Website (Computational Catalysis and Surface Reactions)</a>


## Languages and Technologies used
* Python 2.7


## Dependencies and Plugins
None, but note that the present implementation of RASS is designed to 
interface with the Gaussian09 software suite for performing ab initio quantum
mechanical optimizations.

## Usage Example

The following assumes that RASS.py, RASS.in, and G09OutputSummarizer.py
are in your current working directory.
<br>
<br>
An example input file (RASS.in) is provided below:

```
atoms: B C O N S
atom_numbers: 1 1 1 1 1
structures: 10
```
This input will produce 10 Gaussian09 input files whose starting geometries consist of randomly generated coordinates. Each candidate structures will be comprised of one B, one C,
one O, one N, and one S atom.  A RASS.in file for generating 250 candidate structures for an Si8 cluster would be comprised of the following:
```
atoms: Si
atom_numbers: 8
structures: 250
```
As a final example, generating 100 candidate structures for H2O would be achieved via the follwoing RASS.in file:
```
atoms: H O
atom_numbers: 1 2
structures: 100
```
Input files are generated from RASS.in by running RASS.py from the command line:

```
python RASS.py
```
An example Gaussian09 input file (which should subsequently be submitted for 
optimization) produced by running RASS.py with the BCONS RASS.in file above is:

```
%mem=4gb
# RB3LYP/LANL2DZ Opt=maxcycles=50

Title

0 1
O 0.0 0.0 0.0
C 0.76746085476 0.0862670139946 0.947666305521
S -0.170266608427 -0.994575095863 -1.21403939857
N 0.418233917681 -0.912032132389 0.557059637416
B -1.73448731037 -1.37056791641 -1.18542732833

END
```
Assuming Gaussian09 is used to optimize the candidate structures,
the script 'G09OutputSummarizer.py' can then be executed to collect all the structures located
and order them according to their energy.  A usage example is:
```
python G09OutputSummarizer.py 10 > RASS.results
```
where 10 is the number of candidate structures designated in the RASS.in file.  Executing the above command writes the optimization
results to a file called 'RASS.results'.  An example of RASS.results based on Gaussian09 optimization of 250 candidate structures
of Si8 species is provided in this repository.


## Using RASS Without Gaussian09

### Modifying the Source Code to Print Only Candidate Structure Atomic Coordinates
If usage of a candidate structure optimization package other than Gaussian09 is desired,
then removing the following code (lines 227-230) from RASS.py will alter the program to 
only write the atomic coordinates of generated candidate structures.  The lines which should be removed 
are shown below:
<br>
```Python
        output.write("%mem=4gb\n")
        output.write("# RB3LYP/LANL2DZ Opt=maxcycles=50\n")
        output.write("\nTitle\n\n")
        output.write("0 1\n")
```
Similarly, the Gaussian09 input options can easily be altered by changing the desired text on these lines.
