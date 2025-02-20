#install gcc
qinghuo@qinghuo-desktop:~$ sudo apt update
qinghuo@qinghuo-desktop:~$ sudo apt install build-essential

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
https://github.com/mat10d/EvolvePro
sudo apt install git

#install conda 
qinghuo@qinghuo-desktop:~$ chmod +x Miniconda3-latest-Linux-x86_64.sh 
qinghuo@qinghuo-desktop:~$ bash Miniconda3-latest-Linux-x86_64.sh 
bash Miniconda3-latest-Linux-x86_64.sh
qinghuo@qinghuo-desktop:~$ ~/miniconda3/bin/conda init
#For changes to take effect, close and re-open your current shell.   重新开一个新的终端
qinghuo@qinghuo-desktop:~$ source ~/.bashrc
qinghuo@qinghuo-desktop: conda --version

(base) qinghuo@qinghuo-desktop:~$ pip install pandas numpy scikit-learn scikit-learn-extra xgboost matplotlib seaborn biopython scipy torch fair-esm

git clone https://github.com/mat10d/EvolvePro.git
cd EvolvePro

qinghuo@qinghuo-desktop:~/EvolvePro$ conda env create -f environment.yml
qinghuo@qinghuo-desktop:~/EvolvePro$ conda activate evolvepro

#qinghuo@qinghuo-desktop:~/EvolvePro$ sh setup_plm.sh
qinghuo@qinghuo-desktop:~/EvolvePro$ conda activate plm
qinghuo@qinghuo-desktop:~$mkdir content/output
(base) qinghuo@qinghuo-desktop:~$ conda activate evolvepro
(evolvepro) qinghuo@qinghuo-desktop:~$ python
Python 3.11.11 | packaged by conda-forge | (main, Dec  5 2024, 14:17:24) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

#1. Experimental Mutation Processing,be sure in evolvepro, 
#To generate a wild-type FASTA file and create single amino acid mutants:

from evolvepro.src.process import generate_wt, generate_single_aa_mutants
generate_wt('MSIQHFRVALIPFFAAFCLPVFAHPETLVKVKDAEDQLGARVGYIELDLNSGKILESFRPEERFPMMSTFKVLLCGAVLSRVDAGQEQLGRRIHYSQNDLVEYSPVTEKHLTDGMTVRELCSAAITMSDNTAANLLLTTIGGPKELTAFLHNMGDHVTRLDRWEPELNEAIPNDERDTTMPAAMATTLRKLLTGELLTLASRQQLIDWMEADKVAGPLLRSALPAGWFIADKSGAGERGSRGIIAALGPDGKPSRIVVIYTTGSQATMDERNRQIAEIGASLIKHW', output_file='content/output/bla_WT.fasta')
generate_single_aa_mutants('content/output/bla_WT.fasta', output_file='content/output/bla.fasta')

# To suggest a random set of mutation to assay
from evolvepro.src.process import suggest_initial_mutants
suggest_initial_mutants('content/output/infA.fasta', num_mutants=200, random_seed=101)#第二次产生不同突变，改变random_seed的参数

# To generate n-mutant combinations
#not work # cannot find 'beneficial_mutations.xlsx'
#from evolvepro.src.process import generate_n_mutant_combinations
#generate_n_mutant_combinations('content/output/infA_WT.fasta','beneficial_mutations.xlsx',3,'content/output/dataset_3rd.fasta',threshold=1)

(base) qinghuo@qinghuo-desktop:~/.cache/torch/hub/checkpoints$ cp esm1b_t33_650M_UR50S.pt ~/EvolvePro/
(base) qinghuo@qinghuo-desktop:~/.cache/torch/hub/checkpoints$ cp esm1b_t33_650M_UR50S-contact-regression.pt ~/EvolvePro/

