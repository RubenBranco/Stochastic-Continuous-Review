from bullet import SlidePrompt, Bullet, Numbers


DISTRIBUTIONS = [
    'Uniform',
]


cli = SlidePrompt(
    [
        Bullet(prompt="Choose the distribution", choices=DISTRIBUTIONS),
        Numbers(prompt="Distribution mean(μ) / Starting point(a): ", type=float),
        Numbers(prompt="Distribution standard deviation(σ) / End point(b): ", type=float),
        Numbers(prompt="Delivery time(l): ", type=float),
        Numbers(prompt="Fixed cost of the order(A): ", type=float),
        Numbers(prompt="Unitary item cost(c): ", type=float),
        Numbers(prompt="Storage cost per item per timestep(h): ", type=float),
        Numbers(prompt="Out of stock cost per item(p'): ", type=float),
        Numbers(prompt="Stopping rate of change(ε): ", type=float),
    ]
)


def get_args_from_cli(cli_obj):
    args = cli_obj.launch()
    return dict(
        distribution=args[0][1],
        mean=args[1][1],
        std_deviation=args[2][1],
        delivery_time=args[3][1],
        order_cost=args[4][1],
        unit_cost=args[5][1],
        storage_cost=args[6][1],
        out_of_stock=args[7][1],
        stop_crit=args[8][1],
    )
