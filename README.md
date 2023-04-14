# NBA Shot Location Data - 2016-2023

NBA shot data from the 03-04 season to 22-23 w/ data viz example code. 

As I know pulling data from sites can be a headache at times, I've pulled all NBA regular season shots from 2004-2023 seasons into a single csv file. I've also included a signle csv file for each individual season in case you were looking to study only specific seasons. Compared to the play type dataset, this is data more raw and will invovle more wrangling. But! I've attached an R script that shows how to create the two shot charts at the end of the page! Hoping it can help inspire some cool projects!


--- Data Source

NBA.com

--- Link to Data 

Here is the link to the google drive folder: https://drive.google.com/file/d/1AAxMWC_SSk6lCWPmnWUmbl8MA4pzVbX1/view?usp=sharing


--- Data Dictionary

- Self-Explanatory
  - TEAM_NAME, PLAYER_NAME, POSITION_GROUP, POSITION, HOME_TEAM, AWAY_TEAM, 
- SEASON_1 & SEASON_2: Season indicator variables

- TEAM_ID: Frequency of play type used by that player, in that play type, in that year. (%)
- PLAYER_ID: NBA's unique ID variable of that specific player in their API.
- GAME_DATE: Date of the game (M-D-Y // Month-Date-Year).
- GAME_ID: NBA's unique ID variable of that specific game in their API.
- EVENT_TYPE: Character variable denoting a shot outcome (Made Shot // Missed Shot).
- SHOT_MADE: True/False variable denoting a shot outcome (True // False).
- ACTION_TYPE: Description of shot type (layup, dunk, jump shot, etc.).
- SHOT_TYPE: Type of shot (2PT or 3PT).
- BASIC_ZONE: Name of the court zone the shot took place in.
  - Restricted Area, In the Paint (non-RA), Midrange, Left Corner 3, Right Corner 3, Above the Break, Backcourt.
- ZONE_NAME: Name of the side of court the shot took place in.
  -  left, left side center, center, right side center, right
- ZONE_ABB: Abbreviation of the side of court.
  -  (L), (LC), (C), (RC), (R).
- ZONE_RANGE: Distance range of shot by zones.
  - Less than 8 ft., 8-16 ft. 16-24 ft. 24+ ft.
- LOC_X: X coordinate of the shot in the x, y plane of the court (0, 50).
- LOC_Y: Y coordinate of the shot in the x, y plane of the court (0, 50).
- SHOT_DISTANCE: Distance of the shot with respect to the center of the hoop, in feet.
- QUARTER: Quarter of the game.
- MINS_LEFT: Minutes remaining in the quarter.
- SECS_LEFT: Seconds remaining in minute of the quarter.


--- Snapshot of Data 

![Image 4-13-23 at 8 34 PM](https://user-images.githubusercontent.com/70119566/231919080-015186ad-daa7-446c-8db3-ac11fecc8484.JPG)


--- Example of Potential Data Viz

![PHI](https://user-images.githubusercontent.com/70119566/231919269-73ba4b19-03c3-4830-ba05-c28d390c47aa.jpg)

