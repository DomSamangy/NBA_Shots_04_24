# NBA Shot Location Data - 2016-2023

NBA regular season shot data from the 2003-04 season to 2022-23.

As I know pulling data from sites can be a headache at times, I've pulled all NBA regular season shots from 2004-2023 seasons into a single csv file. I've also included a signle csv file for each individual season in case you were looking to study only specific seasons. Compared to the play type dataset, this is data more raw and will invovle more wrangling. But! I've attached an R script that shows how to create the two shot charts at the end of the page! Hoping it can help inspire some cool projects!


--- Data Source

NBA.com

--- Link to Data 

Here is the link to the google drive folder: https://drive.google.com/file/d/1AAxMWC_SSk6lCWPmnWUmbl8MA4pzVbX1/view?usp=sharing


--- Data Dictionary

- POSS: Number of possessions used by that player, in that play type, in that year.
- FREQ: Frequency of play type used by that player, in that play type, in that year. (%)
  - FREQ_PCTL: Percentile rank of play type frequency.
  - Scale of 0 to 100 --- (0 relates to worst while 100 relates to best)
- PPP: Points per possessions of that player, in that play type, in that year. (%)
  - PPP_PCTL: Percentile rank of PPP variable. 
  - Scale of 0 to 100 --- (0 relates to worst while 100 relates to best)
- GP: Games Played
- PTS: Points
- FG: Field goals made
- FGA: Field goals attempted
- FG_PCT: Field goal percentage (%)
- EFG_PCT: Effective field goal percentage (%)
- SF_FREQ: Frequency of shooting fouls drawn (%)
- FTA_FREQ: Frequency of free throws attempted (%)
- AND1_FREQ: Frequency of and one plays made (%)
- TOV_FREQ: Frequenyc of turnovers committed (%)



--- Snapshot of Data 

![Image 4-13-23 at 8 34 PM](https://user-images.githubusercontent.com/70119566/231919080-015186ad-daa7-446c-8db3-ac11fecc8484.JPG)


--- Example of Potential Data Viz

![PHI](https://user-images.githubusercontent.com/70119566/231919269-73ba4b19-03c3-4830-ba05-c28d390c47aa.jpg)


- FREQ: Frequency of play type used by that player, in that play type, in that year. (%)
