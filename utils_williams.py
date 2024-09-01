''' FINAL EXAMPLE

Module: Professional Baseball Analytics
This module provides a simple, reusable foundation for my analytics projects.
'''
import statistics

has_baseball_players: bool = True
years_in_operation: int = 148
main_hitting_caregories: list = ["Batting Average, "Hits", "On-base Percentage"]
individual_runs_scored: list = [78, 67, 98, 104, 92]

# Calculate basic stats using built-in functions min(), max() and statistics module functions mean() and stdev().
min_score: float = min(individual_runs_scored)
max_score: float = max(individual_runs_scored)
mean_score: float = statistics.mean(individual_runs_scored)
stdev_score: float = statistics.stdev(individual_runs_scored)

byline: str = f""
-----------------------------------------------------------------------
Professional Baseball Analytics: Delivering Professional Insights
-----------------------------------------------------------------------
Has Baseball Players: {has_baseball_players}
Years in Operation: {years_in_operation}
Main Hitting Categories: {main_hitting_categories}
Individual Runs Scored: {individual_runs_scored}
Minimum Individual Runs Scored: {min_score}
Maximum Individual Runs Scored: {max_score}
Standard Deviation of Individual Runs Scored: {stdev_score: .2f}
"""

def get_byline() -> str:
   '''Return a byline for my analytics projects.'''
   return byline

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

if__name__ == '__main__':
   main()
