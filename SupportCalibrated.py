import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(calibrated_model, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param calibrated_model: calibrated model
    :param strategy_name: the name of the selected therapy
    """

    # print expected mean survival time
    print(strategy_name)
    print("Expected mean reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          calibrated_model.get_mean_survival_time_proj_interval(alpha=P.ALPHA, deci=1))


def print_comparative_outcomes(calibrated_model_fair, calibrated_model_unfair):
    """ prints expected and percentage increase in average survival time when drug is available
    :param calibrated_model_no_drug: calibrated model simulated when drug is not available
    :param calibrated_model_with_drug: calibrated model simulated when drug is available
    """

    # increase in survival time
    increase = Stat.DifferenceStatPaired(
        name='Increase in mean reward',
        x=calibrated_model_unfair.get_mean_total_reward(),
        y_ref=calibrated_model_fair.get_mean_total_reward()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in mean reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    # % increase in mean survival time
    relative_diff = Stat.RelativeDifferencePaired(
        name='% increase in mean reward',
        x=calibrated_model_unfair.get_mean_total_reward(),
        y_ref=calibrated_model_fair.get_mean_total_reward()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=relative_diff.get_mean(),
        interval=relative_diff.get_bootstrap_CI(alpha=P.ALPHA, num_samples=1000),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Percentage increase in mean reward and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)
