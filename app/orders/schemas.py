import uuid

from pydantic import BaseModel
from typing import Any
from datetime import datetime

from app.orders.models import Pizza_Size, Order


class OrderIn(BaseModel):
    quantity:int 
    pizza_size: Pizza_Size
    flavour: str 

class OrdersList(BaseModel):
    data: Any 
    quantity: Any


class OrderOut(OrderIn): 
    id: uuid.UUID 
    ordered_at: datetime


