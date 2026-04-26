import pandas as pd

# 读取数据
data = pd.read_csv('owid-covid-data.csv')

# 查看缺失值情况
print(data.isnull().sum())

# 填充缺失值为0
data_filled = data.fillna(0)

# 标记存在缺失值的列
missing_columns = data.columns[data.isnull().any()].tolist()
print(f"存在缺失值的列: {missing_columns}")

# 保存处理后的数据到新文件
data_filled.to_csv('owid-covid-data-filled.csv', index=False)
