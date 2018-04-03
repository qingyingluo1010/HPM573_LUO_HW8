import Parameters as P
import CalibrationClasses as Cls
import SupportCalibrated as Support

# create a calibrated model for fair game
calibratedModelFair = Cls.CalibratedModel('..\Labs_Calibration\CalibrationResults.csv')
# simulate the calibrated model
calibratedModelFair.simulation(P.N_Games, 20, P.N_Games_In_A_Set)

# create a calibrated model for unfair game
calibratedModelUnfair = Cls.CalibratedModel('..\Labs_Calibration\CalibrationResults.csv', P.Unfair_Prob_Head)
# simulate the calibrated model
calibratedModelUnfair.simulation(
    P.N_Games_In_A_Set, P.N_Games, 20, range(2000, 2000+P.N_Games_In_A_Set))

# report mean and projection interval of expected survival time
Support.print_outcomes(calibratedModelFair, 'When Game is Fair:')
Support.print_outcomes(calibratedModelUnfair, 'When Game is Fair (probability of head if 45%):')

# print comparative outcomes
Support.print_comparative_outcomes(calibratedModelFair, calibratedModelUnfair)