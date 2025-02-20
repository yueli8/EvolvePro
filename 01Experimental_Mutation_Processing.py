#Process This directory contains scripts to prepare files for use in EvolvePro. There are two main scripts for processing mutation data: one for experimental data and another for deep mutational scanning (DMS) data. The source functions used here are in evolvepro/src/process.py.
#For process, use the evolvepro environment:
conda activate evolvepro

#This script shows examples of how to generate single amino acid mutants and n-mutant variants for proteins to improve. The output target is a FASTA file of all single AA substitutions relative to the WT sequence.
#How to Run: To generate a wild-type FASTA file and create single amino acid mutants:
from evolvepro.src.process import generate_wt, generate_single_aa_mutants
generate_wt('MNTINIAKNDFS', 'output_path/dataset_WT.fasta')
generate_single_aa_mutants('output_path/dataset_WT.fasta', 'output_path/dataset.fasta')

#To suggest a random set of mutants to assay:
from evolvepro.src.process import suggest_initial_mutants
suggest_initial_mutants('output_path/dataset.fasta', 10)

#To generate n-mutant combinations:生成包含3个突变的组合序列，并保存到dataset_3rd.fasta文件中
from evolvepro.src.process import generate_n_mutant_combinations
generate_n_mutant_combinations('output_path/dataset_WT.fasta', 'beneficial_mutations.xlsx', 3, 'output_path/dataset_3rd.fasta', threshold=1)

#To generate n-mutant combinations:生成包含4个突变的组合序列，并保存到dataset_4rd.fasta文件中
#generate_n_mutant_combinations('output_path/dataset_WT.fasta', 'beneficial_mutations.xlsx', 4, 'output_path/dataset_4rd.fasta', threshold=1)

