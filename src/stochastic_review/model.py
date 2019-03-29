from .models.uniform import uniform_continuous_review
from .models.normal import normal_continuous_review


def continuous_review(cfg, logger):
    return globals()[f"{cfg['distribution'].lower()}_continuous_review"](cfg, logger)
