import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from app.orders.service import (place_order, 
                            remove_order, get_order_by_id, 
                            update_order_status,
                            get_all_orders)
from app.orders.models import Order_Status
from app.orders.schemas import OrderIn, OrderOut
from app.auth.dependencies import current_user
from app.database import SessionDep
from app.models import UserModel

orders_router = APIRouter()
      

@orders_router.get("/{id}", response_model=OrderOut)
def order_by_id(id: uuid.UUID, session: SessionDep,
                 current_user = Depends(current_user)):
    return get_order_by_id(id, session, current_user)


@orders_router.get("/")
def user_orders(session:SessionDep, user: UserModel = Depends(current_user)):
    return get_all_orders(session, user)


@orders_router.post("/new", response_model=OrderOut)
def new_order(order_in: OrderIn, 
                    user: Annotated[UserModel, Depends(current_user)],
                    session: SessionDep):
    order = place_order(order_in, user, session)
    return order 


@orders_router.delete("/{id}")
def delete_order_by_id(id: uuid.UUID, session: SessionDep,
                  current_user = Depends(current_user)):
    return remove_order(id, session, current_user)


@orders_router.patch("/{id}/update")
def update_order(id: uuid.UUID, session: SessionDep, 
                 new_status: Order_Status,
                 current_user = Depends(current_user)):
    return update_order_status(id, session, current_user,new_status)


