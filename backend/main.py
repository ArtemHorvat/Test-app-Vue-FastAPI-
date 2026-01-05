import random
import string

from typing import Annotated, List
from fastapi import FastAPI, Body, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

ALPHABET_ID = string.ascii_letters + string.digits

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CommentId = Annotated[
    str, 
    Field(
        min_length=8, 
        max_length=8, 
        pattern=r"^[a-zA-Z0-9]+$",
        description="Уникальные ID комментария")
]

CommentUsername = Annotated[
    str,
    Field(
        min_length=2, 
        max_length=20)
]

CommentText = Annotated[
    str,
    Field(
        min_length=1,
        max_length=150
    )
]


class Comment(BaseModel):
    """
    Модель валидации хранимых данных
    """
    id: CommentId
    username: CommentUsername
    comment: CommentText

class CommentCreate(BaseModel):
    """
    Модель валидаци полученных данных
    """
    username: CommentUsername
    comment: CommentText

class CommentUpdate(BaseModel):
    comment: CommentText

project_db = [Comment(id="8dvsfJuK", username="Bob", comment="It's funny :)"),
              Comment(id="XuF8W0bo", username="Alice", comment="For what this?"),
              Comment(id="mvclTS2h", username="James", comment="Simple app, good for study"),
              Comment(id="2lclvZI1", username="Artem", comment="This is the end of comments. Try contimnue"),
              Comment(id="2lc55ZI1", username="Vanya", comment="Hahahaha")]

def create_key() -> str:
    """
    Создает уникальный ключ для каждой записи
    """
    return ''.join(random.choices(ALPHABET_ID, k=8))


@app.get('/comments', response_model = List[Comment]) 
async def get_comments() -> list[Comment]:
    """
    Возвращает все коментарии из project_db
    """
    return project_db


@app.post('/comments', 
          response_model=Comment, 
          status_code=status.HTTP_201_CREATED)


# Вариант, где всё идет в Body посредством модели CommentCreate
async def create_comment(data: CommentCreate) -> Comment:
    """
    Получает новый комментарий и записывает в project_db
    """
    key = create_key()

    new_comment = Comment(id=key, username=data.username, comment=data.comment)
    project_db.append(new_comment)
    return new_comment


# Вариант, где часть выражения идет через Path, а другая - через Body
@app.patch('/comments/{comment_id}',
           response_model=Comment, 
           status_code=status.HTTP_200_OK)

async def replace_comment(comment_id: CommentId,
                          new_message: CommentUpdate) -> Comment:
    """
    Редактирует содержимое комментария по ID
    """
    for comment_item in project_db:
        if comment_item.id == comment_id:
            comment_item.comment = new_message.comment
            return comment_item
    raise HTTPException(
        status_code=404,
        detail="Comment not found"
    )

@app.delete('/comments/{comment_id}',
            response_model=Comment,
            status_code=status.HTTP_200_OK)

async def delete_comment(comment_id: CommentId) -> Comment:
    """
    Удаляет комментарий по ID
    """
    for comment_item in project_db:
        if comment_item.id == comment_id:
            project_db.remove(comment_item)
            return comment_item
    raise HTTPException(
        status_code=404,
        detail="Comment not found"
    )