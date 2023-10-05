# NBA Champion Prediction Project
### Who will be our 2022 champion?

## Overview
"The National Basketball Association (NBA) is a professional basketball league
in North America. The league is composed of 30 teams (29 in the United States
and 1 in Canada) and is one of the major professional sports leagues in the
United States and Canada. It is the premier men's professional basketball league
in the world.” Aware of the huge impact this sport has worldwide and the data
available to us, our final project will focus on learning how historical team
statistics/data can help us predict the 2022 NBA champion using machine learning
models. Additionally, we will analyze important team statistics to help us come
to a consensus about why our machine learning model predicted certain teams as
being the most probable choice for NBA Champion.

We will use a supervised machine learning model, Logistic Regression, to predict
the 2022 NBA Champion. Using our NBA Stats Database that we have created via Web
Scraping and ETL preprocessing we will analyze the machine learning model's
feature importance as well as create Tableau visualizations to further
understand the overall outcome of our predictions. Finally, we'll create a Flask
app to deploy these visualizations and analysis.

<div align="center">
    <img src="assets/images/nba_prediction/website_landing_page.svg"
         alt="app landing page" />
</div>


## Overarching Analysis Questions
* Can we create a machine learning model to predict this year's NBA Champion?
* Which team statistics give the most insight into what a champion team looks
  like?
* What features does the machine learning model weight most heavily, and can
  these provide insight into our analysis?


