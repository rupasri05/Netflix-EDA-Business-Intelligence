# 📊 Netflix Global Content Insights — EDA & Business Intelligence

> **Internship Assignment | Task 2 — Exploratory Data Analysis & Business Intelligence**
> Uncovering patterns, trends, and actionable insights from Netflix content data (2016–2025) using Python and SQL.

---

## 📁 Repository Structure

```
netflix-eda/
│
├── data/
│   └── netflix_cleaned.csv           # Cleaned dataset (output from Task 1)
│
├── visuals/
│   ├── eda_fig1_univariate.png       # Descriptive analysis charts (auto-generated)
│   └── eda_fig2_multivariate.png     # Correlation & multivariate charts (auto-generated)
│
├── eda_analysis.py                   # ⭐ Main Python EDA script (run this)
├── sql_queries.sql                   # 7 business SQL queries with results
├── eda_report.md                     # Full written EDA report with insights
├── Netflix_Dashboard.pptx            # Static dashboard mock-up (PowerPoint)
└── README.md                         # You are here
```

---

## 🎯 Objective

Perform a full Exploratory Data Analysis on the cleaned Netflix dataset to:
- Compute descriptive statistics across all numerical and categorical fields
- Answer 7 real business questions using SQL
- Discover relationships between variables through multivariate analysis
- Present key findings in a static PowerPoint dashboard mock-up

---

## 📊 Dataset Overview

| Property | Value |
|---|---|
| File | `netflix_cleaned.csv` |
| Source | Task 1 — Data Cleaning output |
| Rows | 200 |
| Columns | 16 |
| Period Covered | 2016 – 2025 |
| Key Fields | `IMDb`, `Viewership_M`, `Genre`, `Primary_Country`, `Duration_Min`, `Release_Month` |

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install pandas matplotlib seaborn
```

### 2. Place the cleaned dataset in the same folder
```
netflix_cleaned.csv   ← from Task 1
eda_analysis.py
```

### 3. Run the EDA script
```bash
python3 eda_analysis.py
```

### What happens when you run it:
- All 11 analysis sections print to the console
- Two chart files are saved automatically:
  - `eda_fig1_univariate.png`
  - `eda_fig2_multivariate.png`

---

## 🔍 What `eda_analysis.py` Covers

The script is divided into 12 clearly labelled sections:

| Section | What It Does |
|---|---|
| 1 | Load dataset — shows shape, column names, data types |
| 2 | Descriptive statistics — mean, median, std, min, max for numerical columns |
| 3 | Categorical summaries — IMDb band counts, top genres, content by country |
| 4 | Univariate analysis — IMDb distribution, release month counts, yearly content volume |
| 5 | Correlation matrix — relationships between IMDb, Viewership, Duration, Year |
| 6 | IMDb Band vs Avg Viewership — does quality drive views? |
| 7 | Genre vs Avg Viewership — which genres attract the most viewers? |
| 8 | Country vs Viewership & IMDb — which country performs best? |
| 9 | Yearly avg IMDb trend — has Netflix quality improved over time? |
| 10 | Release month vs Viewership — best time to release a title |
| 11 | Duration vs Viewership — do longer series get more views? |
| 12 | Chart generation — saves both PNG visualization files |

---

## 🗄️ SQL Business Questions

All 7 queries are in `sql_queries.sql`. Run them using Python + SQLite (no extra setup needed):

```python
import pandas as pd, sqlite3

df   = pd.read_csv("netflix_cleaned.csv")
conn = sqlite3.connect("netflix.db")
df.to_sql("netflix", conn, if_exists="replace", index=False)

