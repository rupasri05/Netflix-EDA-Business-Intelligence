import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np

RED    = "#E50914"
DARK   = "#141414"
CARD   = "#1f1f1f"
WHITE  = "#FFFFFF"
MUTED  = "#b3b3b3"
GOLD   = "#f5c518"
TEAL   = "#00b4d8"
PALETTE = [RED, GOLD, TEAL, "#b3b3b3", "#ff6b6b", "#4ecdc4", "#95e1d3", "#f38181"]

plt.rcParams.update({
    "figure.facecolor":  DARK,
    "axes.facecolor":    CARD,
    "axes.edgecolor":    "#333",
    "axes.labelcolor":   WHITE,
    "xtick.color":       MUTED,
    "ytick.color":       MUTED,
    "text.color":        WHITE,
    "grid.color":        "#2a2a2a",
    "grid.linewidth":    0.8,
    "font.family":       "DejaVu Sans",
})

# LOAD DATA
print("--- Loading Dataset ---")

df = pd.read_csv("netflix_cleaned.csv")

print(f"\nShape  : {df.shape[0]} rows x {df.shape[1]} columns")
print(f"\nFirst 3 rows:")
print(df.head(3).to_string())
print(f"\nData types:")
print(df.dtypes)

# 1 — DESCRIPTIVE STATISTICS (Numerical)
print("\n" + "=" * 60)
print("1: Descriptive Statistics - Numerical Columns")
print("=" * 60)

num_cols = ["IMDb", "Viewership_M", "Duration_Min"]
print(df[num_cols].describe().round(2).to_string())

print("\n--- Key Stats ---")
print(f"IMDb     Mean:{df['IMDb'].mean():.2f}  Median:{df['IMDb'].median():.2f}  Std:{df['IMDb'].std():.2f}  Min:{df['IMDb'].min()}  Max:{df['IMDb'].max()}")
print(f"Views_M  Mean:{df['Viewership_M'].mean():.1f}  Median:{df['Viewership_M'].median():.1f}  Std:{df['Viewership_M'].std():.1f}  Min:{df['Viewership_M'].min()}  Max:{df['Viewership_M'].max()}")
print(f"Dur_Min  Mean:{df['Duration_Min'].mean():.1f}  Median:{df['Duration_Min'].median():.1f}  Std:{df['Duration_Min'].std():.1f}  Min:{df['Duration_Min'].min()}  Max:{df['Duration_Min'].max()}")

# 2 — CATEGORICAL SUMMARIES
print("\n" + "=" * 60)
print("2: Categorical Variable Summaries")
print("=" * 60)

# 2a. IMDb Quality Band
print("\n--- IMDb Quality Band Distribution ---")
band_counts = df["IMDb_Band"].value_counts()
band_pct    = (band_counts / len(df) * 100).round(1)
print(pd.DataFrame({"Count": band_counts, "% of Total": band_pct}).to_string())
print(f"\nNote: {(df['IMDb_Band'].isin(['Good','Excellent'])).sum()} titles ({(df['IMDb_Band'].isin(['Good','Excellent'])).sum()/len(df)*100:.1f}%) are Good or Excellent")

# 2b. Top 5 Genres
print("\n--- Top 5 Genres by Title Count ---")
print(df["Genre"].value_counts().head(5).to_string())

# 2c. Content by Country with avg IMDb
print("\n--- Content by Country (Top 6) ---")
country_summary = (df.groupby("Primary_Country")
                     .agg(Titles=("Title","count"),
                          Avg_IMDb=("IMDb", lambda x: round(x.mean(),2)))
                     .sort_values("Titles", ascending=False)
                     .head(6))
print(country_summary.to_string())

# 3 — UNIVARIATE ANALYSIS
print("\n" + "=" * 60)
print("3: Univariate Analysis")
print("=" * 60)

# 3a. IMDb distribution facts
print(f"\nTitles with IMDb < 6.0 : {(df['IMDb'] < 6.0).sum()} out of {len(df)}")
print(f"Titles with IMDb >= 8.0: {(df['IMDb'] >= 8.0).sum()} out of {len(df)}")

# 3b. Release month counts
print("\n--- Release Month Distribution ---")
month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]
month_counts = df["Release_Month"].value_counts().reindex(month_order).fillna(0).astype(int)
print(month_counts.to_string())
print(f"\nBusiest month : {month_counts.idxmax()} ({month_counts.max()} releases)")
print(f"Quietest month: {month_counts.idxmin()} ({month_counts.min()} releases)")
q1 = month_counts[["January","February","March"]].sum()
print(f"Q1 (Jan-Mar)  : {q1} releases = {q1/len(df)*100:.1f}% of all")

