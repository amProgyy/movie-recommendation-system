from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="movie recommendation system")
app.mount("/static", StaticFiles(directory="static"), name='static')

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request = request,
        name = "sign_in.html",
        
    )

@app.get('/sign_up', response_class=HTMLResponse)
async def sign_up(request: Request):
    return templates.TemplateResponse(
        request = request,
        name ='sign_up.html',
        

    )

@app.get('/sign_in', response_class=HTMLResponse)
async def sign_in(request: Request):
    return templates.TemplateResponse(
        request = request,
        name ='sign_in.html',
        
        
    )

@app.get('/recommend')
async def recommend(movie:str):
    return {
        'movie': movie,
        'recommends': []
    }

