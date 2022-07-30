from typing import List
from fastapi import APIRouter

import app.controllers.crud as crud

router = APIRouter()

@router.post("/", response_model=crud.result.ResultRead)
def create_result(result: crud.result.ResultCreate) -> crud.result.ResultRead:
    result_obj = crud.result.create_result(result)
    return crud.result.ResultRead.from_orm(result_obj)

@router.get("/", response_model=List[crud.result.ResultRead])
def get_results(skip: int=0, limit: int=100) -> List[crud.result.ResultRead]:
    result_obj = crud.result.get_results(skip=skip, limit=limit)
    return result_obj

@router.get("/{result_id}", response_model=crud.result.ResultRead)
def get_result(result_id: int) -> crud.result.ResultRead:
    result_obj = crud.result.get_result(result_id=result_id)
    return result_obj

@router.patch("/{result_id}", response_model=crud.result.ResultRead)
def update_result(result_id: int, result: crud.result.ResultUpdate) -> crud.result.ResultRead:
    result_obj = crud.result.update_result(result_id=result_id, result=result)
    return result_obj

@router.delete("/{result_id}")
def delete_result(result_id: int) -> dict:
    crud.result.delete_result(result_id=result_id)
    return {"status": "success"}