# 3c. Yearly content count
print("\n--- Yearly Content Count ---")
print(df["Year"].value_counts().sort_index().to_string())

# 4 — MULTIVARIATE ANALYSIS
print("\n" + "=" * 60)
print("4: Multivariate Analysis")
print("=" * 60)

# 4a. Correlation matrix

print("\n--- Correlation Matrix ---")
corr = df[["IMDb","Viewership_M","Duration_Min","Year"]].corr().round(3)
print(corr.to_string())

print("\n--- Key Pairs (from report) ---")
print(f"IMDb <-> Duration_Min : {corr.loc['IMDb','Duration_Min']:+.3f}  (weak positive)")
print(f"Year <-> IMDb         : {corr.loc['Year','IMDb']:+.3f}  (slight decline over time)")
print(f"IMDb <-> Viewership_M : {corr.loc['IMDb','Viewership_M']:+.3f}  (near zero)")
print(f"Year <-> Viewership_M : {corr.loc['Year','Viewership_M']:+.3f}  (slight growth)")

# 4b. IMDb BAND vs AVG VIEWERSHIP

print("\n--- IMDb Band vs Average Viewership ---")

band_order = ["Excellent","Good","Average","Below Average"]
band_views = df.groupby("IMDb_Band")["Viewership_M"].mean().reindex(band_order).round(1)
print(band_views.to_string())
print(f"\nExcellent vs Below Average: {band_views['Excellent']/band_views['Below Average']:.1f}x more views")

# 4c. GENRE vs AVG VIEWERSHIP
print("\n--- Genre vs Average Viewership (Top 10) ---")

genre_views = (df.groupby("Genre")["Viewership_M"]
                 .mean()
                 .sort_values(ascending=False)
                 .head(10)
                 .round(1))
print(genre_views.to_string())

# 4d. COUNTRY vs VIEWERSHIP & IMDb
print("\n--- Country vs Avg Viewership and IMDb ---")

country_perf = (df.groupby("Primary_Country")
                  .agg(
                      Titles=("Title","count"),
                      Avg_IMDb=("IMDb", lambda x: round(x.mean(),2)),
                      Avg_Views_M=("Viewership_M", lambda x: round(x.mean(),1))
                  )
                  .sort_values("Avg_Views_M", ascending=False)
                  .head(10))
print(country_perf.to_string())
print("\nNote from report: Spain lowest avg IMDb but HIGHEST avg viewership")

# 4e. YEARLY AVG IMDb TREND
print("\n--- Yearly Average IMDb Trend ---")

yearly_imdb = df.groupby("Year")["IMDb"].mean().round(2)
print(yearly_imdb.to_string())
print(f"\nPeak year (IMDb)  : {yearly_imdb.idxmax()} ({yearly_imdb.max()})")
print(f"Lowest year (IMDb): {yearly_imdb.idxmin()} ({yearly_imdb.min()})")

# 4f. RELEASE MONTH vs VIEWERSHIP
print("\n--- Release Month vs Avg Viewership ---")

month_views = (df.groupby("Release_Month")["Viewership_M"]
                 .mean()
                 .sort_values(ascending=False)
                 .round(1))
print(month_views.to_string())

best  = month_views.idxmax()
worst = month_views.idxmin()
print(f"\nBest  month: {best}  ({month_views[best]}M avg)")
print(f"Worst month: {worst} ({month_views[worst]}M avg)")
print(f"Ratio: {month_views[best]/month_views[worst]:.1f}x")

# 4g. DURATION vs VIEWERSHIP
print("\n--- Duration Bucket vs Avg Viewership ---")

def duration_bucket(mins):
    if mins < 300:  return "Short (<300 min)"
    elif mins < 500: return "Medium (300-500 min)"
    else:            return "Long (500+ min)"

df["Duration_Bucket"] = df["Duration_Min"].apply(duration_bucket)

dur_views = (df.groupby("Duration_Bucket")
               .agg(Titles=("Title","count"),
                    Avg_IMDb=("IMDb", lambda x: round(x.mean(),2)),
                    Avg_Views_M=("Viewership_M", lambda x: round(x.mean(),1)))
               .sort_values("Avg_Views_M", ascending=False))
print(dur_views.to_string())
long_avg  = dur_views.loc["Long (500+ min)","Avg_Views_M"]
short_avg = dur_views.loc["Short (<300 min)","Avg_Views_M"]
print(f"\nLong vs Short viewership ratio: {long_avg/short_avg:.1f}x")

