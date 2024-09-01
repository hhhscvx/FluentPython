def make_averager():
    series = []

    def averager(new_value: float) -> float:
        series.append(new_value)  # видит неглобальную переменную, определенную все своего тела (замыкание)
        total = sum(series)
        return total / len(series)
    return averager
