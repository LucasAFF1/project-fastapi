
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.auth.router import auth_router
from app.orders.router import orders_router
from app.exceptions import DomainError


main_app = FastAPI()


main_app.include_router(auth_router, tags=["auth"])
main_app.include_router(orders_router,prefix="/orders" ,tags=["orders"])

@main_app.exception_handler(DomainError)
def excepcion_handler(request: Request, exc: DomainError):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail
    )

def main():
    uvicorn.run(main_app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()

