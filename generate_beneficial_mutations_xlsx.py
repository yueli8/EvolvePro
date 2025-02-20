import pandas as pd

# 原始 Variant 和 DMS 活性值
data = {
    "Variant": ["E4M", "V31C", "T12H"],
    "activity": [1, 1.02, 0.97]  # 真实的 DMS 活性值
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 去掉 Variant 的第一个字母
#df["Variant"] = df["Variant"].str[1:]

# 保存到 Excel 文件
df.to_excel("beneficial_mutations.xlsx", index=False)

print("✅ beneficial_mutations.xlsx 文件已创建！")
