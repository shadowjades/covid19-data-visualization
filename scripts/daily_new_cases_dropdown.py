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

# 创建一个交互菜单项
buttons = []
for country in data['location'].unique():
    country_data = data[data['location'] == country]
    buttons.append(
        dict(
            args=[{"y": [country_data['new_cases'].tolist()],
                   "x": [country_data['date'].tolist()],
                   "title": f'{country}每日新增确诊病例数'}],
            label=country,
            method="update"
        )
    )

# 创建初始图表
initial_country = data['location'].unique()[0]
initial_data = data[data['location'] == initial_country]
fig = px.line(initial_data, x='date', y='new_cases', color='location', title=f'{initial_country}每日新增确诊病例数')

# 添加按钮菜单
fig.update_layout(
    updatemenus=[dict(
            buttons=buttons,
            direction="down",
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),]  # 删除选择框
)

# 添加颜色标识栏
fig.for_each_trace(lambda trace: trace.update(name=trace.name.split('=')[-1]))

fig.show()
