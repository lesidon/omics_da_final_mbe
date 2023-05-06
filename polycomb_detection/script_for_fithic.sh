#!/bin/bash

# this command converts the .hic into .mcool 
hic2cool convert /gss/home/l.sidorov/omics_final_project/data/GSE168524_neurons_fem_wt_allValidPairs.hic \
/gss/home/l.sidorov/omics_final_project/GSE168524_neurons_fem_wt_allValidPairs.mcool -p 1

# this python script creates input files for Fit-Hi-C
python3 interactions_and_fragments_file.py

# this command generated the bias file
python3 ../../fithic/fithic/utils/HiCKRy.py -i ./fithic_inputs/interactions.txt.gzip -f ./fithic_inputs/fragments.gzip -o ./fithic_inputs -x 0.05

# this command creates a file with contact enrichment
fithic -i ./fithic_inputs/interactions.txt.gzip -f ./fithic_inputs/fragments2.gzip -o ../output_fithic/ -r 100000 -t ./fithic_inputs/bias_file
