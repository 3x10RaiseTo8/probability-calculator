import prob_calculator

prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

hat = prob_calculator.Hat(blue=3, red=2, green=6)
probability = prob_calculator.experiment(hat=hat, expected_balls={
                                         "blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
print("Probability:", probability)

hat = prob_calculator.Hat(yellow=5, red=1, green=3, blue=9, test=1)
probability = prob_calculator.experiment(hat=hat, expected_balls={
                                         "yellow": 2, "blue": 3, "test": 1}, num_balls_drawn=6, num_experiments=100)
print("Probability:", probability)
