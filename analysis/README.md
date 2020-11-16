


**Analysis**

**Introduction**
*Our analysis of the project will be included here.*
In our analyses, we set out to observes the numerous variables in a chess match and the effects they had on the outcome of the game. Our dataset is composed of 20,000 matches played on lichess.com, an online competitive chess website where people around the world play against each other. 

**The data analysed** 

**1a. Are strategies involving a lower number of opening plies more likely to be used**

In chess a ply is one move by one player in a turn; thus, there are two plies in a turn. We expect that strategies involving fewer moves will more likely result in fewer plies. When we take the mean of the number of plies from all the strategies employed as shown above, the average number of plies the opening strategies involve is roughly 3 plies implying that such strategies are more likely to be used. 

When we take the count of most popular strategies (and in so doing, removing any specifics regarding the variation of the move or whether it was accepted or rejected), we find that the top 3 opening moves (Sicilian Defense, French Defense, and Queen's Pawn Game) each involve no more than 5 plies. In forth position is the Italian defense which, depending on the variation employed, involves between 6-8 plies. Given the fact that a disproportionate number of the matches were rated (in other words, played competitively) may have resulted in the Italian Defense being more highly ranked (since more players would be aware of it), it is safe to assume that lower ply strategies are indeed more popular. 

**1. Do ratings influence opening moves and outcomes?**

We started off by finding out what are the most common opening plies. In our findings, we noticed that some of the more popular opening plies were irregular, for example, the Hungarian Opening (A00) proved to be one of the more popular opening moves as opposed to the more well known Sicilian and French Defenses. Even opening plies more popular with beginners, such as the Ruy Lopez (C60) were not as popular, suggesting that a lot of the players on Lichess are very experienced. 

On the subject of player experience, we wanted to analyse how game and player ratings influenced chess matches. First, we comprared * matches were rated or unrated* to see whether there was a difference in the preference of opening moves. Indeed, although irregular openinig plies such as the Hungarian Opening remained popular in both classes, the more beginner-friendly openings such as the Ruy Lopez among players in unrated matches.

From there, we analysed whether higher player ratings correlated with higher wins. In the above graph, we took the differences in absolute ratings of each side (where a positive absolute values denote matches where White has the higher rating and negative absolute values denote matches where black has the higher rating) to determine whether this was the case. As expected, players with higher ratings due to win more often than those with lower ratings. 

If one is playing a game against a player with a noticeably higher/lower rating, might one employ a different opening move than they would have done otherwise? If one knew one was playing with someone of a higher rating, it might be possible that they may choose to employ a different opening move in an effort to improve their likelihood of winning. To see whether this was the case, we also looked to see whether certain moves were more popular with matches where there was a greater disparity in player rating. Indeed, we did notice that certain moves, namely the Bishop's opening and Queen's Gambit were more popular in these matches; however, the beginner-friendly openings such as Ruy Lopez also continued to remain popular, suggesting that a number of lower-rated players stuck with the strategies they know best. 

**2. Does one's colour alter one's strategy?**

   In chess, the player playing white goes first, meaning they get to choose what opening move they wish to employ. Their opening strategy can often be changed based on how the player playing black responds to their opening. Thus, black's response has a great influence on the opening strategy is ultimately employed. 

   Because of this, we decided to see whether the colour one played as may have influenced the choice of opening ply. To do this, we broke down the victories by colour to analyse whether there were any differences. 
   
   In short, certain opening moves do appear to be more preferred depending on the colour one chooses. Moves such as the Van't Krujis Opening (A00) translated to far more wins for black than for white while other strategies, such as the semi-open Scandinavian Defense: Mieces-Kotroc Variatoin (B01), often worked in white's favour. More broadly, it is observed that open games (where both players start by moving the King's pawn two spaces forward) more often result in victories for white while semi-open matches (where white moves king's pawn two spaces forward while black responds with a different move) tend to end in black's favour. 

**Conclusions**

In summary, our analyses show that: 

1. Strategies with fewer plies are more commonly used
2. Players with higher ratings are more likely to win
3. Differences in ratings can influence what opening moves are likely to be employed. 
3. The colour one plays as is likely to influence the opening strategy one employs