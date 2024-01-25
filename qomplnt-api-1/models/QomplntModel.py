from sqlalchemy import Column, Integer, String, JSON, Numeric, Table, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from .BaseModel import EntityMeta
import uuid








class QomplntQr(EntityMeta):
    __tablename__ = "qomplnt_or"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    uuid = Column(String(255), unique=True, nullable=False)
    location_id = Column(Integer,  ForeignKey('location.id'))
    b2b_tenant_id = Column(Integer, ForeignKey('b2b_tenant.id'))
    ml_quote = Column(String(255))
    ml_sub_text = Column(String(255)) 
    sub_media = Column(String(255))

    location = relationship("Location", back_populates="qomplnt_qrs")
    b2b_tenant = relationship("B2BTenant", back_populates='qomplnt_qrs')

    def __init__(self, **kwargs):
        if 'uuid' not in kwargs:
            kwargs['uuid'] = str(uuid.uuid4())  # Generate UUID if not provided
        super().__init__(**kwargs)


class B2BTenant(EntityMeta):
    __tablename__ = 'b2b_tenant'

    id = Column(Integer, nullable=False, primary_key=True, index=True)
    name = Column(String(255), index=True) 
    ml_name = Column(String(255), index=True)
    location_id = Column(Integer,  ForeignKey('location.id'))
    media = Column(String(255), index=True)
    qomplnt_qrs = relationship("QomplntQr", back_populates="b2b_tenant") 
    location = relationship("Location", back_populates="b2b_tenant")  

class Location(EntityMeta):
    __tablename__ = 'location'

    id = Column(Integer, nullable=False, primary_key=True)
    geo_id = Column(JSON, nullable = False)
    address1 = Column(String(255), nullable=False)
    address2 = Column(String(255))
    landmark = Column(String(255))
    city_id = Column(Integer, nullable=False)
    zip_code = Column(Integer)

    qomplnt_qrs = relationship("QomplntQr", back_populates="location")  # Define the back_populates correctly
    b2b_tenant = relationship("B2BTenant", back_populates="location")

    __table_args__ = (CheckConstraint('zip_code >= 100000 and zip_code <= 999999'), )

class MultiLingualText(EntityMeta):
    __tablename__ = 'multilingual_text'

    id = Column(Integer, nullable=False, primary_key=True)
    keys = Column(Integer, unique=True, nullable=False, index=True)
    lang_code = Column(Integer, nullable=False, unique=True)    
    display_text = Column(String(255)) 


class City(EntityMeta):
    __tablename__ = 'city'
    id = Column(Integer, nullable=False, primary_key=True)
    city = Column(String(255), nullable=False, server_default='')
    district = Column(String(255), nullable=False, server_default='')
    state = Column(String(255), nullable=False, server_default='')
    country = Column(String(255), nullable=False, server_default='')








