
## BASIC ROUTES TO IMPLEMENT
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* (Done) | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* (Done) | ```/auth/login/``` | _Login user_|_All users_|
| *POST* (Done)| ```/orders/order/``` | _Place an order_|_All users_|
| *PUT* (Done)| ```/orders/order/status/{order_id}/``` | _Update order status_|_Superuser_|
| *DELETE*(Done) | ```/orders/order/delete/{order_id}/``` | _Delete/Remove an order_ |_All users_|
| *GET* (Done)| ```/orders/user/orders/``` | _Get user's orders_|_All users_|
| *GET*(Done) | ```/orders/orders/``` | _List all orders made_|_Superuser_|
| *GET* (Done)| ```/orders/orders/{order_id}/``` | _Retrieve an order_|_Superuser_|
| *GET* (Done)| ```/orders/user/order/{order_id}/``` | _Get user's specific order_|
| *GET* (Pendiente)| ```/docs/``` | _View API documentation_|_All users_|

