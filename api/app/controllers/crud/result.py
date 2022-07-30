from typing import List
from datetime import datetime
from fastapi import HTTPException
from app.models import session, Result, ResultCreate, ResultRead, ResultUpdate, RcpChoices, RcpResults

from sqlmodel import select

def create_result(result: ResultCreate) -> ResultRead:
    result_remapped = Result.from_orm(result)
    session.add(result_remapped)
    try:
        session.commit()
    except:
        session.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    else:
        session.refresh(result_remapped)
        return ResultRead.from_orm(result_remapped)

def get_results(skip: int = 0, limit: int = 100) -> List[ResultRead]:
    results = session.exec(select(Result).order_by(Result.id).offset(skip).limit(limit)).all()
    if len(results) == 0:
        raise HTTPException(status_code=404, detail="Result not found")
    return [ResultRead.from_orm(result) for result in results]

def get_result(result_id: int) -> ResultRead:
    result = session.get(Result, result_id)
    if result:
        result = ResultRead.from_orm(result)
        return result
    else:
        raise HTTPException(status_code=404, detail="Result not found")

def update_result(result_id: int, result: ResultUpdate) -> ResultRead:
    db_result = session.get(Result, result_id)
    if not db_result:
        raise HTTPException(status_code=404, detail="Result not found")
    result_data = result.dict(exclude_unset=True)
    for key, value in result_data.items():
        if value is not None:
            setattr(db_result, key, value)
    setattr(db_result, "updated_at", datetime.now())
    session.add(db_result)
    session.commit()
    session.refresh(db_result)
    db_result = ResultRead.from_orm(db_result)
    return db_result

def delete_result(result_id: int) -> bool:
    result = session.get(Result, result_id)
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")
    session.delete(result)
    session.commit()
    return True

def get_result_counts() -> dict:
    results = {k: len(session.exec(select(Result).filter(Result.result == RcpResults.WIN).filter(Result.choice == k)).all()) for k in RcpChoices.__members__.keys()}
    return results