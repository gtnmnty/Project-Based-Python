def mean(values):
    return sum(values) / len(values)


def sse(x_data, y_data, m, b):
    total_errors = 0
    for i in range(len(x_data)):
        # Predict the y value for the current x using the line equation
        prediction = predict(x_data[i], m, b)
        # Calculate the vertical distance (residual) between actual and predicted
        error = y_data[i] - prediction
        # Square the error to penalize large misses and avoid negative cancellation
        total_errors += error ** 2

    return total_errors


def predict(x, m, b):
    return m * x + b


def fit_line(x_data, y_data):
    x_mean = mean(x_data)
    y_mean = mean(y_data)

    numerator = 0
    denominator = 0

    # Calculate the components of the slope formula:
    # m = sum((x - x_mean)(y - y_mean)) / sum((x - x_mean)^2)
    for i in range(len(x_data)):
        x_diff = x_data[i] - x_mean
        y_diff = y_data[i] - y_mean
        numerator += x_diff * y_diff
        denominator += x_diff ** 2

    # Guard against division by zero if all x values are identical
    if denominator == 0:
        raise ValueError("Cannot fit line: All x values are identical (denominator is zero).")

    # Calculate slope (m) and y-intercept (b)
    m = numerator / denominator
    b = y_mean - m * x_mean

    return m, b


def gradient_disc(x_data, y_data, learning_rate=0.01, epochs=1000):
    # Initial guesses for slope and intercept
    m = 0
    b = 0
    n = len(x_data)

    # Loop through the entire dataset 'epochs' number of times
    for _ in range(epochs):
        # Reset gradients at the start of each epoch
        gradient_m = 0
        gradient_b = 0

        # Calculate the gradient (derivative) of the SSE function
        for i in range(n):
            prediction = predict(x_data[i], m, b)
            error = y_data[i] - prediction

            # Accumulate the partial derivatives with respect to m and b
            # Gradient for m is proportional to x * error
            gradient_m += -2 * x_data[i] * error
            # Gradient for b is proportional to the error itself
            gradient_b += -2 * error

        # Average the gradients by the number of data points
        gradient_m /= n
        gradient_b /= n

        # Update m and b by stepping in the opposite direction of the gradient
        m -= learning_rate * gradient_m
        b -= learning_rate * gradient_b

    return m, b


def main():
    # Sample dataset: x is independent variable, y is dependent
    x_data = [1, 2, 3, 4, 5]
    y_data = [2, 4, 5, 4, 5]

    # uses tuple unpacking
    m, b = fit_line(x_data, y_data)
    error = sse(x_data, y_data, m, b)

    print(f"Fitted line: y = {m:.4f}x + {b:.4f}")
    print(f"Sum of Squared Errors: {error:.4f}")

    # Test the model with a new value
    test_x = 6
    print(f"Prediction for x={test_x}: y={predict(test_x, m, b):.4f}")

    # --- Method 2: Gradient Descent (Approximation) ---
    print("\n--- Gradient Descent (stretch goal) ---")
    # Note: Learning rate and epochs must be tuned; too high and it overshoots
    gd_m, gd_b = gradient_disc(x_data, y_data, learning_rate=0.01, epochs=1000)
    gd_error = sse(x_data, y_data, gd_m, gd_b)

    print(f"Fitted line:            y = {gd_m:.4f}x + {gd_b:.4f}")
    print(f"Sum of Squared Errors:  {gd_error:.4f}")
    print(f"Closed-form m,b:        {m:.4f}, {b:.4f}")
    print(f"Grad. desc. m,b:        {gd_m:.4f}, {gd_b:.4f}")


if __name__ == "__main__":
    main()