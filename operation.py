from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class Currency:
    name: str
    code: str


@dataclass
class OperationAmount:
    amount: str
    currency: Currency


@dataclass
class Operation:
    id: int
    state: str
    date: str | datetime
    operationAmount: OperationAmount
    description: str
    from_: str
    to: str
