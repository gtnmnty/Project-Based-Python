from abc import ABC, abstractmethod


def calc_mean(values):
    return sum(values) / len(values)


class BaseModel(ABC):
    def __init__(self):
        self.is_fitted = False

    @abstractmethod
    def fit(self, x, y):
        raise NotImplementedError

    # abstractmethod annotation already have NotImplementedError
    # so no need to add: raise NotImplementedError
    @abstractmethod
    def predict(self, x):
        if not self.is_fitted:
            raise RuntimeError("Call fit() first")


class ConstantModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.value = None

    def fit(self, x, y):
        self.value = calc_mean(y)
        self.is_fitted = True

    def predict(self, x):
        super().predict(x)
        return [self.value] * len(x)


class LinearModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.m = None
        self.b = None

    def fit(self, x, y):
        x_mean = calc_mean(x)
        y_mean = calc_mean(y)
        numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
        denominator = sum((xi - x_mean) ** 2 for xi in x)
        self.m = numerator / denominator
        self.b = y_mean - self.m * x_mean
        self.is_fitted = True

    def predict(self, x):
        super().predict(x)
        return [self.m * xi + self.b for xi in x]


def evaluate(model, x_test, y_test):
    predictions = model.predict(x_test)
    errors = [abs(a - p) for a, p in zip(y_test, predictions)]
    return sum(errors) / len(errors)


def main():
    #print(isinstance(LinearModel(), ConstantModel))

    # m = ConstantModel()
    # m.predict([1, 2, 3])
    # print(m)

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2.1, 4.2, 5.8, 8.1, 9.9, 12.2, 13.8, 16.1, 17.9, 20.2]


    split = 7
    x_train, y_train = x[:split], y[:split]
    x_test, y_test = x[split:], y[split:]

    const_model = ConstantModel()
    linear_model = LinearModel()

    # Train
    const_model.fit(x_train, y_train)
    linear_model.fit(x_train, y_train)

    # Evaluate (model is already trained)
    mae_const = evaluate(const_model, x_test, y_test)
    mae_linear = evaluate(linear_model, x_test, y_test)

    if mae_linear < mae_const:
        improvement = (1 - mae_linear / mae_const) * 100
        print(f"LinearModel beats baseline by {improvement:.1f}%")
    else:
        print("Baseline wins — no linear signal!")


if __name__ == "__main__":
    main()