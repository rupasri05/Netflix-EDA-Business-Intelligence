# 📊 EDA Report — Netflix Global Content Insights (2016–2025)

**Assignment:** Exploratory Data Analysis & Business Intelligence  
**Dataset:** `netflix_cleaned.csv` — 200 rows × 16 columns  
**Tools:** Python 3, Pandas, Matplotlib, Seaborn, SQLite  
**Script:** `eda_analysis.py`

---

## 1. 📐 Descriptive Statistics — Numerical Variables

The table below summarises the three key numerical columns across all 200 titles:

| Metric | IMDb Score | Viewership (M) | Duration (Min) |
|---|---|---|---|
| **Count** | 200 | 187 (13 missing) | 200 |
| **Mean** | 7.70 | 81.9 | 442.9 |
| **Median** | 7.70 | 33.5 | 400.0 |
| **Std Dev** | 0.76 | 144.8 | 208.4 |
| **Min** | 4.30 | 1.8 | 104 |
| **25th %ile** | 7.30 | 10.85 | 300.0 |
| **75th %ile** | 8.20 | 68.6 | 502.5 |
| **Max** | 9.30 | 792.0 | 1800 |

**Key observations:**

- **IMDb** scores are tightly clustered — mean and median are both 7.70, indicating a symmetric distribution with very little skew. Netflix's catalogue skews high quality overall.
- **Viewership** has an extremely high standard deviation (144.8M) relative to its mean (81.9M), meaning a small number of blockbuster titles drive the bulk of total views. The median of 33.5M is far below the mean, confirming a right-skewed distribution.
- **Duration** ranges widely from 104 minutes (short film/miniseries) to 1,800 minutes (long multi-season run), with the average sitting at 442.9 minutes — roughly equivalent to a mid-length series.

---

## 2. 🔡 Categorical Variable Summaries

### 2.1 IMDb Quality Band Distribution

| Band | Count | % of Total |
|---|---|---|
| Good (7.5 – 8.4) | 97 | 48.5% |
| Average (6.5 – 7.4) | 57 | 28.5% |
| Excellent (≥ 8.5) | 36 | 18.0% |
| Below Average (< 6.5) | 10 | 5.0% |

**133 titles (66.5%)** fall into the Good or Excellent bands, confirming Netflix predominantly acquires and produces high-quality content. Only 10 titles (5%) fall below average.

### 2.2 Top 5 Genres by Title Count

| Genre | Count |
|---|---|
| Crime Drama | 14 |
| Coming-of-age | 8 |
| Heist / Crime | 5 |
| Comedy | 5 |
| Sci-Fi / Horror | 5 |

Crime-related genres (Crime Drama + Heist/Crime) together account for **19 titles (9.5%)**, making crime the dominant content theme on the platform.

### 2.3 Content by Country (Top 6)

| Country | Titles | Avg IMDb |
|---|---|---|
| USA | 124 | 7.65 |
| UK | 27 | 8.12 |
| South Korea | 20 | 7.90 |
| Spain | 9 | 7.46 |
| Canada | 4 | 8.48 |
| Germany | 4 | 7.60 |

The USA dominates in volume at **62% of the catalogue**, but Canada and UK lead on average quality. South Korea sits in 3rd place by volume with a strong average IMDb of 7.90.

---

## 3. 📈 Univariate Analysis

### 3.1 IMDb Score Distribution

- Only **6 out of 200 titles** (3%) score below 6.0 on IMDb.
- **83 out of 200 titles** (41.5%) score 8.0 or above.
- The distribution is approximately bell-shaped centred at 7.70, with a slight left tail representing a small number of poor-performing titles.

### 3.2 Release Month Distribution

| Month | Releases | | Month | Releases |
|---|---|---|---|---|
| January | **25** ← busiest | | July | 13 |
| February | 18 | | August | **10** ← quietest |
| March | 22 | | September | 21 |
| April | 16 | | October | 17 |
| May | 16 | | November | 16 |
| June | 12 | | December | 14 |

- **January** is the single busiest release month with 25 titles.
- **August** is the quietest with only 10 releases.
- **Q1 (January–March)** accounts for 65 releases — **32.5% of the entire annual catalogue** — meaning Netflix front-loads the year heavily.

### 3.3 Yearly Content Volume

Each year from 2016 to 2025 contains exactly **20 titles**, making this a perfectly balanced dataset with consistent annual representation across all 10 years.

---

## 4. 🔗 Multivariate Analysis

### 4.1 Correlation Matrix

| | IMDb | Viewership_M | Duration_Min | Year |
|---|---|---|---|---|
| **IMDb** | 1.000 | +0.069 | +0.210 | −0.208 |
| **Viewership_M** | +0.069 | 1.000 | +0.198 | +0.140 |
| **Duration_Min** | +0.210 | +0.198 | 1.000 | +0.007 |
| **Year** | −0.208 | +0.140 | +0.007 | 1.000 |

**Key findings from the correlation matrix:**

| Pair | Correlation | Interpretation |
|---|---|---|
| IMDb ↔ Duration_Min | +0.210 | Weak positive — longer content tends to rate slightly higher |
| Year ↔ IMDb | −0.208 | Slight decline in avg quality rating over time |
| IMDb ↔ Viewership_M | +0.069 | Near zero — quality does NOT reliably predict popularity |
| Year ↔ Viewership_M | +0.140 | Slight positive — viewership has grown modestly over the years |

> **Critical insight:** The near-zero correlation between IMDb score and viewership (0.069) tells us that **critical quality and audience popularity are largely independent**. A title can be excellent and unpopular, or mediocre and massively watched.

### 4.2 IMDb Band vs Average Viewership

