### Introduction
- This the week 6 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Define a function called `search(keyword, filename)` that takes a keyword and the name of a file as input.
   - Open the file and iterate through the file object line by line.
   - If you find the keyword in the line, yield it.
2. Write a query to create a new table using the `customers` table that has columns `customer_id`, `first_name`, `points`, and `type`. 
   - There are three different types.
     - Customers with `points <= 2000`: Bronze
     - Customers with `2000 < points <= 3000`: Silver
     - Customers with `points > 3000`: Gold
3. Using the iris datasets from the sklearn package, try to group the observations into clusters using all the features.
   - The four columns in the iris dataset are `sepal length`, `sepal width`, `petal length`, `petal width`.
   - Using `dendrogram` to figure out the best number of clusters.
   - Return the Hierarchical Cluster model re-fitted with the optimal number of clusters.
4. Write a function that uses regex to extrat the start date and end date from the input date string.
   - Return the start date and end date at the end of the function.
   - `extract_dates('05/22/2023 - 08/23/2023')` => `'05/22/2023', '08/23/2023'`
5. Implement the `double_bettor_v2(initial_funds, initial_wager, intended_rounds)` function so that:
   - The bettor cannot wager more than the bettor has.
   - The maximum wager should be the remaining wealth
   - Return the path of the player fund.
6. Implement the `double_bettor_v2(initial_funds, initial_wager, intended_rounds, scaler = 1)` function so that:
   - In addition to the above improvment, generalize the wager scaling.
   - Instead of doubleing the bet, paramaterize the scaler 
   - When the bettor loses, the next bet is multiplied by the scaler.
7. Implement the `double_bettor_v2(initial_funds, initial_wager, intended_rounds, scaler = 1, increment = 0)` function so that:
   - Further generalize the function by adding a bet size increment.
   - If the bettor loses, the wager multiplied by the scaler and then increases by the increment. 
   - If the bettor wins, the wager decreases by the increment. 
   - The wager does not fall below the original wager size.