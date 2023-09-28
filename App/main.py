from fastapi import FastAPI, HTTPException, status, Response, Path, Query

from pyngrok import ngrok

from routes import aliens_router, pirates_router, kanye_router

app = FastAPI()

app.include_router(aliens_router.router, prefix="/api/v1/aliens", tags=['aliens'])
app.include_router(pirates_router.router, prefix="/api/v1/pirates", tags=['pirates'])
app.include_router(kanye_router.router, prefix="/api/v1/kanye", tags=['kanye'])

if __name__ == "__main__":
    import uvicorn

    # ngrok_tunnel = ngrok.connect(8000)
    # print("Public URL: ", ngrok_tunnel.public_url)
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info", reload=True)
