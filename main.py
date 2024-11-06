
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from response.endpoint import view_app


load_dotenv()






app = FastAPI(description='Это АПИ для получения данных от погоды с погодой')
app.include_router(view_app)




if __name__ == "__main__":
	uvicorn.run('main:app', host='127.0.0.1', port=5659, reload=True)


