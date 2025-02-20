https://github.com/mat10d/EvolvePro

git clone https://github.com/mat10d/EvolvePro.git
cd EvolvePro

qinghuo@qinghuo-desktop:~/EvolvePro$ conda env create -f environment.yml
qinghuo@qinghuo-desktop:~/EvolvePro$ conda activate evolvepro

qinghuo@qinghuo-desktop:~/EvolvePro$ sh setup_plm.sh
qinghuo@qinghuo-desktop:~/EvolvePro$ conda activate plm

(evolvepro) jing@jing-Inspiron-3670:~/EvolvePro$ python

#be sure in evolvepro
from evolvepro.src.process import generate_wt, generate_single_aa_mutants
generate_wt('MAKEDNIEMQGTVLETLPNTMFRVELENGHVVTAHISGKMRKNYIRILTGDKVTVELTPYDLSKGRIVFRSR', output_file='out/kelsic_WT.fasta')
generate_single_aa_mutants('out/kelsic_WT.fasta', output_file='out/kelsic.fasta')

from evolvepro.src.process import suggest_initial_mutants
suggest_initial_mutants('out/kelsic.fasta', num_mutants=12, random_seed=42)

(base) qinghuo@qinghuo-desktop:~/.cache/torch/hub/checkpoints$ cp esm1b_t33_650M_UR50S.pt ~/EvolvePro/out/
(base) qinghuo@qinghuo-desktop:~/.cache/torch/hub/checkpoints$ cp esm1b_t33_650M_UR50S-contact-regression.pt ~/EvolvePro/out/

!python evolvepro/plm/esm/extract.py esm1b_t33_650M_UR50S out/kelsic.fasta out/kelsic_esm1b_t33_650M_UR50S --toks_per_batch 512 --include mean --concatenate_dir out







from evolvepro.src.process import generate_wt, generate_single_aa_mutants
generate_wt('MNTINIAKNDFS', 'out/dataset_WT.fasta')
generate_single_aa_mutants('out/dataset_WT.fasta', 'out/dataset.fasta')

from evolvepro.src.process import suggest_initial_mutants
suggest_initial_mutants('out/dataset.fasta', 10)

from evolvepro.src.process import generate_n_mutant_combinations
generate_n_mutant_combinations('out/dataset_WT.fasta', 'beneficial_mutations.xlsx', 3, 'out/dataset_3rd.fasta', threshold=1)

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


from evolvepro.src.plot import read_exp_data, plot_variants_by_iteration

round_base_path = '~/content/EvolvePro/colab/rounds_data'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx', 'kelsic_Round3.xlsx', 'kelsic_Round4.xlsx', 'kelsic_Round5.xlsx']
wt_fasta_path = '/home/qinghuo/content/output/kelsic_WT.fasta'

df = read_exp_data(round_base_path, round_file_names, wt_fasta_path)
plot_variants_by_iteration(df, activity_column='activity', output_dir=output_dir, output_file="kelsic")