# 5 — VISUALIZATIONS
print("\n" + "=" * 60)
print("5: Generating Visualization Charts")
print("=" * 60)

# ── FIGURE 1: Univariate / Descriptive ───────────────────────────────────────
fig = plt.figure(figsize=(20, 14), facecolor=DARK)
fig.suptitle("Netflix Content Insights 2016-2025 - Descriptive Analysis",
             fontsize=20, fontweight="bold", color=WHITE, y=0.97)
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

# Panel 1 - IMDb Histogram
ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(df["IMDb"], bins=18, color=RED, edgecolor=DARK, alpha=0.9)
ax1.axvline(df["IMDb"].mean(), color=GOLD, linewidth=2, linestyle="--",
            label=f"Mean: {df['IMDb'].mean():.2f}")
ax1.set_title("IMDb Score Distribution", fontweight="bold", color=WHITE)
ax1.set_xlabel("IMDb Score"); ax1.set_ylabel("Count")
ax1.legend(fontsize=9); ax1.grid(axis="y", alpha=0.4)

# Panel 2 - IMDb Band Pie
ax2 = fig.add_subplot(gs[0, 1])
band_c = df["IMDb_Band"].value_counts()
ax2.pie(band_c, labels=band_c.index, autopct="%1.0f%%",
        colors=[RED, GOLD, TEAL, "#666"], startangle=140,
        textprops={"color": WHITE, "fontsize": 9},
        wedgeprops={"edgecolor": DARK, "linewidth": 2})
ax2.set_title("Content by IMDb Quality Band", fontweight="bold", color=WHITE)

# Panel 3 - Content per Year
ax3 = fig.add_subplot(gs[0, 2])
yr = df["Year"].value_counts().sort_index()
ax3.bar(yr.index, yr.values, color=TEAL, edgecolor=DARK, width=0.7)
ax3.set_title("Content Count per Year", fontweight="bold", color=WHITE)
ax3.set_xlabel("Year"); ax3.set_ylabel("Count"); ax3.grid(axis="y", alpha=0.4)

# Panel 4 - Top 10 Genres
ax4 = fig.add_subplot(gs[1, 0])
top_g = df["Genre"].value_counts().head(10)
cols_g = [RED if i == 0 else "#555" for i in range(10)]
ax4.barh(top_g.index[::-1], top_g.values[::-1], color=cols_g[::-1])
ax4.set_title("Top 10 Genres by Count", fontweight="bold", color=WHITE)
ax4.set_xlabel("Count"); ax4.grid(axis="x", alpha=0.4)

# Panel 5 - Content by Country
ax5 = fig.add_subplot(gs[1, 1])
top_c = df["Primary_Country"].value_counts().head(8)
ax5.bar(top_c.index, top_c.values, color=PALETTE[:8], edgecolor=DARK)
ax5.set_title("Count by Country", fontweight="bold", color=WHITE)
ax5.set_xlabel("Country"); ax5.set_ylabel("Count")
plt.setp(ax5.xaxis.get_majorticklabels(), rotation=30, ha="right", fontsize=8)
ax5.grid(axis="y", alpha=0.4)

# Panel 6 - Releases by Month
ax6 = fig.add_subplot(gs[1, 2])
month_short = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
month_map = dict(zip(
    ["January","February","March","April","May","June",
     "July","August","September","October","November","December"],
    month_short))
df["Month_Short"] = df["Release_Month"].map(month_map)
mc = df["Month_Short"].value_counts().reindex(month_short).fillna(0)
ax6.bar(mc.index, mc.values, color=GOLD, edgecolor=DARK, alpha=0.9)
ax6.set_title("Releases by Month", fontweight="bold", color=WHITE)
ax6.set_xlabel("Month"); ax6.set_ylabel("Count"); ax6.grid(axis="y", alpha=0.4)

plt.savefig("eda_fig1_univariate.png", dpi=150, bbox_inches="tight", facecolor=DARK)
plt.close()
print("Saved: eda_fig1_univariate.png")

# ── FIGURE 2: Multivariate / Correlation ─────────────────────────────────────
fig2 = plt.figure(figsize=(20, 14), facecolor=DARK)
fig2.suptitle("Netflix Content Insights 2016-2025 - Multivariate Analysis",
              fontsize=20, fontweight="bold", color=WHITE, y=0.97)
gs2 = gridspec.GridSpec(2, 3, figure=fig2, hspace=0.45, wspace=0.38)

# Panel 1 - Correlation Heatmap
ax1 = fig2.add_subplot(gs2[0, 0])
corr_plot = df[["IMDb","Viewership_M","Duration_Min","Year"]].corr()
sns.heatmap(corr_plot, annot=True, fmt=".2f", cmap="RdYlGn", center=0,
            ax=ax1, linewidths=1, linecolor=DARK,
            annot_kws={"size": 10, "color": "white"},
            cbar_kws={"shrink": 0.8})
