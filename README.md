# AMAZON-EDA

This Exploratory Data Analysis (EDA) project focuses on analyzing the content available on Amazon Prime Video, including both movies and TV shows, using two datasets: titles.csv (containing metadata like title, type, genre, runtime, release year, etc.) and credits.csv (containing information about actors and directors). The objective is to uncover patterns, trends, and insights related to the types of content, genres, countries of origin, and the popularity and ratings of the content on the platform.

The initial phase involved data loading and inspection. Both datasets were successfully loaded using Pandas, and initial exploratory functions like .head(), .info(), and .describe() were used to understand the structure. The titles.csv dataset has 9,871 entries, while credits.csv contains over 124,000 records of cast and crew.

In the data cleaning stage, key columns like genres and production_countries, which were stored as stringified lists, were converted into proper Python list objects using conditional ast.literal_eval(). Missing values in important columns such as age_certification, imdb_score, and imdb_votes were filled using appropriate strategies—either default values or column means.

For the Exploratory Data Analysis, multiple visualizations were created using Seaborn and Matplotlib to answer meaningful business and analytical questions.

Key findings include:

Content Type: A significantly higher number of movies are available compared to TV shows on Amazon Prime.

Release Year Trend: Content production has grown over time, peaking around 2019–2021, showing Amazon's aggressive expansion in recent years.

Genres: The most dominant genres are Drama, Comedy, Action, and Romance, which reflects mainstream viewer interests.

IMDb Score Distribution: Most content has IMDb scores in the 6.0 to 8.5 range, indicating generally favorable reception.

Country of Origin: A majority of the content originates from the United States, followed by India, the UK, and Canada.

Runtime Analysis: Movies tend to have a wider spread in runtime (ranging from under 60 minutes to over 180), while shows typically have consistent episode lengths.

Top Actors: Using the credits.csv, the most frequent actors across Amazon Prime content were identified, with names like Joe Besser, Moe Howard, and Larry Fine appearing frequently.

Top Directors: Directors like Michael Curtiz and Alfred Hitchcock were among the most frequently occurring.

The visualizations used included bar plots, line plots, pie charts, histograms, boxplots, and a heatmap for correlation analysis of IMDb and TMDB scores and popularity metrics.

The project concluded with several meaningful insights about how Amazon Prime curates its content, focusing on high-rated, U.S.-based, drama/comedy-oriented material, while increasingly investing in TV series production post-2018. These insights are crucial for understanding customer engagement, planning future content acquisition, or designing recommendation engines.

This project demonstrates the power of Python-based EDA to convert raw data into meaningful, actionable information using libraries like Pandas, Matplotlib, Seaborn, and ast. It serves as a foundational exercise for any data-driven content strategy or recommendation system development in the media and entertainment industry.

keyboard_arrow_down
