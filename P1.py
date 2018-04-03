#P1. Comparing Steady State

import Parameters as P
import GameClasses as Cls
import SupportSteadyState as Support

# create a cohort of patients for when the drug is not available
cohortFair = Cls.SetOfGames(
    id=1,
    prob_head=P.Prob_Head,
    n_games=P.N_Games)
# simulate the cohort
FairOutcome = cohortFair.simulation()

# create a cohort of patients for when the drug is available
cohortUnfair = Cls.SetOfGames(
    id=2,
    prob_head=P.Unfair_Prob_Head,
    n_games=P.N_Games)
# simulate the cohort
UnfairOutcome = cohortUnfair.simulation()

# print outcomes of each cohort
Support.print_outcomes(FairOutcome, 'When Game is Fair:')
Support.print_outcomes(UnfairOutcome, 'When Game is Fair (probability of head if 45%):')

# print comparative outcomes
Support.print_comparative_outcomes(FairOutcome, UnfairOutcome)


