from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from src.recommendation.service import MovieRecommender
from src.auth.router import router as auth_router
from src.users.schemas import UserCreate

app = FastAPI(title="movie recommendation system")
app.mount("/static", StaticFiles(directory="static"), name='static')
app.include_router(auth_router)

templates = Jinja2Templates(directory='templates')

recommender = MovieRecommender()

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

@app.post('/sign_up')
async def register_user(user: UserCreate):

    print("Username:", user.username)
    print("Email:", user.email)

    

    return {
        "message": "Registration successful!"
    }

@app.get('/sign_in', response_class=HTMLResponse)
async def sign_in(request: Request):
    return templates.TemplateResponse(
        request = request,
        name ='sign_in.html',
        
        
    )

# @app.get('/recommend')
# async def recommend(movie:str, no_of_movies: int = 5):

#     recommendations = recommender.recommend(
#         movie_title=movie, no_of_movies=no_of_movies
#     )
#     print(recommendations)
#     return {
#         'recommendation' : recommendations,
#         'movie': movie,
#     }

@app.get('/recommend', response_class=HTMLResponse)
async def recommend(request: Request):
    return templates.TemplateResponse(
        request = request,
        name ='recommendation.html',    
    )


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
