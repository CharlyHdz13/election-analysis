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
  
  To now count the total amount of votes, I used a `for` loop using the "reader" as the collection. Inside the `for` I added 1 to the previous value of `total_votes` as follows:
  
  ![image](https://user-images.githubusercontent.com/89402038/135728755-ef037067-9f8a-4ec1-a8af-3204ea731d59.png)
  
  After the `for` loop ends we will get the exact amount of votes of the election which were: 369,711.

- Breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  
  How the algorithm works to obtain this data from the csv file is as follows. First of an empty list and an empty dictionary were initialized before the `with` statement where I read the file.
  
  ![image](https://user-images.githubusercontent.com/89402038/135734135-a25a8432-8844-4ed9-9bcf-83e5f7e3dc5f.png)
  
  The list "counties" will save the names for every county in the file and the dictionary "county_votes" will have as keys the names of the counties and as values the number of votes casted in that county. To do this a variable named county_name was declared inside the `for` loop inside the `with` statement and was asigned the value of the second position of the list "row".
  
  ![image](https://user-images.githubusercontent.com/89402038/135734200-05b3331d-2b1b-4d86-a832-c0c6c7323bd6.png)
  
  After that an `if` statement is used to determine if the variable "county_name" is already in the list "counties", using the `not in` conditional. If the county is not in the list then it will be appended onto the list and also it will start tracking the number of votes in the dictionary. If the county is already in the list then it will only be added one vote onto the value in the dictionary tracking the number of votes casted in that county.
  
  ![image](https://user-images.githubusercontent.com/89402038/135734323-a3a88d5d-cced-4cd3-b053-964151444c61.png)
  
  I now print or write the values obtained through the algorithm and obtain the following:
  
  ![image](https://user-images.githubusercontent.com/89402038/135734357-fb7afcd9-d25b-4d3f-b72c-5a459872e15a.png)
  
- Which county had the largest number of votes?
  
  At first glance it is very easy to see from the previous image which county had the biggest turnout, but what if this was not the case and we had very tight numbers between counties or had lots of counties? Then the following is an efficient way to solve that problem. First two variables were declared: one empty string "county_largest_turnout" and an integer, "county_largest_turnout_votes", with its default value as zero. 
  
  ![image](https://user-images.githubusercontent.com/89402038/135734770-822eb256-644c-48ef-a2ba-3e928057d889.png)
  
  Now using a `for` loop I iterate through the dictionary "county_votes" where the number of votes are stored for each county. With an `if` statement I check if the number of votes of the actual county is greater than the variable "country_largest_turnout_votes" if true then this varible is assigned the new value.
  
  ![image](https://user-images.githubusercontent.com/89402038/135734832-8f70b43f-ab52-40b8-adbb-291f05e0f37b.png)
  
  With this we now can print easyily the following:
  
  ![image](https://user-images.githubusercontent.com/89402038/135734850-7b569bc4-3d58-4d4f-be05-c392264dd881.png)
  
- Breakdown of the number of votes and the percentage of the total votes each candidate received.
  
  This was made the same way as for the counties but focusing on the candidates instead of the counties. The results obtained where the following:
  
  ![image](https://user-images.githubusercontent.com/89402038/135734889-e5e5834c-3ae8-4e39-9486-7123acaac2a1.png)
  
- Which candidate won the election, what was their vote count, and what was their percentage of total votes?
  
  In the same style as for the county with the largest turnout, the same algorithm was used to determine the winner of the election. 
  
  ![image](https://user-images.githubusercontent.com/89402038/135734903-2e50b913-90be-4851-972d-a4e169bc3e7d.png)
  
## Election-Audit Summary
The code is able to succesfully determine the winner of an election and the amount of votes for each county. This code can be easily used for any other election, bigger or smaller. The only important changes that should be made to the code is to add more variables which save this other entities that we want to track. For example, in a bigger election we would also like to focus on the states or in a smaller election perhaps divide by districs. Another future implementation could be a GUI for the user to be able to get which ever information he wants from the data and also graph the data in bar charts or pie graphs. 

