from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from DB import Base


class Image:
    __tablename__ = "images"

    