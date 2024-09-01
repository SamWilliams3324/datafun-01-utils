''' ITERATION 3

Module: Professional Baseball Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

Process:
In this third iteration, I declare additional variables to show skills with different data types.

#####################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
#####################################

# Boolean variable to indicate if the company has baseball players
has_baseball_players: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 148

# List of strings representing the main hitting categories
main_hitting_caregories: list = ["Batting Average, "Hits", "On-base Percentage"]

# List of floats representing individual runs scored
individual_runs_scored: list = [78, 67, 98, 104, 92]

#####################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
#####################################

byline: str = f""
-----------------------------------------------------------------------
Professional Baseball Analytics: Delivering Professional Insights
-----------------------------------------------------------------------
Has Baseball Players: {has_baseball_players}
Years in Operation: {years_in_operation}
Main Hitting Categories: {main_hitting_categories}
Individual Runs Scored: {individual_runs_scored}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
   '''Return a byline for my analytics projects.'''
   return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

######################################
# Conditional Execution 
######################################

if_name_ == '_main_':
   main()
