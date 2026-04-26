import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

# 读取预处理后的数据
data = pd.read_csv('owid-covid-data-filled.csv')

# 过滤无效数据
data = data.dropna(subset=['total_vaccinations', 'total_cases', 'population'])

# 获取所有的日期
dates = sorted(data['date'].unique())
countries = data['location'].unique()

# 创建一个颜色字典，为每个国家分配不同的颜色
colors = px.colors.qualitative.T10  # 使用 Plotly 提供的颜色方案
color_dict = {country: colors[i % len(colors)] for i, country in enumerate(countries)}

# 创建一个空的 Figure
fig = make_subplots(rows=1, cols=1)

# 添加滑块每一步的数据
for date in dates:
    # 获取该日期的数据
    day_data = data[data['date'] == date]

    # 提取所需数据
    x = day_data['total_vaccinations']
    y = day_data['total_cases']
    size = day_data['population'] / 100000  # 假设人口数据用于表示气泡大小
    countries = day_data['location']  # 国家名称

    # 添加该日期的散点图
    fig.add_trace(go.Scatter(
        x=x, y=y, mode='markers',
        marker=dict(size=size, sizemode='area', sizeref=2. * max(size) / (40. ** 2), opacity=0.5),
        text=countries,  # 设置气泡上显示的文本信息
        hoverinfo='text+x+y',
        name=date,  # 设置名称为日期
        visible=False
    ))

# 设置第一个数据集可见
fig.data[0].visible = True

# 创建滑块
steps = []
for i, date in enumerate(dates):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": f"疫苗接种与确诊病例的关系（{date}数据）"}],  # 更新标题
    )
    step["args"][0]["visible"][i] = True  # 让当前步骤的图形可见
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "日期: "},
    pad={"t": 50},
    steps=steps
)]

# 创建一个下拉框，用于选择颜色
updatemenu = [
    dict(
        buttons=[
                    dict(
                        args=[{"marker.color": list(color_dict.values())}],
                        label="默认颜色",
                        method="restyle"
                    )
                ] + [
                    dict(
                        args=[{"marker.color": [color_dict[country] if country in color_dict else 'grey' for country in
                                                countries]}],
                        label=country,
                        method="restyle"
                    ) for country in countries
                ],
        direction="down",
        showactive=True,
    )
]

fig.update_layout(
    sliders=sliders,
    updatemenus=updatemenu,
    title='疫苗接种与确诊病例的关系（滑动选择日期）',
    xaxis_title='总疫苗接种数量',
    yaxis_title='总确诊病例数量',
    hoverlabel=dict(bgcolor="white", font_size=12, font_family="Rockwell"),
    showlegend=False
)

# 显示图表
fig.show()