#PLM(protein language model)
(base) qinghuo@qinghuo-desktop:~/EvolvePro$ python evolvepro/plm/esm/extract.py esm2_t36_3B_UR50D.pt ~/content/output/bla.fasta ~/content/output/bla_esm2_t36_3B_UR50D --toks_per_batch 512 --include mean --concatenate_dir ~/content/output

#wget https://dl.fbaipublicfiles.com/fair-esm/models/esm2_t36_3B_UR50D.pt
#wget https://dl.fbaipublicfiles.com/fair-esm/regression/esm2_t36_3B_UR50D-contact-regression.pt

#Saved concatenated representations to /home/qinghuo/content/output/infA_esm1b_t33_650M_UR50S.pt.csv

(base) qinghuo@qinghuo-desktop:~$ conda activate evolvepro
#Run EVOLVEpro
(evolvepro) jing@jing-Inspiron-3670:~/EvolvePro$ python
from evolvepro.src.evolve import evolve_experimental

protein_name = 'infa'
embeddings_base_path = '~/content/output'
embeddings_file_name = 'infA_esm2_t36_3B_UR50D.pt.csv'
round_base_path = '~/EvolvePro/colab/rounds_data'
wt_fasta_path = '/home/qinghuo/content/output/infA_WT.fasta'
number_of_variants = 16
output_dir = '/home/qinghuo/content/output/'
rename_WT = False

