from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str | None = None
    name : str
    email: str
    password: str | None = None
    picture: str

