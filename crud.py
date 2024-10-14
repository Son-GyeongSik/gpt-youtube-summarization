from sqlalchemy.orm import Session

from model import Summary


def db_add_summary(db: Session, summary: str, code: str):

    summary_input = Summary(summary=summary, videoCode=code, is_created=True)

    db.add(summary_input)
    db.commit()
    db.refresh(summary_input)
    return summary


def db_get_summary(db: Session, code: str):
    return db.query(Summary).filter(Summary.videoCode == code).first()