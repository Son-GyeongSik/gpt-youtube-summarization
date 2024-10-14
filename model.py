from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Summary(Base):
    __tablename__ = 'summary'

    summaryId = Column(Integer, primary_key=True)
    videoCode = Column(String)
    summary = Column(String)
    is_created = Column(Boolean, default=False)