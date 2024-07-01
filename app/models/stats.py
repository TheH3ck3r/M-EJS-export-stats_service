import uuid
from pydantic import BaseModel, Field
import datetime


class Item(BaseModel):
    student_id: uuid.UUID = Field(alias="studentId")
    date: datetime.date
    discipline_id: uuid.UUID = Field(alias="disciplineId")
    discipline_type: int = Field(alias="disciplineType")
    absence_type: int = Field(alias="absenceType")
    start_at: str = Field(alias="startAt")
    finish_at: str = Field(alias="finishAt")


class Stats(BaseModel):
    items: list[Item]
    students: dict[uuid.UUID, str]
    disciplines: dict[uuid.UUID, list[str]]


class CommonStats(BaseModel):
    student_id: uuid.UUID = Field(alias="studentId")
    discipline_id: uuid.UUID = Field(alias="disciplineId")
    count: int


class CommonStatsList(BaseModel):
    __root__: list[CommonStats]


class MonthStats(BaseModel):
    student_id: uuid.UUID = Field(alias="studentId")
    date: datetime.datetime
    count: int


class MonthStatsList(BaseModel):
    __root__: list[MonthStats]


def absence_type_view(absence_type: int):
    views = ["Н", "У", "З"]
    return views[absence_type]


def months_in_semester(term: int):
    return [["Сентябрь", "Октябрь", "Ноябрь", "Декабрь"], ["Февраль", "Март", "Апрель", "Май"]][term]


def discipline_type_view(discipline_type: int):
    return ["Лек", "Пр", "Лаб", "С/Р"][discipline_type]
