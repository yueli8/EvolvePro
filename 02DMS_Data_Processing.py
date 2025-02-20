#代码调用evolvepro库中的process_data函数，主要目的是处理DMS（Deep Mutational Scanning）活性数据，并进行筛选和转换。
from evolvepro.src.process import process_dataset
process_df=process_dataset(
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

#输出结果在'output/dms'
#To create visualization plots:
from evolvepro.src.process import plot_mutations_per_position
import pandas as pd
processed_df=pd.read_csv("output/dms/brenan_labels.csv")
print(processed_df.head())

from evolvepro.src.process import plot_histogram_of_readout
plot_mutations_per_position(processed_df)
plot_histogram_of_readout(processed_df, 'DMS_SCH', 2.5)
