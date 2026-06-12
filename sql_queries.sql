-- ============================================================
-- Netflix Global Content Insights — SQL Business Queries
-- Dataset : netflix_cleaned.csv (loaded as table: netflix)
-- Engine  : SQLite  |  Run via: python3 sql_queries.py
-- ============================================================


-- ─────────────────────────────────────────────────────────────
-- Q1. What is the #1 most-watched Netflix title each year?
-- Business use: Year-over-year blockbuster tracking
-- ─────────────────────────────────────────────────────────────
SELECT Year, Title, Genre, Viewership_M, Viewership_Unit
FROM netflix
WHERE Viewership_M IS NOT NULL
  AND Viewership_M = (
        SELECT MAX(n2.Viewership_M)
        FROM netflix n2
        WHERE n2.Year = netflix.Year
          AND n2.Viewership_M IS NOT NULL
  )
ORDER BY Year;

/*
Results:
Year | Title                   | Genre           | Viewership_M | Unit
2016 | Orange Is the New Black | Comedy Drama    | 23.0         | Streams
2017 | Ozark                   | Crime Drama     | 491.0        | Hours
2018 | 13 Reasons Why          | Teen Drama      | 496.0        | Hours
2019 | Stranger Things 3       | Sci-Fi/Horror   | 582.0        | Hours
2020 | Money Heist             | Heist / Crime   | 619.0        | Hours
2021 | Money Heist             | Heist / Crime   | 792.0        | Hours
2022 | All of Us Are Dead      | Zombie Horror   | 679.0        | Hours
2023 | The Night Agent         | Action Thriller | 99.2         | Views
2024 | Squid Game 2            | Survival Drama  | 192.6        | Views
2025 | KPop Demon Hunters      | Musical Fantasy | 482.0        | Views

Insight: Crime & Thriller genres dominate annual #1 spots.
         Money Heist is the only title to top the charts 2 years running.
*/


-- ─────────────────────────────────────────────────────────────
-- Q2. Which country produces the highest-rated Netflix content
--     (minimum 2 titles to be meaningful)?
-- Business use: Guide international co-production strategy
-- ─────────────────────────────────────────────────────────────
SELECT Primary_Country,
       COUNT(*)                    AS total_titles,
       ROUND(AVG(IMDb), 2)         AS avg_imdb,
       ROUND(AVG(Viewership_M), 1) AS avg_viewership_M
FROM netflix
GROUP BY Primary_Country
HAVING total_titles >= 2
ORDER BY avg_imdb DESC;

/*
Results:
Country      | Titles | Avg IMDb | Avg Viewership (M)
Canada       |   4    |   8.47   |   7.3
UK           |  27    |   8.12   |  39.7
South Korea  |  20    |   7.90   | 143.9
USA          | 124    |   7.65   |  76.0
Germany      |   4    |   7.60   | 116.0
Spain        |   9    |   7.46   | 229.1

Insight: Spain has the LOWEST avg IMDb among top producers
         but the HIGHEST avg viewership — proving that
         entertainment value ≠ critical rating.
*/


-- ─────────────────────────────────────────────────────────────
-- Q3. Which genres drive the most engagement?
--     (genres with at least 3 titles)
-- Business use: Content commissioning decisions
-- ─────────────────────────────────────────────────────────────
SELECT Genre,
       COUNT(*)                     AS title_count,
       ROUND(AVG(IMDb), 2)          AS avg_imdb,
       ROUND(AVG(Viewership_M), 1)  AS avg_viewership_M,
       MAX(Viewership_M)            AS peak_viewership_M
FROM netflix
GROUP BY Genre
HAVING title_count >= 3
ORDER BY avg_viewership_M DESC;

/*
Top 5 by Avg Viewership:
Genre              | Count | Avg IMDb | Avg Views (M) | Peak (M)
Heist / Crime      |   5   |   7.72   |    388.4      | 792.0
Period Romance     |   3   |   7.40   |    291.8      | 656.0
Fantasy Drama      |   4   |   7.72   |    263.0      | 541.0
Survival Drama     |   3   |   8.00   |    201.2      | 265.2
True Crime Drama   |   3   |   7.10   |    190.9      | 511.0

Insight: Heist/Crime genre averages 388M views — nearly double
         the third-placed Fantasy Drama.
*/


