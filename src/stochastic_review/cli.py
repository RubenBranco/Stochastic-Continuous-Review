from bullet import SlidePrompt, Bullet


DISTRIBUTIONS = [
    'Uniform',
]


cli = SlidePrompt(
    [
        Bullet(prompt="Choose the distribution", choices=DISTRIBUTIONS),
    ]
)

result = cli.launch()
print(result)