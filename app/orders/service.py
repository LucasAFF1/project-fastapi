import uuid

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.orders.schemas import OrderIn
from app.models import UserModel
from app.orders.models import Order, Order_Status
from app.exceptions import OrderNotFound, NotAuthorized
from app.orders.schemas import OrdersList


def get_order_by_id(order_id: uuid.UUID, session: Session, current_user: UserModel)->Order:
    order = session.get(Order, order_id)
    if not order: 
        raise OrderNotFound()
    if not current_user.is_staff or (current_user.id != order.user_id):
        raise NotAuthorized()
    return order

def get_all_orders(session: Session, current_user:UserModel, offset: int = 0, limit: int = 100)->OrdersList:
    if current_user.is_staff: 
        count = session.execute(select(func.count()).select_from(Order)).one()
        orders = session.execute(select(Order).order_by(Order.ordered_at).offset(offset).limit(limit)).all()
    else: 
        count = session.execute(select(func.count()).select_from(Order).where(Order.user_id == current_user.id)).one()
        orders = session.execute(select(Order).where(Order.user_id == current_user.id).order_by(Order.ordered_at).offset(offset).limit(limit)).all()
    return OrdersList(data=orders, quantity=count)


def place_order(order_in: OrderIn, 
                      user: UserModel, 
                      session: Session)->Order:
    order = Order(**order_in.model_dump(), user_id = user.id)
    order.user = user 
    
    session.add(order)
    session.commit()
    session.refresh(order)

    return order 
    

def remove_order(order_id: uuid.UUID, session: Session, current_user: UserModel)->dict[str,str]: 
    order = get_order_by_id(order_id, session, current_user)
    
    session.delete(order)
    session.commit()
    return {"msg": "order deleted succesfully"}


def update_order_status(order_id: uuid.UUID, 
                        session: Session, 
                        current_user: UserModel,
                        new_status: Order_Status)->dict[str,str]: 
    order = get_order_by_id(order_id, session, current_user)

    order.order_status = new_status 

    return {"update": f"the order is now {new_status}"}



    


