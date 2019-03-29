import math


def k_func(q, r, mu, delta, phi_func, cfg):
    return (cfg['order_cost'] * delta) / q + cfg['unit_cost'] * delta + \
        cfg['storage_cost'] * (q / 2 + r - cfg['mean']) + \
        ((cfg['out_of_stock'] * delta) / q) * phi_func(r, cfg)


def q_func(q0, w, phi):
    return math.sqrt(q0 ** 2 + 2 * w * phi)


def _stop_criteria(q_last, q_star, r_last, r_star, phi_func, mu, delta, cfg):
    return r_last is None or q_last is None or \
        abs(k_func(q_star, r_star, mu, delta, phi_func, cfg) - \
            k_func(q_last, r_star, mu, delta, phi_func, cfg)) \
             > cfg['stop_crit']


def quality_of_service(q_star, r_star, w, delta):
    return (1 - q_star / w) ** (delta / q_star)


def iterative_function_optimizer(r_func, phi_func, mu, delta, cfg, logger):
    w = (cfg['out_of_stock'] / cfg['storage_cost']) * delta
    q0 = math.sqrt((2 * cfg['order_cost'] * delta) / cfg['storage_cost'])

    q_last = None
    q_star = q0
    logger.debug(f"Calculated Q0: {q0}")

    r_last = None
    r_star = r_func(q_star, w, cfg, delta)
    logger.debug(f"Starting r*: {r_star}")

    i = 1
    while _stop_criteria(q_last, q_star, r_last, r_star, phi_func, mu, delta, cfg):
        logger.debug(f"Starting iteration number {i}")
        phi = phi_func(r_star, cfg)
        logger.debug(f"New phi value: {phi}")

        q_last = q_star
        q_star = q_func(q0, w, phi)
        logger.debug(f"New Q* value: {q_star}")

        r_last = r_star
        r_star = r_func(q_star, w, cfg, delta)
        logger.debug(f"New r* value: {r_star}")

        i += 1

    k_star = k_func(q_star, r_star, mu, delta, phi_func, cfg)
    logger.debug(
        f"Ended the optimization after {i} iterations with values: Q={q_star}, r={r_star}, K={k_star}"
    )
    return k_star, q_star, r_star, w

