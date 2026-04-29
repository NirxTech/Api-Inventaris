from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Barang(Base):
    __tablename__ = "barang"
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    deskripsi = Column(String)
    stok = Column(Integer, default=0)
    
    transaksi = relationship("Transaksi", back_populates="barang")

class Transaksi(Base):
    __tablename__ = "transaksi"
    id = Column(Integer, primary_key=True, index=True)
    barang_id = Column(Integer, ForeignKey("barang.id"))
    jenis = Column(String) # "MASUK" atau "KELUAR"
    jumlah = Column(Integer)
    tanggal = Column(DateTime, default=datetime.utcnow)
    
    barang = relationship("Barang", back_populates="transaksi")