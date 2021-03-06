


**Analysis**

   <img src="../images/Chess_Board.png" width="300px">

**Introduction**
*Our analysis of the project will be included here.*
In our analyses, we set out to observe the effect numerous chess variables have on the outcome of the game. Our dataset is comprised of 20,000 matches played on lichess.com, an online competitive chess website where people around the world play against each other in rated or unrated matches. 

**The data analysed** 

   
<img src="../images/Histogram of Opening Plys.png" width="300px"> (figure 1)

**1. Are strategies involving a lower number of opening plies more likely to be used?**

    
In chess a ply is one move by one player in a turn; thus, two plies make a turn. We expect that strategies involving fewer moves will more likely result in fewer plies. When we take the mean of the number of plies from all the strategies employed as shown above (figure 1), the average number of plies the opening strategies involve is roughly 3 plies, implying that such strategies are more likely to be used. 

   <img src="../images/Total Count of Different Openings.png" width="300px"> (figure 2)
 
When we take the count of the most popular strategies (while removing any specifics regarding the variation of the move or whether it was accepted or rejected), we find that the top 3 opening moves (Sicilian Defense, French Defense, and Queen's Pawn Game) each involve no more than 5 plies. In forth position is the Italian defense which, depending on the variation employed, involves between 6-8 plies. Given the fact that a disproportionate number of the matches in our sample were rated (in other words, played competitively), this may have resulted in the Italian Defense being more highly ranked (since experienced players would be aware of it) Therefore, it is safe to assume that lower ply strategies are indeed more popular. 

**2. Do ratings influence opening moves and outcomes?**

   <img src="../images/popular_rated_openings.png" width="300px"> (figure 3)
    
To answer this questions, we started off by finding out what are the most common opening plies. In our findings, we noticed that some of the more popular opening plies were irregular, for example, the Hungarian Opening (A00) proved to be one of the more popular opening moves as opposed to the more well known Sicilian and French Defenses. Even opening plies more popular with beginners, such as the Ruy Lopez (C60) were not as popular, suggesting that a lot of the players on Lichess are very experienced (figure 3). 

As for player experience, we wanted to analyse how game and player ratings influenced chess matches. First, we compared *matches that were rated or unrated* to see whether there was a difference in the preference of opening moves. As figure 3 shows, although irregular openinig plies such as the Hungarian Opening remained popular in both classes, the more beginner-friendly openings such as the Ruy Lopez is more popular among among players in unrated matches.

   <img src="../images/Absolute Ratings vs Match Outcomes.png" width="300px"> (figure 4)

From there, we analysed whether higher player ratings correlated with higher wins. In the above graph (figure 4), we took the differences in absolute ratings of each side (where positive absolute values denote matches where White has the higher rating and negative absolute values denote matches where Black has the higher rating) to determine whether this was the case. As expected, players with higher ratings tend to win more often. 

<img src="../images/rating_disparity.png" width="300px"> (figure 5)

If one is playing a game against a player with a noticeably higher/lower rating, might one employ a different opening move than they would have done otherwise? In the scenario that one is playing with a more highly ranked player, they might possibly choose to employ a different opening move in an effort to improve their likelihood of winning. To see whether this was the case, we also looked to see whether certain moves were more popular with matches where there was a greater disparity in player rating. Indeed, we did notice that certain moves, namely the Bishop's opening and Queen's Gambit were more popular in these matches; however, the beginner-friendly openings such as Ruy Lopez also continued to remain popular, suggesting that a number of lower-rated players stuck with the strategies they know best. 

**3. Does one's colour alter one's strategy?**

   In chess, the player playing white goes first, meaning they get to choose what opening move they wish to employ. Their opening strategy can often be changed based on how the player playing black responds to their opening. Thus, black's response has a great influence on the opening strategy is ultimately employed. 

   Because of this, we decided to see whether the colour one played as may have influenced the choice of opening ply. To do this, we broke down the victories by colour to analyse whether there were any differences. 
   
   <img src="../images/preferred_openings_by_colour.png" width="400px"> (figure 6)
    
    
   <img src="../images/wins_per_opening_per_colour.png" width="400px"> (figure 7)
 
   In short, certain opening moves do appear to be more preferred depending on the colour one chooses. As the above figures show, moves such as the Van't Krujis Opening (A00) translated to far more wins for black than for white while other strategies, such as the semi-open Scandinavian Defense: Mieces-Kotroc Variatoin (B01), often worked in white's favour. More broadly, it is observed that open games (where both players start by moving the King's pawn two spaces forward) more often result in victories for white while semi-open matches (where white moves king's pawn two spaces forward while black responds with a different move) tend to end in black's favour.
   
**4. Does time influence the choice of opening ply?**

   <img src="../images/time_and_ply_2.png" width="300px"> (figure 8) <img src="../images/match_times.png" width="300px"> (figure 9)
   
Given the variation in chess match times, it may be possible that there might be a positive correlation between amount of time and ply moves. After all, if one has more time, why not try a more complex opening move? However, as figure 8 shows, no such correlation appears to be present. Granted, the vast majority of matches were under 25 minutes in length, giving the data a bias towards shorter matches(figure 9). Nevertheless, it appears that other factors, such as the difference in rating, play a far greater role. 

**Conclusions**

In summary, our analyses show that: 

1. Strategies with fewer plies are more commonly used
2. Players with higher ratings are more likely to win
3. Differences in ratings can influence what opening moves are likely to be employed. 
4. The colour one plays as is likely to influence the opening strategy one employs
5. Time plays little role in the choice of ply