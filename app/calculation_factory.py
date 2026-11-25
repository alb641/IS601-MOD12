
from app.schemas.calculation import CalculationCreate, CalculationType


class CalculationFactory:

    @staticmethod
    def calculate(data: CalculationCreate) -> float:
        if data.type == CalculationType.Add:
            return data.a + data.b

        elif data.type == CalculationType.Subtract:
            return data.a - data.b

        elif data.type == CalculationType.Multiply:
            return data.a * data.b

        elif data.type == CalculationType.Divide:
            if data.b == 0:
                raise ValueError("Cannot divide by zero")
            return data.a / data.b

        raise ValueError("Invalid calculation type")


