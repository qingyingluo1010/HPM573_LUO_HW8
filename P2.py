#P2: Comparing Transient State

import Parameters as P
import GameClasses as Cls
import SupportTransientState as Support

# create multiple cohorts for when the drug is not available
cohortFair = Cls.MultipleGameSets(
    ids=range(P.N_Games_In_A_Set),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    prob_head= P.Prob_Head ,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    n_games_in_a_set=P.N_Games_In_A_Set  # [p, p, ...]
)
# simulate all cohorts
cohortFair.simulation()

# create multiple cohorts for when the drug is available
cohortUnfair = Cls.MultipleGameSets(
    ids=range(P.N_Games_In_A_Set, 2*P.N_Games_In_A_Set),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    prob_head=P.Unfair_Prob_Head,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    n_games_in_a_set=P.N_Games_In_A_Set
)
# simulate all cohorts
cohortUnfair.simulation()

# print outcomes of each cohort
Support.print_outcomes(cohortFair, 'When Game is Fair:')
Support.print_outcomes(cohortUnfair, 'When Game is Fair (probability of head if 45%):')

# print comparative outcomes
Support.print_comparative_outcomes(cohortFair, cohortUnfair)