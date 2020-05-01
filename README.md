# Blotto Tournament - Round 1
Many of us enjoy solving puzzles and playing games for our own sake. One strategic game (technically, class of games) is called Blotto. While the setup is traditionally described in terms of medieval warfare, here is a presentation more relevant to the twenty-first century!

You and another (equally qualified) candidate are running for office. There are **10 districts**, numbered 1, 2, 3, …, 10 and each is worth **1 vote**. You have **100 discrete units of resources** (e.g. time, campaign workers), which you can allocate between the districts however you wish. Your opponent independently does the same. District **N  will award its vote to a candidate if and only if that candidate spends strictly more than N times the resources as their opponent** (for N = 1, 2, 3, …, 10).

For example, here is one match:

|District|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|
|-|-|-|-|-|-|-|-|-|-|-|
|Alice|10|10|10|10|10|10|10|10|10|10|
|Carol|15|5|30|5|10|5|0|10|0|20|


In this match, Alice wins districts 7 and 9, for a total of 2 districts, and Carol wins only district 1, for a total of 1 district. (Nobody wins a vote among the remaining 7 districts.)

Let’s play a tournament. You get one entry and your final score is the average of your number of districts won playing head-to-head against each other entry among applicants.

An entry should be submitted as a list of 10 non-negative integers, adding up to 100, where the nth element is the number of units of resources being sent to district n.

```
python blotto.py -e myemail@unity3d.com -l 10 10 10 10 10 10 10 10 10 10
```
