
from pydantic import BaseModel, Field


class Chapter(BaseModel):
    name: str = Field(alias="nev")
    serial_number: str = Field(alias="sorszam")
    id: int


class UpdateTaskGroup(BaseModel):
    last_updated: int = Field(alias="frissitesFormatted")


class TaskGroup(BaseModel):
    chapters: list[Chapter] = Field(alias="fejezet")
    id: int
    short_name: str = Field(alias="rovid")
    name: str = Field(alias="nev")
    updates: list[UpdateTaskGroup] = Field(alias="frissitesFeladatCsoport")


class TaskGroupResult(BaseModel):
    task_groups: list[TaskGroup] = Field(alias="feladatCsoport")
    id: int


class TaskGroupResponse(BaseModel):
    result: TaskGroupResult


class QuestionAnswer(BaseModel):
    is_correct: int = Field(alias="helyes")
    explanation_plain_text: str | None = Field(alias="magyarazatPlaintext")
    has_image: int = Field(alias="vanKepIn")
    letter: str = Field(alias="betujel")
    text: str = Field(alias="szoveg")
    explanation: str | None = Field(alias="magyarazat")
    id: int
    text_plain_text: str | None = Field(alias="szovegPlaintext")


class QuestionElementAnswer(BaseModel):
    has_image: int = Field(alias="vanKepIn")
    number: str = Field(alias="szam")
    text: str = Field(alias="szoveg")
    id: int


class AssociationItemLink(BaseModel):
    question_id: int = Field(alias="kerdesId")
    id: int


class AssociationItem(BaseModel):
    has_image: int = Field(alias="vanKepIn")
    letter: str = Field(alias="betujel")
    text: str = Field(alias="szoveg")
    links: list[AssociationItemLink] = Field(alias="asszociaciosLeirasTetel")
    id: int
    text_plain_text: str = Field(alias="szovegPlaintext")


class Association(BaseModel):
    to_sub_serial_number: int | None = Field(alias="alsorszamIg")
    serial_number: str = Field(alias="csorszam")
    from_sub_serial_number: int | None = Field(alias="alsorszamTol")
    items: list[AssociationItem] = Field(alias="leirasTetelAsszociacios")
    has_image: int = Field(alias="vanKepIn")
    from_sub_sub_serial_number: int | None = Field(alias="subsorszamTol")
    description: str = Field(alias="leiras")
    id: int
    description_plain_text: str = Field(alias="leirasPlaintext")
    from_serial_number: int = Field(alias="sorszamTol")
    to_sub_sub_serial_number: int | None = Field(alias="subsorszamIg")
    to_serial_number: int = Field(alias="sorszamIg")


class CaseDescription(BaseModel):
    name_plain_text: str | None = Field(alias="nevPlaintext")
    serial_number: str = Field(alias="csorszam")
    description: str = Field(alias="leiras")
    id: int
    description_plain_text: str = Field(alias="leirasPlaintext")
    name: str | None = Field(alias="nev")


class Question(BaseModel):
    serial_number: str = Field(alias="csorszam")
    explanation_plain_text: str | None = Field(alias="magyarazatPlaintext")
    sub_serial_number: int = Field(alias="alSorszam")
    sub_sub_serial_number: int = Field(alias="subSorszam")
    has_image: int = Field(alias="vanKepIn")
    answers: list[QuestionAnswer] | None = Field(alias="kerdesValasz", default=None)
    description: str = Field(alias="leiras")
    difficulty: int | None = Field(alias="nehezseg")
    task_type_id: int = Field(alias="feladatTipusId")
    status_id: str | int | None = Field(alias="statuszId")
    sorszam: int
    explanation: str | None = Field(alias="magyarazat")
    id: int
    description_plain_text: str = Field(alias="leirasPlaintext")
    is_not_permanent: bool = Field(alias="nemperm")
    is_active: bool = Field(alias="aktiv")
    association: Association | None = Field(alias="asszociaciosLeiras", default=None)
    element_answers: list[QuestionElementAnswer] | None = Field(alias="kerdesElemiValasz", default=None)
    case_description: CaseDescription | None = Field(alias="esetleiras", default=None)


class ChapterOutput(BaseModel):
    name: str
    questions: list[Question]


class GroupOutput(BaseModel):
    name: str
    chapters: list[ChapterOutput] | None = None
    questions: list[Question] | None = None
