import pandas as pd
import plotly.express as px

# 读取数据
data = pd.read_csv('owid-covid-data-filled.csv')

# 处理缺失值
data.fillna(0, inplace=True)

# 创建颜色字典，定义大洲与对应颜色
color_dict = {
    'Asia': 'red',
    'Europe': 'blue',
    'Oceania': 'green',
    'South America': 'yellow',
    'North America': 'cyan',
    'Africa': 'black',
    'Other': 'orange'  # 将所有其他的归为 'Other' 并用橙色表示
}

# 将非洲、亚洲、欧洲、大洋洲、南美洲和北美洲之外的国家归类为 'Other'
data['continent'] = data['continent'].apply(lambda x: x if x in color_dict else 'Other')

# 将 'Other' 标签改为 '无洲属地区'
data['continent'] = data['continent'].replace('Other', '无洲属地区')

# 按大洲和日期分组并计算确诊病例数总和
continent_cases = data.groupby(['date', 'continent'])['total_cases'].sum().reset_index()

# 创建面积图
fig = px.area(continent_cases, x='date', y='total_cases', color='continent',
              title='各大洲确诊病例数随时间的变化',
              labels={'date': '日期', 'total_cases': '确诊病例数', 'continent': '大洲'},
              color_discrete_map=color_dict)

# 显示图表
fig.show()
