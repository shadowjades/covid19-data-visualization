import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

# 将 'Other' 标签改为 '无洲属地区'
data['continent'] = data['continent'].replace('Other', '无洲属地区')

# 添加一个'location_or_continent'列，用于交互选择
data['location_or_continent'] = data.apply(
    lambda row: row['location'] if row['continent'] == 'Other' else row['continent'], axis=1)

# 创建一个交互菜单项
buttons = []
for loc_or_cont in data['location_or_continent'].unique():
    loc_or_cont_data = data[data['location_or_continent'] == loc_or_cont]
    fig = px.line(loc_or_cont_data, x='date', y='new_cases', color='location', title=f'{loc_or_cont}每日新增确诊病例数')

    buttons.append(
        dict(
            args=[{"y": [loc_or_cont_data['new_cases'].tolist()]}],
            label=loc_or_cont,
            method="update"
        )
    )

# 创建初始图表
fig = px.line(data, x='date', y='new_cases', color='location', title='全球每日新增确诊病例数')

# 添加按钮菜单
fig.update_layout(
    updatemenus=[
        dict(
            buttons=buttons,
            direction="down",
            showactive=False,
            x=1.1,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

fig.show()
