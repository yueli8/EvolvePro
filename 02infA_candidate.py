from Bio import Entrez, SeqIO

# 配置 NCBI Entrez 参数
Entrez.email = "yueli118@126.com"
search_term = "infA"  # 搜索关键词

# 在 NCBI Protein 数据库中搜索关键词
handle = Entrez.esearch(db="protein", term=search_term, retmax=50)
record = Entrez.read(handle)
handle.close()

# 提取匹配序列的 ID
protein_ids = record["IdList"]

# 如果没有找到候选序列
if not protein_ids:
    print("没有找到 AsCas12f 候选序列，请检查搜索关键词或数据来源。")
else:
    # 下载候选序列
    sequences = []
    for protein_id in protein_ids:
        handle = Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text")
        seq_record = SeqIO.read(handle, "fasta")
        sequences.append(seq_record)
        handle.close()

    # 保存序列到文件
with open("infA_candidates.fasta", "w") as output_file:
    SeqIO.write(sequences, output_file,"fasta")
        

    # 输出结果
print(f"共找到 {len(sequences)} 个infA候选序列，已保存为 'infA_candidates.fasta' 文件。")

