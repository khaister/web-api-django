from pydantic import BaseModel


class Person(BaseModel):
    name: str
    url: str | None


class TvShow(BaseModel):
    id: int
    synopsis: str | None = None
    year_start: int | None = None
    year_stop: int | None = None
    creators: list[Person]


class TvShows(BaseModel):
    shows: list[TvShow]