result = pd.read_sql("SELECT * FROM netflix LIMIT 5", conn)
print(result)
```

| # | Business Question | Key Finding |
|---|---|---|
| Q1 | #1 most-watched title each year | Crime/Thriller dominates every year since 2017 |
| Q2 | Which country produces the highest-rated content? | Canada (8.47) and UK (8.12) lead on IMDb |
| Q3 | Which genres drive the most engagement? | Heist/Crime averages 388M views — nearly double 3rd place |
| Q4 | How has viewership trended year by year? | 2022 was peak year with 3,985M total views |
| Q5 | Which release month generates the most views? | June (115.8M) beats October (34.2M) by 3.4× |
| Q6 | Top critically acclaimed + popular titles? | Stranger Things 3 leads (582M views, IMDb 8.7) |
| Q7 | Does longer content get more views? | Long content (500+ min) gets 3.6× more views than short |

---

## 💡 Top 6 Business Insights

| # | Insight | Data Evidence |
|---|---|---|
| 1 | 🇰🇷 **Korean content ROI is exceptional** | 20 titles, avg 143.9M views — nearly 2× the USA average of 76M |
| 2 | ☀️ **Summer releases outperform all other months** | June–July avg 113M vs October 34.2M — 3.3× difference |
| 3 | 📺 **Longer series dramatically outperform short content** | 500+ min content averages 122M views vs 33.6M for short |
| 4 | 🎭 **Heist/Crime genre is severely underproduced** | Only 5 titles but highest avg viewership at 388M per title |
| 5 | 🇪🇸 **Spanish content has the best views-to-volume ratio** | 9 titles averaging 229M views — highest of any country |
| 6 | ⭐ **Quality and popularity are largely independent** | IMDb ↔ Viewership correlation is only +0.07 (near zero) |

---

## 📈 Visualizations Generated

### Figure 1 — Univariate / Descriptive Analysis
`eda_fig1_univariate.png` — 6 panels:
- IMDb score histogram
- IMDb quality band pie chart
- Content count per year
- Top 10 genres by count
- Content by country
- Releases by month

### Figure 2 — Multivariate & Correlation Analysis
`eda_fig2_multivariate.png` — 6 panels:
- Correlation heatmap (IMDb, Viewership, Duration, Year)
- IMDb vs Viewership scatter plot with trendline
- Avg Viewership by IMDb Band
- Avg Viewership by Country
- Yearly avg IMDb trend line
- Avg Viewership by Genre (top 8)

---

## 🖥️ Static Dashboard Mock-up

`Netflix_Dashboard.pptx` — 7-slide PowerPoint deck covering:

| Slide | Content |
|---|---|
| 1 | Title slide with key dataset metrics |
| 2 | KPI overview — 5 KPI cards + 5 insight cards |
| 3 | Content analysis — genre, country, duration, release month charts |
| 4 | Viewership analysis — yearly trend, genre, country, IMDb band charts |
| 5 | SQL business questions — 6 queries with code and findings |
| 6 | Top titles table + #1 most-watched title each year (2016–2025) |
| 7 | Key insights and 6 business recommendations |

Open in Microsoft PowerPoint or import into Google Slides (File → Import Slides).

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| Python 3 | Core scripting language |
| Pandas | Data loading, groupby analysis, SQL execution |
| Matplotlib | Chart generation (histogram, bar, scatter, pie, line) |
| Seaborn | Correlation heatmap |
| NumPy | Trendline calculation |
| SQLite (built-in) | SQL query engine — no setup needed |

---

## 📤 Deliverables Checklist

- [x] `eda_analysis.py` — full Python EDA script (12 sections)
- [x] `sql_queries.sql` — 7 business SQL queries with comments and results
- [x] `eda_report.md` — written analysis report with all findings
- [x] `eda_fig1_univariate.png` — descriptive analysis charts
- [x] `eda_fig2_multivariate.png` — multivariate & correlation charts
- [x] `Netflix_Dashboard.pptx` — static PowerPoint dashboard mock-up
- [x] `README.md` — this file

---

## 👤 Author

**[Your Name]**
Data Analytics Intern
[Your LinkedIn Profile] | [Your GitHub Profile]
