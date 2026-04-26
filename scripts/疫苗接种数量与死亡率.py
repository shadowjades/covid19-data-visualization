import pandas as pd
import plotly.express as px

# 读取数据
data = pd.read_csv('owid-covid-data-filled.csv')

# 处理缺失值（填充为0）
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

# 设置颜色
data['color'] = data['continent'].apply(lambda x: color_dict[x])

# 调整气泡大小比例
data['population_size'] = data['population'] / 1  # 将人口数量调整到合适的大小比例

# 创建气泡图动画
fig = px.scatter(
    data,
    x='total_vaccinations_per_hundred',
    y='total_deaths',
    size='population_size',
    color='continent',
    hover_name='location',
    animation_frame='date',
    size_max=150,  # 设置最大气泡大小
    title='疫苗接种率与死亡数量的关系（随时间变化）',
    labels={
        'total_vaccinations_per_hundred': '每百人接种疫苗总数',
        'total_deaths': '死亡总数',
        'continent': '大洲',
        'location': '国家',
        'date': '日期'
    },
    color_discrete_map=color_dict  # 使用颜色字典
)

# 调整动画速度
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 50  # 将每帧的持续时间设置为50ms
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 10  # 将过渡持续时间设置为10ms

# 显示图表
fig.show()
