from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from .database import Base
class OutageEvent(Base):
    __tablename__ = 'outage_history'
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    area_name = Column(String, index=True)
    stage = Column(Integer)
    duration_minutes = Column(Integer)
class FactoryProfile(Base):
    __tablename__ = 'factory_profiles'
    id = Column(Integer, primary_key=True, index=True)
    factory_name = Column(String, unique=True, index=True)
    industry_type = Column(String)
    hourly_production_loss_rand = Column(Float)
    restart_cost_rand = Column(Float)