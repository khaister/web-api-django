from pydantic import BaseModel, Field


class Creator(BaseModel):
    name: str
    url: str | None


class Info(BaseModel):
    id: int
    synopsis: str | None = None
    years_aired: str | None = Field(alias="yearsAired")
    creators: list[Creator]
