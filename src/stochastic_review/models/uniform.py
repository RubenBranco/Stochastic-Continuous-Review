from scipy.stats import uniform

from .common import iterative_function_optimizer, quality_of_service


def _r_func(q_star, w, cfg, delta):

    return uniform.ppf(
        1 - (q_star / w),
        cfg['mean'],
        cfg['std_deviation'] - cfg['mean'],
    )


def _phi_func(r_star, cfg, q_star=None, w=None):
    return cfg['std_deviation'] / 2 - r_star + (r_star ** 2 / (2 * cfg['std_deviation']))


def uniform_continuous_review(cfg, logger):
    delta = uniform.median(cfg['mean'], cfg['std_deviation'] - cfg['mean'])
    mu = cfg['order_cost'] * delta
    logger.info(f"Calculated delta: {delta}")
    logger.debug("Beginning iterative optimization")
    k_star, q_star, r_star, w = iterative_function_optimizer(
        _r_func,
        _phi_func,
        mu,
        delta,
        cfg,
        logger,
    )
    qos = quality_of_service(q_star, r_star, w, delta)
    return k_star, q_star, r_star, qos