## Resources
- Data Source: Official Team Stats for NBA: [NBA Advanced Stats](https://www.nba.com/stats/teams/traditional/?sort=W_PCT&dir=-1)
- Software & Tools: Python, Flask, SKlearn, Tableau Public, Javascript, HTML,
  Bootstrap, CSS


## Schema
<div align="center">
    <img src="assets/images/nba_prediction/project_schema.svg"
         alt="project schema" />
</div>


## Entity Relationship Diagram
<div align="center">
    <img src="assets/images/nba_prediction/erd.svg"
         alt="entity relationship diagram" />
</div>


## Exploratory Data Analysis & Visualizations
#### Tableau Visualizations
The Evolution of the NBA: How teams have evolved from playing a paint-dominant
game to players now expected to stretch the floor.
* 3-point data using attempted, made, and percentage of 3-points made
* Offensive Stats: EFG%, Free Throws Percentage, Points off turnovers, Offensive
  Rebounds
* Defensive Stats: Blocks, Steals, Defensive Rebounds, Defensive Rating
* Comparing Past Champions to Current Season: Offensive vs. Defensive Rating,
  Assists vs Turnovers, Effective vs True Shooting Percentages
* Our Machine Learning Model Stats on Predicted Champion via Logistic Regression
  Model, Feature Importance Visual and Analysis


#### Flask App
* We have structured a Flask app that will hold our final dashboard. HTML
  templates were created with a base file that has bootstrap and our own
  additional css file loaded as well as the structure for any other html file to
  inherit from this base file.
* We have included our Tableau visuals in our flask app by writing code to embed
  visuals directly from Tableau and produce a cohesive app


#### Machine Learning Model: Logistic Regression
* We used a Logistic Regression Model to best fit for our goal of predicting a
  champion. Producing an outcome of a possible champions: Memphis Grizzlies
* We have also used this model to analyze feature importance in order to see
  which statistics our champion prediction are most heavily dependent on.


## Game Evolution
The Evolution of the NBA game has come a long way since 1997 (where our data
dates back). We have seen a slow and steady change in how the style of the game
is played.


#### 3 Point Shots
<div align="center">
    <img src="assets/images/nba_prediction/game_evolution_3_pt_shots.svg"
         alt="game evolution for 3 point shots" />
</div>

The first two visuals show an evolution of how teams have evolved from playing a
paint-dominant game to players now expected to stretch the floor. Using 3-Point
shot statistics such as Attempted, Made, and Percentage we can see the shift and
increase in 3-Point shots made in more recent years. From roughly the 2016 &
2017 season, the style of 3-point shots used shifted dramatically. We can assume
that using seasons from 2016 to present in our analysis may show a more accurate
presentation of how teams are playing.


#### Defensive Stats
<div align="center">
    <img src="assets/images/nba_prediction/defensive_stats_by_season.svg"
         alt="defensive stats by season" />
</div>

The Defensive Stats visual shows historical trends for average Blocks, Steals,
Defensive Rebounds, and Defensive Rating.

Blocks: Shows a slight decrease in recent years in the average blocks by teams
Steals: Shows a slight increase in recent years in the average steals by teams
Defensive Rebounds: Shows a gradual increase in recent years in the average defensive rebounds by teams
Defensive Rating: Shows a slight increase in recent years in the average defensive rating by teams


#### Offensive Stats
<div align="center">
    <img src="assets/images/nba_prediction/offensive_stats_by_season.svg"
         alt="offensive stats by season" />
</div>

The Offensive Stats visual shows historical trends for average Effective Field
Goal%, Free Throw Percentage, Points Off Turnovers, and Offensive Rebounds.

Effective Field Goal%: Shows a gradual increase in recent years in the average Effective Field Goal% by teams
Free Throw Percentage: Shows an apparent increase in recent years in the average Free Throw Percentage by teams
Points Off Turnovers: Shows an even distribution without much change in recent years in the average Points Off Turnovers by teams
Offensive Rebounds: Shows an apparent decrease in recent years in the average Offensive Rebounds by teams


## Comparisons
Past Champions vs. Current Playoff Teams compares the regular season stats of
historical NBA champions and how they compare to the regular season stats of the
teams currently playing in the 2022 Playoffs.


#### Offensive vs. Defensive Rating
<div align="center">
    <img src="assets/images/nba_prediction/offensive_vs_defensive_rating_2022_past_comparison.svg"
         alt="offensive versus defensive rating 2022 compared to the past champions" />
</div>

Past champions have historically grouped between the 1st and 3rd quadrants. This
past season shows a rough distribution between quadrants. It will be interesting
to see if the champion team will remain between these two quadrants.


#### Assist% vs. Turnover%
<div align="center">
    <img src="assets/images/nba_prediction/assist_vs_turnover_percentages.svg"
         alt="assist versus turnover percentages" />
</div>

Past champions have historically grouped between the 1st and 3rd quadrants. This
past season shows a somewhat similar distribution between the 1st and 3rd
quadrants. Will be interesting to see if the champion team will remain between
these two quadrants.


#### Effective Field Goal% vs. True Shooting%
<div align="center">
    <img src="assets/images/nba_prediction/effective_field_goal_vs_true_shooting_percentages.svg"
         alt="effective field goal versus true shooting percentages" />
</div>

Past champions have historically grouped between the 1st and 3rd quadrants in a
linear fashion with more recent teams in the first quadrant. This past season
shows a similar linear trend. The champion team may be found in the first
quadrant.

## Defensive and Offensive Stats
#### Offensive Stats
<div align="center">
    <img src="assets/images/nba_prediction/offensive_stats_by_team_2022.svg"
         alt="offensive stats by team in 2022" />
</div>

This dashboard visualizes the Average Effective Field Goal %, Offensive Rebound
%, Turnover %, and Free Throw %. You can view the average for each team and
filter the graph season. Currently, we can see the averages of these four
metrics for the 2022 season. We chose these metrics for the most relevant
offensive statistics because they are most heavily correlated to a successful
offense in the NBA.

Effective FG% adjusts field goal percentage to account for the fact that
three-point field goals count for three points while field goals only count for
two points. Offensive Rebound % is the percentage of available offensive
rebounds a player or team obtains while on the floor. Turnover % is the
percentage of plays that end in a player or team’s turnover. Free Throw % is the
percentage of free throw attempts that a player or team has made.

#### Defensive Stats
<div align="center">
    <img src="assets/images/nba_prediction/defensive_stats_by_team_2022.svg"
         alt="defensive stats by team in 2022" />
</div>

This dashboard visualizes the Average Blocks, Steals, Defensive Rebound %, and
Opponents Points Off Turnovers. You can view the average for each team and
filter the graph by season. Currently, we can see the averages of these four
metrics for the 2022 season. We chose these metrics for the most relevant
defensive statistics because they are most strongly correlated to a strong
defensive team in the NBA.

Blocks occur when an offensive player attempts a shot, and the defense player
tips the ball, blocking their chance to score. Steals are the number of times a
defensive player or team takes the ball from a player on offense, causing a
turnover. Defensive Rebound % is the percentage of available defensive rebounds
a player or team obtains while on the floor. Opponents Points Off Turnovers is
the number of points scored by an opposing player or team following a turnover.


#### Offensive vs. Defensive Rating
<div align="center">
    <img src="assets/images/nba_prediction/offensive_vs_defensive_rating_2022.svg"
         alt="offensive versus defensive rating by team in 2022" />
</div>

Offensive rating measures a team's points scored per 100 possessions.
Defensive rating is the number of points allowed per 100 possessions by a team.

From the offensive and defensive ratings, we can calculate the net rating, which
measures a team's point differential per 100 possessions. These ratings can help
us understand the offensive and defensive efficiency of teams compared to each
other. However, these ratings do not determine who the predicted champion will
be since there are several other statistical factors we accounted for.


## Machine Learning Model
### Logistic Regression
#### Prediction
The goal of predicting an NBA champion can be formulated as a binary
classification problem. Here the two classes are champion and non-champion.
Using historical NBA data we know both classes exactly for all past seasons and
thus using a supervised learning model is a fitting approach for our problem.
Additionally, because it is a binary classification problem, we deemed logistic
regression as the appropriate model for the job. We began by filtering out the
non-playoff teams and selecting the range of seasons identified in previous
sections as representative of the style of the modern game (2016 - 2021). After
a few transformations, all three stats tables (traditional, advanced, and
miscellaneous) were merged together into one table containing our complete set
of stats ready for exploratory analysis. To begin exploring the data, we chose
to investigate the relationships between the stats to see the degree of linear
dependence in our dataset. The chart below shows a Pearson correlation
coefficient heatmap for our dataset.

<div align="center">
    <img src="assets/images/nba_prediction/correlation_heatmap_all_stats.svg"
         alt="correlation heatmap of all stats" />
</div>

The heat map reveals several variables that have strong dependence on one or
more of the other variables. As an example, looking at the horizontal rows for
effective field goal percentage (EFG%) and true shooting percentage (TS%), the
correlation coefficient between them is high and thus their entire rows look
very similar. It is important to exclude one of these stats as they carry the
same information as indicated by their strong correlation. Below are two charts
that take a closer look at maximum and 80th percentile values of correlation
coefficient.

<div align="center">
    <img src="assets/images/nba_prediction/correlation_max.svg"
         alt="stats with max correlation coefficients less than 0.8" />
</div>

These are the stats with maximum correlations under 0.8. This was used as a
first attempt at identifying stat types that are more independent, carrying
unique information. It is observed that there are only 16 out of 45 (35%) of
stats that have maximum correlations under 0.8. A correlation of 0.8 is still
strong and thus not ideal. It was important to explore this further to see if
the entire row of correlations for a given stat were also high (we needed a
sense of the distribution of correlations per stat). Thus we have the following
chart.

<div align="center">
    <img src="assets/images/nba_prediction/correlation_80_percentile.svg"
         alt="stats with 80% of correlation coefficients less than 0.35" />
</div>

Here, we're looking at the 80th percentile correlation value for each stat that
is filtered to leave only the stats where 80% of their correlations were below
0.35. This gives us a sense per stat of how independent it is from other stats
on average. Starting with the important stats revealed by the previous sections,
we can now add in stats that on average are independent and thus provide unique
information to the model. The following chart shows the heatmap for the final
selection of features based on an iterative process of running the machine
learning model, viewing the feature importance, and deciding to add or subtract
stats from the feature set.

<div align="center">
    <img src="assets/images/nba_prediction/correlation_heatmap_final_stats.svg"
         alt="correlation heatmap of final chosen stats" />
</div>

Principal Component Analysis was also completed using the full set of stats to
investigate the amount of components needed to explain most of the variance in
the data. This helped us in identifying the number of components to shoot for by
the end of the feature engineering iterative process.

<div align="center">
    <img src="assets/images/nba_prediction/cumulative_explained_variance.svg"
         alt="cumulative explained variance" />
</div>


## Results
After running the model and predicting the test dataset, the following confusion
matrix shows the performance of our model.

<div align="center">
    <img src="assets/images/nba_prediction/confusion_matrix_final.svg"
         alt="confusion matrix" />
</div>

We can see that we predicted champions correctly at a rate of 50%. This is less
than ideal and may be due to a lack of data when limiting the input data to the
year 2016, and only reaching a total 7 features used. Moving on to the goal of
the project, our model predicted the Memphis Grizzlies as having the highest
probability of winning the championship in 2022. See below the resulting
probabilities for all playoff teams.

<div align="center">
    <img src="assets/images/nba_prediction/prediction_probabilities.svg"
         alt="prediction probabilities" />
</div>


## Feature Importance
### Stats
It was important in developing an iterative process to refine our model to have
some sense of the most important features at the end of each run. Feature
importance helped us achieve this. We used the coefficients from the logistic
regression model as our measure and we created a relative scale based on the
stat with the largest coefficient (the most important stat). Below is the visual
showcasing the results for our final iteration using the final feature set.

<div align="center">
    <img src="assets/images/nba_prediction/relative_feature_importance_bar_chart.svg"
         alt="relative feature importance bar chart" />
</div>

<div align="center">
    <img src="assets/images/nba_prediction/relative_feature_importance.svg"
         alt="relative feature importance" />
</div>

We can see here that assist to turnover ratio is the most important to
predicting our champions. Other stats that proved to be strong indicators of
champion likely teams were defensive and offensive rating as well as blocks and
steals.


## Final Predictions
<div align="center">
    <img src="assets/images/nba_prediction/champion_banner.svg"
         alt="champion background banner" />
</div>


### Memphis Grizzlies
<div align="center">
    <img src="assets/images/nba_prediction/our_champion.svg"
         alt="Memphis Grizzlies champion stats" />
</div>

Our machine learning model predicted that the Memphis Grizzlies will be the 2022
NBA Finals Champions. After we ran our machine learning model, we wanted to see
the highest weighted relative importance of each of the stats that were
accounted for in predicting the 2022 champion. The top four features were Assist
to Turnover Ratio (100), Defensive Rating (86.02), Offensive Rating (50.12), and
Blocks (45.9). In the graph above, you can see the seasonal trends over the last
few decades for these four features. If we look at the other dashboards in the
story, we can see how the Grizzlies compare to other playoff teams in each of
the four features.
