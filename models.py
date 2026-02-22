from pydantic import BaseModel, Field
from typing import List, Optional, Union


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


class AssociationItemLink(BaseModel):
    question_id: int = Field(alias="kerdesId")
    id: int


class AssociationItem(BaseModel):
    has_image: int = Field(alias="vanKepIn")
    letter: str = Field(alias="betujel")
    text: str = Field(alias="szoveg")
    links: List[AssociationItemLink] = Field(alias="asszociaciosLeirasTetel")
    id: int
    text_plain_text: str = Field(alias="szovegPlaintext")


class Association(BaseModel):
    to_sub_serial_number: Optional[int] = Field(alias="alsorszamIg")
    serial_number: str = Field(alias="csorszam")
    from_sub_serial_number: Optional[int] = Field(alias="alsorszamTol")
    items: List[AssociationItem] = Field(alias="leirasTetelAsszociacios")
    has_image: int = Field(alias="vanKepIn")
    from_sub_sub_serial_number: Optional[int] = Field(alias="subsorszamTol")
    description: str = Field(alias="leiras")
    id: int
    description_plain_text: str = Field(alias="leirasPlaintext")
    from_serial_number: int = Field(alias="sorszamTol")
    to_sub_sub_serial_number: Optional[int] = Field(alias="subsorszamIg")
    to_serial_number: int = Field(alias="sorszamIg")


class Question(BaseModel):
    serial_number: str = Field(alias="csorszam")
    explanation_plain_text: Optional[str] = Field(alias="magyarazatPlaintext")
    sub_serial_number: int = Field(alias="alSorszam")
    sub_sub_serial_number: int = Field(alias="subSorszam")
    has_image: int = Field(alias="vanKepIn")
    answers: Optional[List[QuestionAnswer]] = Field(alias="kerdesValasz", default=None)
    description: str = Field(alias="leiras")
    difficulty: Optional[int] = Field(alias="nehezseg")
    task_type_id: int = Field(alias="feladatTipusId")
    status_id: Optional[Union[str, int]] = Field(alias="statuszId")
    sorszam: int
    explanation: Optional[str] = Field(alias="magyarazat")
    id: int
    description_plain_text: str = Field(alias="leirasPlaintext")
    is_not_permanent: bool = Field(alias="nemperm")
    is_active: bool = Field(alias="aktiv")
    association: Optional[Association] = Field(alias="asszociaciosLeiras", default=None)
