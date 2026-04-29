from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# --- Schemas untuk User & Auth ---
class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# --- Schemas untuk Barang ---
class BarangBase(BaseModel):
    nama: str
    deskripsi: Optional[str] = None

class BarangCreate(BarangBase):
    stok_awal: int = 0

class BarangResponse(BarangBase):
    id: int
    stok: int

    class Config:
        from_attributes = True

# --- Schemas untuk Transaksi ---
class TransaksiCreate(BaseModel):
    barang_id: int
    jenis: str # Harus "MASUK" atau "KELUAR"
    jumlah: int

class TransaksiResponse(BaseModel):
    id: int
    barang_id: int
    jenis: str
    jumlah: int
    tanggal: datetime

    class Config:
        from_attributes = True

# --- Schemas untuk Laporan ---
class LaporanInventaris(BaseModel):
    total_jenis_barang: int
    total_stok_keseluruhan: int
    barang_list: List[BarangResponse]