#Round 1
round_name = 'Round1'
round_file_names = ['infa_Round1.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

#/home/qinghuo/content/output/infA/Round1/df_test.csv,variant perl match.pl, perl delete_each每一行第一个字母.pl 
#/home/qinghuo/content/EvolvePro/colab/rounds_data infA_Round1.xlsx


#Round 2
round_name = 'Round2'
round_file_names = ['bla_Round1.xlsx', 'bla_Round2.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

#Round 3
round_name = 'Round3'
round_file_names = ['bla_Round1.xlsx', 'bla_Round2.xlsx','bla_Round3.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

#Round 4
round_name = 'Round4'
round_file_names = ['bla_Round1.xlsx', 'bla_Round2.xlsx','bla_Round3.xlsx','bla_Round4.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

#Round 5
round_name = 'Round5'
round_file_names = ['bla_Round1.xlsx', 'bla_Round2.xlsx','bla_Round3.xlsx','bla_Round4.xlsx','bla_Round5.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

#Round 6
round_name = 'Round6'
round_file_names = ['bla_Round1.xlsx', 'bla_Round2.xlsx','bla_Round3.xlsx','bla_Round4.xlsx','bla_Round5.xlsx','bla_Round6.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

#Round 7
round_name = 'Round7'
round_file_names = ['bla_Round1.xlsx', 'bla_Round2.xlsx','bla_Round3.xlsx','bla_Round4.xlsx','bla_Round5.xlsx','bla_Round6.xlsx','bla_Round7.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

#Round 8
round_name = 'Round8'
round_file_names = ['bla_Round1.xlsx', 'bla_Round2.xlsx','bla_Round3.xlsx','bla_Round4.xlsx','bla_Round5.xlsx','bla_Round6.xlsx','bla_Round7.xlsx','bla_Round8.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

#Round 9
round_name = 'Round9'
round_file_names = ['bla_Round1.xlsx', 'bla_Round2.xlsx','bla_Round3.xlsx','bla_Round4.xlsx','bla_Round5.xlsx','bla_Round6.xlsx','bla_Round7.xlsx','bla_Round8.xlsx','bla_Round9.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

#Round 10
round_name = 'Round10'
round_file_names = ['bla_Round1.xlsx', 'bla_Round2.xlsx','bla_Round3.xlsx','bla_Round4.xlsx','bla_Round5.xlsx','bla_Round6.xlsx','bla_Round7.xlsx','bla_Round8.xlsx','bla_Round9.xlsx','bla_Round10.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

#Round 11
round_name = 'Round11'
round_file_names = ['bla_Round1.xlsx', 'bla_Round2.xlsx','bla_Round3.xlsx','bla_Round4.xlsx','bla_Round5.xlsx','bla_Round6.xlsx','bla_Round7.xlsx','bla_Round8.xlsx','bla_Round9.xlsx','bla_Round10.xlsx','bla_Round11.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)


#high activity candidates df_sorted_all.csv  y_actual_binary=1

#Plot
from evolvepro.src.plot import read_exp_data, plot_variants_by_iteration

round_base_path = '~/EvolvePro/colab/rounds_data'
round_file_names = ['infA_Round1.xlsx', 'infA_Round2.xlsx','infA_Round3.xlsx','infA_Round4.xlsx',
'infA_Round5.xlsx','infA_Round6.xlsx','infA_Round7.xlsx','infA_Round8.xlsx','infA_Round9.xlsx','infA_Round10.xlsx']
wt_fasta_path = '/home/qinghuo/content/output/infA_WT.fasta'

df = read_exp_data(round_base_path, round_file_names, wt_fasta_path)
plot_variants_by_iteration(df, activity_column='activity', output_dir=output_dir, output_file="infA") 







































from evolvepro.src.process import process_dataset
process_dataset(
    file_path='data/dms/activity/Source.xlsx',
    dataset_name='brenan',
    wt_fasta_path='data/dms/wt_fasta/brenan_WT.fasta',
    activity_column='DMS_SCH',
    cutoff_value=2.5,
    output_dir='output/dms',
    sheet_name='MAPK1',
    cutoff_rule='greater_than',
    cutoff_percentiles=[90, 95]
)

plot_mutations_per_position(processed_df)
plot_histogram_of_readout(processed_df, 'DMS_SCH', 2.5)


%%capture

!pip install pandas numpy scikit-learn scikit-learn-extra xgboost matplotlib seaborn biopython scipy torch fair-esm
!mkdir /content/output

jing@jing-Inspiron-3670:~$ cd EvolvePro/
jing@jing-Inspiron-3670:~/EvolvePro$ conda activate evolvepro
(evolvepro) jing@jing-Inspiron-3670:~/EvolvePro$ 

(evolvepro) jing@jing-Inspiron-3670:~/EvolvePro$ python


from evolvepro.src.process import generate_wt, generate_single_aa_mutants
generate_wt('MAKEDNIEMQGTVLETLPNTMFRVELENGHVVTAHISGKMRKNYIRILTGDKVTVELTPYDLSKGRIVFRSR', output_file='out/kelsic_WT.fasta')
generate_single_aa_mutants('out/kelsic_WT.fasta', output_file='out/kelsic.fasta')

from evolvepro.src.process import suggest_initial_mutants
suggest_initial_mutants('out/kelsic.fasta', num_mutants=12, random_seed=42)

!python evolvepro/plm/esm/extract.py esm1b_t33_650M_UR50S out/kelsic.fasta out/kelsic_esm1b_t33_650M_UR50S --toks_per_batch 512 --include mean --concatenate_dir out

(evolvepro) jing@jing-Inspiron-3670:~/EvolvePro$ python
from evolvepro.src.evolve import evolve_experimental

protein_name = 'kelsic'
embeddings_base_path = '~/content/output'
embeddings_file_name = 'kelsic_esm1b_t33_650M_UR50S.csv'
round_base_path = '~/content/EvolvePro/colab/rounds_data'
wt_fasta_path = '/home/qinghuo/content/output/kelsic_WT.fasta'
number_of_variants = 12
output_dir = '/home/qinghuo/content/output/'
rename_WT = False

round_name = 'Round1'
round_file_names = ['kelsic_Round1.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

round_name = 'Round2'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

round_name = 'Round3'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx', 'kelsic_Round3.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)


round_name = 'Round4'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx', 'kelsic_Round3.xlsx', 'kelsic_Round4.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

round_name = 'Round5'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx', 'kelsic_Round3.xlsx', 'kelsic_Round4.xlsx', 'kelsic_Round5.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)


