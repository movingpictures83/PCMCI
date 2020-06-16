# PCMCI
# Language: Python
# Input: TSV
# Output: none (screen only)
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to run PCMCI (Runge et al, 2019), performing 
causal analysis on time-series data.

PCMCI takes as input a TSV file of edges (one line per edge).
Each line has the format:

variable	driver	lag	coeff

Where driver is the source, the variable is the destination,
the lag is in units of time, and the coefficient is the edge weight.

Important causal edges are then printed to the screen.