ax1.set_title("Correlation Heatmap", fontweight="bold", color=WHITE)
ax1.tick_params(colors=MUTED)

# Panel 2 - IMDb vs Viewership Scatter
ax2 = fig2.add_subplot(gs2[0, 1])
sdf = df.dropna(subset=["Viewership_M"])
sc = ax2.scatter(sdf["IMDb"], sdf["Viewership_M"],
                 c=sdf["Year"], cmap="RdYlGn", alpha=0.75, s=55, edgecolors="none")
cbar = fig2.colorbar(sc, ax=ax2, shrink=0.85)
cbar.set_label("Year", color=MUTED, fontsize=8)
cbar.ax.yaxis.set_tick_params(color=MUTED)
plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color=MUTED)
z = np.polyfit(sdf["IMDb"], sdf["Viewership_M"], 1)
xline = np.linspace(sdf["IMDb"].min(), sdf["IMDb"].max(), 100)
ax2.plot(xline, np.poly1d(z)(xline), color=RED, linewidth=2, linestyle="--")
ax2.set_title("IMDb Score vs Viewership", fontweight="bold", color=WHITE)
ax2.set_xlabel("IMDb Score"); ax2.set_ylabel("Viewership (M)"); ax2.grid(alpha=0.3)

# Panel 3 - IMDb Band vs Avg Viewership
ax3 = fig2.add_subplot(gs2[0, 2])
bv = df.groupby("IMDb_Band")["Viewership_M"].mean().reindex(["Excellent","Good","Average","Below Average"])
bars = ax3.bar(bv.index, bv.values, color=[GOLD,TEAL,"#888","#555"], edgecolor=DARK)
for bar, val in zip(bars, bv.values):
    ax3.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1,
             f"{val:.0f}M", ha="center", va="bottom", fontsize=9, color=WHITE)
ax3.set_title("Avg Viewership by IMDb Band", fontweight="bold", color=WHITE)
ax3.set_ylabel("Avg Viewership (M)"); ax3.grid(axis="y", alpha=0.4)
plt.setp(ax3.xaxis.get_majorticklabels(), rotation=15)

# Panel 4 - Country vs Avg Viewership
ax4 = fig2.add_subplot(gs2[1, 0])
vc = df.groupby("Primary_Country")["Viewership_M"].mean().sort_values(ascending=False).head(8)
bar_cols = [RED if c == "Spain" else TEAL for c in vc.index[::-1]]
ax4.barh(vc.index[::-1], vc.values[::-1], color=bar_cols)
ax4.set_title("Avg Viewership by Country", fontweight="bold", color=WHITE)
ax4.set_xlabel("Avg Viewership (M)"); ax4.grid(axis="x", alpha=0.4)

# Panel 5 - Yearly Avg IMDb Trend
ax5 = fig2.add_subplot(gs2[1, 1])
yi = df.groupby("Year")["IMDb"].mean()
ax5.plot(yi.index, yi.values, color=GOLD, linewidth=2.5, marker="o", markersize=7)
ax5.fill_between(yi.index, yi.values, alpha=0.15, color=GOLD)
ax5.set_title("Avg IMDb Score by Year", fontweight="bold", color=WHITE)
ax5.set_xlabel("Year"); ax5.set_ylabel("Avg IMDb"); ax5.grid(alpha=0.3); ax5.set_ylim(7.0,8.4)

# Panel 6 - Genre vs Avg Viewership
ax6 = fig2.add_subplot(gs2[1, 2])
top8 = df["Genre"].value_counts().head(8).index
gv = df[df["Genre"].isin(top8)].groupby("Genre")["Viewership_M"].mean().sort_values(ascending=False)
ax6.barh(gv.index[::-1], gv.values[::-1], color=RED, alpha=0.85, edgecolor=DARK)
ax6.set_title("Avg Viewership by Genre (top 8)", fontweight="bold", color=WHITE)
ax6.set_xlabel("Avg Viewership (M)"); ax6.grid(axis="x", alpha=0.4)

plt.savefig("eda_fig2_multivariate.png", dpi=150, bbox_inches="tight", facecolor=DARK)
plt.close()
print("Saved: eda_fig2_multivariate.png")

print("\n" + "=" * 60)
print("ALL EDA SECTIONS COMPLETE")
print("Charts: eda_fig1_univariate.png, eda_fig2_multivariate.png")
print("=" * 60)