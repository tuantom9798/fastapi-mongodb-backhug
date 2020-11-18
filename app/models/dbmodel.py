from datetime import datetime
from typing import Optional
from util import *
from pydantic import BaseModel, Schema, Field
from bson.objectid import ObjectId

class DBModelMixin2(BaseModel):
    created_at: Optional[datetime] = Schema(now_utc(), alias="createdAt")
    updated_at: Optional[datetime] = Schema(now_utc(), alias="updatedAt")
   

class BaseDocument(BaseModel):
    create_time: Optional[datetime] = Schema(now_utc(), alias="createdAt")
    update_time: Optional[datetime] = Schema(now_utc(), alias="updatedAt")

    
class DBModelMixin(DBModelMixin2):
    _id: Optional[str] = Field(None, alias='id of collection')