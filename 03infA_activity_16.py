import random
import pandas as pd
from Bio import SeqIO

# 读取 Excel 数据文件
file_path = "source_infA.xls"  # 请确保文件路径正确
data = pd.read_excel(file_path)

# 设置筛选标准
threshold_dms_min = 0.08
threshold_dms_rich = 0.08

# 筛选符合条件的变体
filtered_variants = data[
    (data["DMS_min"] >= threshold_dms_min) & (data["DMS_rich"] >= threshold_dms_rich)
]

# 如果可选变体少于 16 个，选择全部；否则随机选 16 个
num_variants_to_select = min(16, len(filtered_variants))
selected_variants = filtered_variants.sample(n=num_variants_to_select, random_state=42)

# 读取 fasta 文件中的序列
input_fasta = "infA_candidates.fasta"  # 确保文件存在
sequences = list(SeqIO.parse(input_fasta, "fasta"))

# 选择 16 条序列并匹配变体
output_file = "round2_candidates.txt"
with open(output_file, "w") as file:
    file.write("ID\tVariant\tModified_Variant\tActivity\tDMS_rich\n")  # 添加表头

    for idx, row in selected_variants.iterrows():
        seq = random.choice(sequences)  # 随机选一个序列
        activity = round(random.uniform(0.0, 1.0), 3)  # 生成随机 activity
        variant = row["variant"]  # 选取变体名称
        modified_variant = variant[1:]  # 去掉变体的第一个字母
        dms_rich = row["DMS_rich"]  # 选取对应的 DMS_rich 值

        # 保存到文件
        file.write(f"{seq.id}\t{variant}\t{modified_variant}\t{activity}\t{dms_rich}\n")

print(f"已选出 {num_variants_to_select} 个 Round 2 的候选变体，并保存至 {output_file}！")
