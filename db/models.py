from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import  String, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass

class Appoinments(Base):
    __tablename__ = 'appointments'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    service: Mapped[str] = mapped_column(String(50), nullable=True)

# Logging
    def __repr__(self) -> str:
        return (f"Appointment(id={self.id}, name={self.name}, phone={self.phone}, "
                f"email={self.email}, date={self.date})")
    