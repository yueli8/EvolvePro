(base) qinghuo@qinghuo-desktop:~$ conda activate evolvepro
(evolvepro) qinghuo@qinghuo-desktop:~$ python
Python 3.11.11 | packaged by conda-forge | (main, Dec  5 2024, 14:17:24) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

1. Experimental Mutation Processing
# To generate a wild-type FASTA file and create single
from evolvepro.src.process import generate_wt, generate_single_aa_mutants
generate_wt('MPSETYITKTLSLKLIPSDEEKQALENYFITFQRAVNFAIDRIVDIRSSFRYLNKNEQFPAVCDCCGKKEKIMYVNISNKTFKFKPSRNQKDRYTKDIYTIKPNAHICKTCYSGVAGNMFIRKQMYPNDKEGWKVSRSYNIKVNAPGLTGTEYAMAIRKAISILRSFEKRRRNAERRAIEYEKSKKEYLELIDDVEKGKTNKIVVLEKEGHQRVKRYKHKNWPEKWQGISLNKAKSKVKDIEKRIKKLKEWKHPTLNRPYVELHKNNVRIVGYETVELKLGNKMYTIHFASISNLRKPFRKQKKKSIEYLKHLLTLALKRNLETYPSIIKRGVNFFLQYPVRVTVKVPKLTKNFKAFGIDRGVNRLAVGCIISKDGKLTNKNIFFFHGKEAWAKENRYKKIRDRLYAMAKKLRGDKTKKIRLYHEIRKKFRHKVKYFRRNYLHNISKQIVEIAPENTPTVIVLEDLRYLRERTYRGKGRSKKAKKTNYKLNTFTYRMLIDMIKYKAEEAGVPVMIIDPRNTSRKCSKCGYVDENNRKQASFKCLKCGYSLNADLNAAVNIAKAFYECPTFRWEEKLHAYVCSEPDK', output_file='content/out/cas12f_WT.fasta')
generate_single_aa_mutants('content/out/cas12f_WT.fasta', output_file='content/out/cas12f.fasta')

# To suggest a random set of mutation to assay
from evolvepro.src.process import suggest_initial_mutants
suggest_initial_mutants('content/out/cas12f.fasta', num_mutants=12, random_seed=42)

# To generate n-mutant combinations
from evolvepro.src.process import generate_n_mutant_combinations
#not work 
#generate_n_mutant_combinations('content/out/cas12f_WT.fasta','kelsic_Round5.xlsx',3,'content/out/dataset_3rd.fasta',threshold=1)

!python evolvepro/plm/esm/extract.py esm1b_t33_650M_UR50S ~/out/cas12f.fasta ~/out/cas12f_esm1b_t33_650M_UR50S --toks_per_batch 512 --include mean --concatenate_dir ~/out

(evolvepro) jing@jing-Inspiron-3670:~/EvolvePro$ python
from evolvepro.src.evolve import evolve_experimental


protein_name = 'cas12f'
embeddings_base_path = '~/content/output'
embeddings_file_name = 'cas12f_esm1b_t33_650M_UR50S.csv'
round_base_path = '~/content/EvolvePro/colab/cas12f_rounds_data'
wt_fasta_path = '/home/qinghuo/content/output/cas12f_WT.fasta'
number_of_variants = 12
output_dir = '/home/qinghuo/content/output/'
rename_WT = False

round_name = 'Round1'
round_file_names = ['cas12f_Round1.xlsx']

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

