import uuid
from typing import TYPE_CHECKING
from pydantic import EmailStr

from sqlalchemy import Boolean, VARCHAR, TEXT, UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base

if TYPE_CHECKING:
    from orders.models import Order
        

class UserModel(Base): 
    __tablename__ = "users"

    id:Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: Mapped[str]= mapped_column(VARCHAR(20), index = True, nullable=False)
    email: Mapped[EmailStr] = mapped_column(VARCHAR(256), index=True,nullable=False) 
    password: Mapped[str] = mapped_column(TEXT, nullable=False)

    is_active: Mapped[bool|None] = mapped_column(Boolean, default=True, index=True, nullable=False)
    is_staff:Mapped[bool|None] = mapped_column(Boolean, default=False, index=True, nullable=False)

    orders: Mapped[list["Order"]] = relationship(back_populates="user")

    def __repr__(self): 
        return "User {self.id}, {self.username}"
    



    


