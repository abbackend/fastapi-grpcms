from pydantic import BaseModel, Field, PositiveInt


class AddRequest(BaseModel):
    street: str = Field(min_length=3)
    city: str = Field(min_length=3)
    state: str = Field(max_length=2)
    zip: PositiveInt = 1234
