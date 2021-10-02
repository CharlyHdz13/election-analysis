# Election Analysis
## Overview of Election Audit
Counting is a very tedious task humans do not like to do. Now counting is very important in our daily tasks, but especially in democratic elections. In this type of events the probability of having a human error in the counting is not desirable, therefore through this project I coded a programm using Python which counts all of the votes that reside in a .csv file and determines the winner of the election.
## Election-Audit Results
- How many votes were cast in this congressional election?

  To answer this first question I first needed to have a quick look over the csv file named "election_results.csv" (which can be found in the "Resources" folder). The file is structured as follows:
  
  ![image](https://user-images.githubusercontent.com/89402038/135693614-0c12588b-4153-463c-8e73-11aef962ec21.png)
  
  As it is shown in the image, the data is strucutred as `[Ballot ID, County, Candidate]`, therfore to obtain the total votes of the election I counted each row in the csv file. To do this I use the modules `csv` and `os`: the first one is to read and write over files and the second one to obtain the path to the files in an undirect way. I first declared a string variable to save the path of the "election_results.csv" using the following code:
  
  `file_to_load = os.path.join("Resources", "election_results.csv")`
  
  Afterwards, I initialized the counter of the votes as a integer and assign zero as its default value. Then using the `with` statement to be able to read the file as follows:
  
  ![image](https://user-images.githubusercontent.com/89402038/135728527-e657cd5f-0cd8-464f-bea1-470c7a810b75.png)
   
  And the reader is going to be a dictionary which has inside every row from the csv file. To skip the row of the header I just used the `next` method which fetches the next item in the diccionary.
  
  ![image](https://user-images.githubusercontent.com/89402038/135728606-13714aa9-ca25-487e-8b55-aaf3a3d2a703.png)
  
  To now count the total amount of votes, I used a for loop using the "reader" as the collection. Inside the for I added 1 to the previous value of `total_votes` as follows:
  
  ![image](https://user-images.githubusercontent.com/89402038/135728755-ef037067-9f8a-4ec1-a8af-3204ea731d59.png)
  
  After the for loop ends we will get the exact amount of votes of the election which were: 369,711.

- Breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Which county had the largest number of votes?
- Breakdown of the number of votes and the percentage of the total votes each candidate received.
- Which candidate won the election, what was their vote count, and what was their percentage of total votes?
## Election-Audit Summary
