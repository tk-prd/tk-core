from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database
models.Base.metadata.create_all(bind=database.engine)
app = FastAPI(title='TK-Core Industrial Risk Engine')
def calculate_industrial_loss(stage, duration_hrs, factory):
    base_loss = duration_hrs * factory.hourly_production_loss_rand
    return round(base_loss + factory.restart_cost_rand if stage >= 4 else base_loss, 2)
@app.get('/analyze-risk/{factory_id}')
def get_risk_assessment(factory_id: int, current_stage: int, duration_hrs: float, db: Session = Depends(database.get_db)):
    factory = db.query(models.FactoryProfile).filter(models.FactoryProfile.id == factory_id).first()
    if not factory: raise HTTPException(status_code=404, detail='Factory not found')
    return {'factory': factory.factory_name, 'estimated_loss_zar': calculate_industrial_loss(current_stage, duration_hrs, factory)}