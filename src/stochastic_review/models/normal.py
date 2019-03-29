from scipy.stats import norm

from .common import iterative_function_optimizer, quality_of_service


def _r_func(q_star, w, cfg, delta):
    return norm.ppf(1 - (q_star / w), 0, 1) * cfg['std_deviation'] + cfg['mean']


def _phi_func(r_star, cfg, q_star, w):
    fr = 1 - (q_star / w)
    u = norm.ppf(fr, 0, 1)
    return cfg['std_deviation'] * (
        norm.pdf(u, 0, 1) - u + u * fr)


def normal_continuous_review(cfg, logger):
    delta = cfg['mean'] / cfg['delivery_time']
    logger.info(f"Calculated delta: {delta}")
    logger.debug("Beginning iterative optimization")
    k_star, q_star, r_star, w = iterative_function_optimizer(
        _r_func,
        _phi_func,
        cfg['mean'],
        delta,
        cfg,
        logger,
    )
    qos = quality_of_service(q_star, r_star, w, delta)
    return k_star, q_star, r_star, qos
