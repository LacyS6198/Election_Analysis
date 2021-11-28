# Overview of Election Audit
The primary purpose of this analysis is to understand the election results both in terms of the candidates as well as the counties. The analysis includes 
 - The total vote count across all candidates and counties
 - Voting results for each candidate
 - Voting results for each county
 - Winning candidate results
 - County with the highest voter turnout

Voting results were measured based on each candidate's or county's total votes, as well as the perecentage of votes received out of total votes cast.


# Election-Audit Results

Overall, there were 369,711 votes cast during the election.

## County Election Results
Each county's total votes were calculated. Based on the results, the county with the highest turnout, based on number of votes, was Denver.

#### Votes by County:
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)
- County with highest number of votes:  Denver

## Candidate Election Results
Each candidate's total votes were calculated. Based on the results, the winner of the election was Diana DeGette.

#### Votes by Candidate
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)

#### Winning Candidate
- Winner: Diana DeGette
- Winning Vote Count: 272,892
- Winning Percentage: 73.8%

The full election results are also available here:
[election_analysis.txt](https://github.com/LacyS6198/Election_Analysis/files/7613607/election_analysis.txt)


# Election-Audit Summary
The script written for this analysis was created specifically to count the votes per county and votes per candidate. With a few modifications, this code can be applied to other election analyses. 

## Additional Usage #1 
Using the same election data, this analysis could be modified to breakdown each candidate's votes by county. We could also breakdown each county's votes by candidate. The election results data is present and could support this analysis. The current code creates lists and dictionaries based on the county and candidate separately. See code snippet below. If this code was modified to use multiindex series (hierarchical indexing) then this type of analysis could be performed. 

```
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
counties_list = []
counties_votes = {}
```

## Additional Usage #2
The code cana also be used for different election types including county- or city-level elections, such as a mayoral election. If the data was in the same format/structure as it currently is within the "election_results.csv" with columns of ballot/vote information, geographic location, and candidate name. If a new CSV file was supplied with the same data structure, the code would only need modified to describe the new geographic region type. 

For example, if the election_results.csv file was provided with city information in index 1 instead of county, a few changes could quickly be made to support the use of city in the file. The suggested changes are listed below. 

### Required Modifications
The below modifications to the code would be requried to be changed for a city mayoral election analysis. If the data structure of the CSV file was the exact same then to support a city analysis would not require changes to the code since the index of the city data would be the same. The only change required would be to the output text.

- Line 89: Change to reference "City" instead of "County"
- Line 119: Change to reference "City" instead of "County"

![line89](https://user-images.githubusercontent.com/93630042/143771563-e85ca78f-fe09-4219-a721-f0066ff13154.png)

![line119](https://user-images.githubusercontent.com/93630042/143771567-88e1007d-8354-4c08-9cac-324fc64f853b.png)

### Suggested Modifications
The below modifications to the code are highly suggested if modifying for a city mayoral election analysis. Modifying these portions of code would chagne the code references from "county" to "city", making the code easier to understand. 

- Lines 21 - 22: Change to reference "City" instead of county
- Lines 30 - 32: Change to reference "City" instead of county
