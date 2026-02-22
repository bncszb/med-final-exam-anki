from pydantic import BaseModel, Field
from typing import List, Optional


class Chapter(BaseModel):
    name: str = Field(alias="nev")
    serial_number: str = Field(alias="sorszam")
    id: int


class UpdateTaskGroup(BaseModel):
    last_updated: int = Field(alias="frissitesFormatted")


class TaskGroup(BaseModel):
    chapters: List[Chapter] = Field(alias="fejezet")
    id: int
    short_name: str = Field(alias="rovid")
    name: str = Field(alias="nev")
    updates: List[UpdateTaskGroup] = Field(alias="frissitesFeladatCsoport")


class TaskGroupResult(BaseModel):
    task_groups: List[TaskGroup] = Field(alias="feladatCsoport")
    id: int


class TaskGroupResponse(BaseModel):
    result: TaskGroupResult


class QuestionAnswer(BaseModel):
    is_correct: int = Field(alias="helyes")
    explanation_plain_text: Optional[str] = Field(alias="magyarazatPlaintext")
    has_image: int = Field(alias="vanKepIn")
    letter: str = Field(alias="betujel")
    text: str = Field(alias="szoveg")
    explanation: Optional[str] = Field(alias="magyarazat")
    id: int
    text_plain_text: str = Field(alias="szovegPlaintext")


class Question(BaseModel):
    serial_number: str = Field(alias="csorszam")
    explanation_plain_text: Optional[str] = Field(alias="magyarazatPlaintext")
    sub_serial_number: int = Field(alias="alSorszam")
    sub_sub_serial_number: int = Field(alias="subSorszam")
    has_image: int = Field(alias="vanKepIn")
    answers: List[QuestionAnswer] = Field(alias="kerdesValasz")
    description: str = Field(alias="leiras")
    difficulty: Optional[int] = Field(alias="nehezseg")
    task_type_id: int = Field(alias="feladatTipusId")
    status_id: Optional[int] = Field(alias="statuszId")
    sorszam: int
    explanation: Optional[str] = Field(alias="magyarazat")
    id: int
    description_plain_text: str = Field(alias="leirasPlaintext")
    is_not_permanent: bool = Field(alias="nemperm")
    is_active: bool = Field(alias="aktiv")
