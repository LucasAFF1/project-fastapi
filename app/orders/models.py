import uuid
from datetime import datetime

from sqlalchemy import Integer, VARCHAR, Enum, DateTime, ForeignKey, UUID, func
from sqlalchemy.orm import mapped_column, Mapped, relationship
import enum 

from app.models import UserModel
from app.database import Base


class Order_Status(enum.Enum):
    pending = "pending"
    in_transit = "in transit"
    delivered = "delivered"

class Pizza_Size(enum.Enum):
    small = "small"
    medium = "medium"
    large = "large"
    extra_large = "extra_large"

class Order(Base): 
    __tablename__ = "orders"


    id: Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    order_status: Mapped[Order_Status] = mapped_column(Enum(Order_Status),default=Order_Status.pending, nullable=False, index=True)
    pizza_size: Mapped[Pizza_Size] = mapped_column(Enum(Pizza_Size), nullable=False)
    flavour: Mapped[str] = mapped_column(VARCHAR(20))

    ordered_at: Mapped[datetime|None] = mapped_column(DateTime(timezone=True), default=func.now(), nullable=False)

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False) 

    user: Mapped[UserModel] = relationship(back_populates="orders")

    def __repr__(self): 
        return f"Order {self.id}"


    