| Band | Avg Viewership (M) |
|---|---|
| Excellent (≥ 8.5) | **95.8M** |
| Good (7.5 – 8.4) | 92.0M |
| Average (6.5 – 7.4) | 64.6M |
| Below Average (< 6.5) | 33.8M |

Excellent titles earn **2.8× more views** than Below Average titles. While the correlation is weak overall, there is still a meaningful viewership premium for the highest-quality content.

### 4.3 Genre vs Average Viewership (Top 10)

| Rank | Genre | Avg Viewership (M) |
|---|---|---|
| 1 | Zombie Horror | 679.0 |
| 2 | Musical Fantasy | 482.0 |
| 3 | Teen Drama / Mystery | 475.0 |
| 4 | Legal Drama | 402.0 |
| 5 | Heist / Crime | 388.4 |
| 6 | Period Romance | 291.8 |
| 7 | Fantasy Drama | 263.0 |
| 8 | Survival Drama | 201.2 |
| 9 | True Crime Drama | 190.9 |
| 10 | Supernatural Mystery | 188.0 |

Zombie Horror tops the chart, driven by blockbuster titles. Heist/Crime ranks 5th with 388.4M — notable because it has 5 titles (more than most top genres), making it the most **consistently high-performing** genre at scale.

### 4.4 Country vs Average Viewership

| Country | Titles | Avg IMDb | Avg Viewership (M) |
|---|---|---|---|
| Spain | 9 | 7.46 | **229.1** |
| South Korea | 20 | 7.90 | **143.9** |
| Germany | 4 | 7.60 | 116.0 |
| USA | 124 | 7.65 | 76.0 |
| France | 3 | 6.33 | 61.3 |
| UK | 27 | 8.12 | 39.7 |

**Spain** produces the fewest titles among the top countries yet averages the highest viewership at 229.1M — nearly **3× the USA average** of 76M. South Korea similarly outperforms its share, averaging 143.9M views with 20 titles. The UK produces highly rated content (8.12 avg IMDb) but averages a lower 39.7M views.

### 4.5 Yearly Average IMDb Trend

| Year | Avg IMDb | | Year | Avg IMDb |
|---|---|---|---|---|
| 2016 | 7.92 | | 2021 | 7.53 |
| 2017 | 7.74 | | 2022 | 7.71 |
| 2018 | 7.86 | | 2023 | 7.64 |
| 2019 | **8.21** ← peak | | 2024 | **7.18** ← lowest |
| 2020 | 7.52 | | 2025 | 7.64 |

**2019** was the highest-quality year on average (8.21), driven by titles like Stranger Things 3 and Our Planet. **2024** was the lowest (7.18), possibly reflecting a broader push for volume over quality. The overall trend shows a modest decline from 2019 onwards.

### 4.6 Release Month vs Average Viewership

| Month | Avg Viewership (M) | | Month | Avg Viewership (M) |
|---|---|---|---|---|
| June | **115.8** ← best | | September | 84.4 |
| July | 110.2 | | August | 78.3 |
| December | 94.8 | | November | 70.8 |
| May | 94.1 | | April | 67.3 |
| March | 91.7 | | February | 60.1 |
| January | 89.4 | | October | **34.2** ← worst |

**June is the single best month** to release a title (115.8M avg), closely followed by July (110.2M). October is the worst performing month at just 34.2M average — a **3.4× gap** compared to June. Summer releases (June–July) consistently outperform the rest of the year, likely due to school holidays and increased leisure time.

### 4.7 Duration vs Average Viewership

| Duration Bucket | Titles | Avg IMDb | Avg Viewership (M) |
|---|---|---|---|
| Long (500+ min) | 59 | 7.86 | **122.4** |
| Medium (300–500 min) | 112 | 7.66 | 74.8 |
| Short (< 300 min) | 29 | 7.48 | 33.6 |

Long-form content (500+ minutes) generates **3.6× more viewership** than short content and also carries a higher average IMDb score (7.86 vs 7.48). This strongly suggests that investing in multi-season renewals and longer series is the highest-ROI content strategy.

---

## 5. 🏆 Key Business Insights Summary

| # | Insight | Supporting Data |
|---|---|---|
| 1 | **Korean & Spanish content is severely underinvested** | Spain: 9 titles, 229M avg views. S.Korea: 20 titles, 143.9M avg views. Both far exceed USA's 76M avg |
| 2 | **Schedule premium titles in June–July** | June 115.8M avg vs October 34.2M avg — a 3.4× difference from timing alone |
| 3 | **Renew for more seasons — long content dominates** | 500+ min content averages 122.4M vs 33.6M for short — a 3.6× difference |
| 4 | **Quality and popularity are independent** | IMDb ↔ Viewership correlation = +0.069 (near zero). Marketing and timing matter as much as quality |
| 5 | **Crime and Heist genres are the most reliable performers** | Heist/Crime: 5 titles, 388.4M avg — the most consistently high-performing genre at scale |
| 6 | **2019 represents the quality benchmark to aim for** | Peak avg IMDb of 8.21 in 2019 — the standard for a golden-year lineup |

---

## 6. 📁 Deliverables

| File | Description |
|---|---|
| `eda_analysis.py` | Python script — runs all 12 analysis sections and generates charts |
| `sql_queries.sql` | 7 business SQL queries with results and comments |
| `eda_fig1_univariate.png` | 6-panel descriptive / univariate chart |
| `eda_fig2_multivariate.png` | 6-panel multivariate & correlation chart |
| `Netflix_Dashboard.pptx` | 7-slide static PowerPoint dashboard mock-up |
| `eda_report.md` | This report |
