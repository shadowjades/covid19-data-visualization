# COVID-19 数据可视化分析 | COVID-19 Data Visualization

本项目基于 **Our World in Data** 提供的 COVID-19 公开数据集，使用 Python 进行数据处理，并通过 **Plotly** 创建了多个**交互式动态图表**，用于探索疫情的发展趋势、疫苗接种情况、经济指标（GDP）以及不同大洲之间的差异。

This project uses the public COVID-19 dataset from **Our World in Data**, processes the data with Python, and creates multiple **interactive dynamic charts** using **Plotly** to explore pandemic trends, vaccination progress, economic indicators (GDP), and differences across continents.

---

## ✨ 项目特点 | Features

- **动态交互**：图表支持悬停显示数据、滑动选择日期、下拉菜单切换国家/地区等交互操作。  
  **Interactive** – hover tooltips, date sliders, dropdown menus for country/region selection.

- **多维度分析**：涵盖确诊病例、新增病例、死亡人数、疫苗接种率、GDP、人口规模等指标。  
  **Multi‑dimensional** – confirmed cases, new cases, deaths, vaccination rates, GDP, population.

- **大洲颜色映射**：统一使用自定义颜色区分各大洲（亚洲-红，欧洲-蓝，非洲-黑，北美洲-青，南美洲-黄，大洋洲-绿，无洲属地区-橙）。  
  **Custom continent colours** – Asia(red), Europe(blue), Africa(black), North America(cyan), South America(yellow), Oceania(green), Others(orange).

- **时间动画**：部分图表包含时间滑块动画，可动态观察指标随时间的变化。  
  **Animated over time** – some charts include a date slider to watch indicators evolve.

---

## 📊 可视化图表列表 | Chart List

| 文件名 (Chinese) | 英文文件名 (English) | 图表类型 | 说明 |
|-----------------|---------------------|----------|------|
| `全球确诊病例数随时间的变化（折线图）.py` | `global_cases_line.py` | 折线图 | 全球总确诊病例数的时间序列趋势 |
| `全球每日新增病例数（柱状图）.py` | `daily_new_cases_dropdown.py` | 柱状图 + 下拉菜单 | 可切换不同国家/地区，查看每日新增病例 |
| `不同大洲的确诊病例数（饼状图）.py` | `cases_by_continent_pie.py` | 饼图 | 各大洲累计确诊病例占比 |
| `各大洲确诊病例数随时间的变化（面积图）.py` | `continent_cases_area.py` | 面积图 | 各大洲累计确诊病例随时间堆积变化 |
| `各大洲显示确诊病例数量（柱状图）.py` | `continent_cases_bar.py` | 柱状图 | 各大洲累计确诊病例总数对比 |
| `确诊病例数与人均GDP的关系.py` | `cases_vs_gdp_animated.py` | 气泡图 + 时间动画 | 每百万人确诊 vs 人均GDP，气泡大小代表人口 |
| `疫苗接种率与人均GDP的关系.py` | `vaccine_vs_gdp_animated.py` | 气泡图 + 时间动画 | 每百人疫苗接种量 vs 人均GDP |
| `疫苗接种数量与死亡率.py` | `vaccine_vs_deaths_animated.py` | 气泡图 + 时间动画 | 每百人疫苗接种量 vs 总死亡人数 |
| `Covid_cases_vs_GDP.py` | `covid_cases_vs_gdp.py` | 气泡图动画 | 确诊病例数 vs GDP (Plotly Express 版) |
| `Bubblechart.py` | `bubblechart_static.py` | 静态气泡图 (Matplotlib) | 最新日期的疫苗接种率 vs GDP per capita |
| `1.py` | `daily_cases_dropdown.py` | 折线图 + 下拉菜单 | 按国家切换每日新增病例折线图 |
| `3.py` | `vaccine_cases_slider.py` | 散点图 + 滑块 | 总疫苗接种量 vs 总确诊病例，按日期滑块 |
| `Data_preprocessing.py` | `data_preprocessing.py` | 预处理脚本 | 原始数据缺失值填充，生成 `filled.csv` |

> 注：部分早期脚本（如 `1.py`、`3.py`）与后期脚本功能相似，可根据需要保留或合并。  
> *Note: Some early scripts (e.g., `1.py`, `3.py`) have similar functionality to later ones; feel free to keep or merge them.*

---

## 🚀 快速开始 | Quick Start

### 1. 克隆仓库 | Clone the repository

```bash
git clone https://github.com/shadowjades/covid19-data-visualization.git
cd covid19-data-visualization
