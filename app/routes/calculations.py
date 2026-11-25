from uuid import UUID
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.dependencies import get_current_active_user
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate, CalculationRead
from app.calculation_factory import CalculationFactory

router = APIRouter(prefix="/calculations", tags=["Calculations"])


@router.post(
    "",
    response_model=CalculationRead,
    status_code=status.HTTP_201_CREATED
)
def create_calculation(
    data: CalculationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    try:
        result = CalculationFactory.calculate(data)

        calculation = Calculation(
            a=data.a,
            b=data.b,
            type=data.type.value,
            result=result,
            user_id=current_user.id
        )

        db.add(calculation)
        db.commit()
        db.refresh(calculation)

        return calculation

    except ValueError as exc:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )


@router.get("", response_model=list[CalculationRead])
def list_calculations(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    """Retrieve all calculations belonging to the logged-in user."""

    calculations = (
        db.query(Calculation)
        .filter(Calculation.user_id == current_user.id)
        .all()
    )

    return calculations


class CalculationUpdate(BaseModel):
    a: float
    b: float
    type: str


@router.get("/{calc_id}", response_model=CalculationRead)
def read_calculation(
    calc_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    calculation = db.query(Calculation).filter(
        Calculation.id == calc_id,
        Calculation.user_id == current_user.id
    ).first()

    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")

    return calculation


@router.put("/{calc_id}", response_model=CalculationRead)
def update_calculation(
    calc_id: UUID,
    data: CalculationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    calculation = db.query(Calculation).filter(
        Calculation.id == calc_id,
        Calculation.user_id == current_user.id
    ).first()

    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")

    calculation.a = data.a
    calculation.b = data.b
    calculation.type = data.type.value
    calculation.result = CalculationFactory.calculate(data)

    db.commit()
    db.refresh(calculation)

    return calculation


@router.delete("/{calc_id}", status_code=204)
def delete_calculation(
    calc_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    calculation = db.query(Calculation).filter(
        Calculation.id == calc_id,
        Calculation.user_id == current_user.id
    ).first()

    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")

    db.delete(calculation)
    db.commit()
    return None
