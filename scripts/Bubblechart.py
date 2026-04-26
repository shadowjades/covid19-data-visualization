import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('owid-covid-data.csv')

# 处理缺失值
data.fillna(0, inplace=True)

# 过滤特定日期的数据
latest_data = data[data['date'] == data['date'].max()]

# 创建气泡图
plt.figure(figsize=(12, 8))

# 气泡大小和颜色
sizes = latest_data['population'] / 1e5  # 调整大小比例
colors = np.random.rand(len(latest_data))  # 随机颜色

# 绘制气泡图
scatter = plt.scatter(latest_data['total_vaccinations_per_hundred'],
                      latest_data['gdp_per_capita'],
                      s=sizes,
                      c=colors,
                      alpha=0.5,
                      cmap='viridis')

# 添加标题和标签
plt.title('COVID-19 Vaccinations vs GDP per Capita', fontsize=18)
plt.xlabel('Total Vaccinations per 100 People', fontsize=14)
plt.ylabel('GDP per Capita', fontsize=14)

# 添加颜色条
cbar = plt.colorbar(scatter)
cbar.set_label('Random Color Scale', fontsize=14)

# 显示图表
plt.show()
