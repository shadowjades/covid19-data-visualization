import pandas as pd
import plotly.express as px

# 读取数据
data = pd.read_csv('owid-covid-data-filled.csv')

# 处理缺失值
data.fillna(0, inplace=True)

# 转换日期列为datetime类型
data['date'] = pd.to_datetime(data['date'])

# 聚合全球确诊病例数
global_data = data.groupby('date').sum().reset_index()

# 创建折线图
fig = px.line(global_data, x='date', y='total_cases', title='全球确诊病例数随时间的变化')

# 调整图表布局
fig.update_layout(
    xaxis_title='日期',
    yaxis_title='确诊病例数',
    hovermode='x unified'
)

# 显示图表
fig.show()
