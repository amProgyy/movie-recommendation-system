from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    movie: str
    no_of_movies: int = 5

