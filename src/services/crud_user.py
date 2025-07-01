from sqlmodel import Session, select
from config.connection import engine
from model.user import User

def signin_or_register(user: User) -> int | None:

    with Session(engine) as session:
        statement = select(User).where(User.email == user.email)
        find_user = session.exec(statement).first()
        if not find_user:
            print("el usuario no existe, creando uno nuevo")
            new_user = User(
                name=user.name,
                email=user.email,
                picture=user.picture,
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            find_user = new_user
        else:
            print(f"el usuario ya existe, retornando {find_user.name}")

        return find_user.id