-- ─────────────────────────────────────────────────────────────
-- Q4. What is the yearly trend in viewership and quality?
-- Business use: Longitudinal platform growth analysis
-- ─────────────────────────────────────────────────────────────
SELECT Year,
       COUNT(*)                          AS titles,
       ROUND(AVG(IMDb), 2)               AS avg_imdb,
       ROUND(AVG(Viewership_M), 1)       AS avg_viewership_M,
       ROUND(SUM(Viewership_M), 0)       AS total_viewership_M
FROM netflix
GROUP BY Year
ORDER BY Year;

/*
Year | Avg IMDb | Avg Views (M) | Total Views (M)
2016 |   7.92   |     7.4       |    147
2017 |   7.75   |    79.5       |   1511
2018 |   7.87   |    41.8       |    794
2019 |   8.21   |    75.8       |   1515
2020 |   7.53   |    82.9       |   1409
2021 |   7.53   |   107.3       |   2039
2022 |   7.71   |   306.6       |   3985   ← peak year
2023 |   7.64   |    41.0       |    821   ← unit change to Views
2024 |   7.18   |    61.0       |   1219
2025 |   7.64   |    93.7       |   1874

Insight: 2022 was the peak year for cumulative viewership.
         The drop in 2023 is partly due to metric unit change
         (Hours → Views), not necessarily a real decline.
*/


-- ─────────────────────────────────────────────────────────────
-- Q5. Which release months generate the highest viewership?
-- Business use: Optimal release scheduling strategy
-- ─────────────────────────────────────────────────────────────
SELECT Release_Month,
       COUNT(*)                    AS releases,
       ROUND(AVG(IMDb), 2)         AS avg_imdb,
       ROUND(AVG(Viewership_M), 1) AS avg_viewership_M
FROM netflix
GROUP BY Release_Month
ORDER BY avg_viewership_M DESC;

/*
Month     | Releases | Avg IMDb | Avg Viewership (M)
June      |    12    |   7.36   |    115.8  ← Best month
July      |    13    |   8.06   |    110.2
December  |    14    |   7.61   |     94.8
May       |    16    |   7.68   |     94.1
March     |    22    |   7.73   |     91.7
October   |    17    |   7.94   |     34.2  ← Worst month

Insight: Summer (Jun–Jul) releases get 3.4× more views than
         October releases. Premium titles should avoid Oct.
*/


-- ─────────────────────────────────────────────────────────────
-- Q6. What are the top 15 critically acclaimed titles
--     (Excellent IMDb band) ranked by viewership?
-- Business use: Identify "prestige + popular" content
-- ─────────────────────────────────────────────────────────────
SELECT Title, Year, Genre, Primary_Country,
       IMDb, Viewership_M,
       "Directors/Creators" AS Director
FROM netflix
WHERE IMDb_Band = 'Excellent'
ORDER BY Viewership_M DESC
LIMIT 15;

/*
Top 5:
Title                  | Year | Genre           | IMDb | Views (M)
Stranger Things 3      | 2019 | Sci-Fi / Horror | 8.7  |  582.0
Ozark                  | 2017 | Crime Drama     | 8.5  |  491.0
Extraordinary Atty Woo | 2022 | Legal Drama     | 8.6  |  402.0
Adolescence            | 2025 | Crime Drama     | 8.8  |  142.6
Stranger Things 4      | 2022 | Sci-Fi / Horror | 8.7  |  140.7

Insight: Stranger Things is Netflix's strongest franchise —
         combining Excellent IMDb with top-tier viewership.
*/


-- ─────────────────────────────────────────────────────────────
-- Q7. Does longer content get more views?
-- Business use: Guide season length / renewal decisions
-- ─────────────────────────────────────────────────────────────
SELECT
    CASE
        WHEN Duration_Min < 300 THEN 'Short (<300 min)'
        WHEN Duration_Min < 500 THEN 'Medium (300–500 min)'
        ELSE 'Long (500+ min)'
    END AS duration_bucket,
    COUNT(*)                    AS titles,
    ROUND(AVG(IMDb), 2)         AS avg_imdb,
    ROUND(AVG(Viewership_M), 1) AS avg_viewership_M
FROM netflix
GROUP BY duration_bucket
ORDER BY avg_viewership_M DESC;

/*
Bucket           | Titles | Avg IMDb | Avg Viewership (M)
Long (500+ min)  |   59   |   7.86   |    122.4
Medium (300-500) |  112   |   7.66   |     74.8
Short (<300 min) |   29   |   7.48   |     33.6

Insight: Long content gets 3.6× more views than short content.
         Every season renewal is a high-ROI investment.
*/
