import random


class LinearRegression:

    def __init__(self, test="default", slope=None, intercept=None):
        self.test = test
        self.slope = slope
        self.intercept = intercept

    def fit(self, x, y):
        if not x or not y:
            raise ValueError("Data cannot be empty")

        n = len(x)

        # Extract x values from nested lists
        sum_x = sum(xi[0] for xi in x)
        sum_y = sum(y)
        sum_xy = sum(xi[0] * yi for xi, yi in zip(x, y))
        sum_xx = sum(xi[0] * xi[0] for xi in x)

        # Calculate the slope / denominator
        denominator = n * sum_xx - sum_x ** 2
        if denominator == 0:
            raise ValueError("Cannot compute slope: all x values are identical")

        # Calculate the numerator
        self.slope = (n * sum_xy - sum_x * sum_y) / denominator

        # Calculate intercept using correct formula
        mean_x = sum_x / n
        mean_y = sum_y / n
        self.intercept = mean_y - self.slope * mean_x


    def predict(self, x):
        if self.slope is None or self.intercept is None:
            raise RuntimeError("Cannot predict before the model is fitted. Call .fit() first.")

        return [self.slope * xi[0] + self.intercept for xi in x]


def mean(values):
    return sum(values) / len(values)



def main():
    # Makes the "random" noise the same every time you run the code
    random.seed(0)

    # Simple linear relationship y = 2.5 * x + 1 with a bit of noise
    x_raw = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_raw = [2.5 * xi + 1 + random.uniform(-0.5, 0.5) for xi in x_raw]

    # Converts the
    x = [[xi] for xi in x_raw]
    y = y_raw

    # Create model
    model = LinearRegression(test="demo")

    # Fit the model
    try:
        model.fit(x, y)
    except Exception as e:
        print(f"Fit failed: {e}")
        return

    # Calls the predict method
    new_x = [[11], [12], [13]]
    predictions = model.predict(new_x)

    print("Learned parameters:")
    print(f"  test attribute (demo):    {model.test}")
    print(f"  Learned slope:            {model.slope:.4f}")
    print(f"  Learned intercept:        {model.intercept:.4f}")
    print("\nPredictions for new_x:",   new_x)
    print("Model predictions:",         predictions)


if __name__ == "__main__":
    main()