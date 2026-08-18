def mean(values):
    return sum(values) / len(values)


def sse(x_data, y_data, m, b):

    total_errors = 0
    for i in range(len(x_data)):
        prediction = predict(x_data[i], m, b)
        error = y_data[i] - prediction
        total_errors += error ** 2

    return total_errors


def predict(x, m, b):
    return m * x + b


def fit_line(x_data, y_data):

    x_mean = mean(x_data)
    y_mean = mean(y_data)

    numerator = 0
    denominator = 0

    for i in range(len(x_data)):
        x_diff = x_data[i] - x_mean
        y_diff = y_data[i] - y_mean
        numerator += x_diff * y_diff
        denominator += x_diff * x_diff

    m = numerator / denominator
    b = y_mean - m * x_mean
    return m, b


def gradient_disc(x_data, y_data, learning_rate=0.01, epochs=1000):

    m = 0
    b = 0
    n = len(x_data)

    for _ in range(epochs):
        gradient_m = 0
        gradient_b = 0

        for i in range(n):
            prediction = predict(x_data[i], m, b)
            error = y_data[i] - prediction
            gradient_m +=  -2 * x_data[i] * error
            gradient_b += -2 * error

    return m, b


def main():

    x_data = [1, 2, 3, 4, 5]
    y_data = [2, 4, 5, 4, 5]

    m, b = fit_line(x_data, y_data)
    error = sse(x_data, y_data, m, b)

    print(f"Fitted line: y = {m:.4f}x + {b:.4f}")
    print(f"Sum of Squared Errors: {error:.4f}")

    # Try a prediction
    test_x = 6
    print(f"Prediction for x={test_x}: y={predict(test_x, m, b):.4f}")

    # Stretch goal: compare against gradient descent
    print("\n--- Gradient Descent (stretch goal) ---")
    gd_m, gd_b = gradient_disc(x_data, y_data, learning_rate=0.01, epochs=1000)
    gd_error = sse(x_data, y_data, gd_m, gd_b)
    print(f"Fitted line: y = {gd_m:.4f}x + {gd_b:.4f}")
    print(f"Sum of Squared Errors: {gd_error:.4f}")
    print(f"Closed-form m,b:  {m:.4f}, {b:.4f}")
    print(f"Grad. desc. m,b:  {gd_m:.4f}, {gd_b:.4f}")


if __name__ == "__main__":
    main()

