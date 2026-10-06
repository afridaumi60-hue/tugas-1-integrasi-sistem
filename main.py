from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Tugas 1 Integrasi Sistem", version="1.0")

# Model Data sesuai perintah tugas (Nama, Alamat, IPK, Semester, Hobi)
class Mahasiswa(BaseModel):
    id: int
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str

class MahasiswaUpdate(BaseModel):
    nama: Optional[str] = None
    alamat: Optional[str] = None
    ipk: Optional[float] = None
    semester: Optional[int] = None
    hobi: Optional[str] = None

# Database sementara menggunakan list di memori komputer
database_mahasiswa = []

# 1. GET: Menampilkan semua data
@app.get("/mahasiswa", response_model=List[Mahasiswa])
def get_mahasiswa():
    return database_mahasiswa

# 2. POST: Menambahkan data baru
@app.post("/mahasiswa", response_model=Mahasiswa)
def tambah_mahasiswa(data: Mahasiswa):
    for mhs in database_mahasiswa:
        if mhs.id == data.id:
            raise HTTPException(status_code=400, detail="ID Mahasiswa sudah ada!")
    database_mahasiswa.append(data)
    return data

# 3. PUT: Mengubah data berdasarkan ID
@app.put("/mahasiswa/{id}", response_model=Mahasiswa)
def update_mahasiswa(id: int, data: MahasiswaUpdate):
    for mhs in database_mahasiswa:
        if mhs.id == id:
            if data.nama is not None:
                mhs.nama = data.nama
            if data.alamat is not None:
                mhs.alamat = data.alamat
            if data.ipk is not None:
                mhs.ipk = data.ipk
            if data.semester is not None:
                mhs.semester = data.semester
            if data.hobi is not None:
                mhs.hobi = data.hobi
            return mhs
    raise HTTPException(status_code=404, detail="Data Mahasiswa tidak ditemukan!")

# 4. DELETE: Menghapus data berdasarkan ID
@app.delete("/mahasiswa/{id}")
def hapus_mahasiswa(id: int):
    for index, mhs in enumerate(database_mahasiswa):
        if mhs.id == id:
            database_mahasiswa.pop(index)
            return {"message": f"Data mahasiswa dengan ID {id} berhasil dihapus"}
    raise HTTPException(status_code=404, detail="Data Mahasiswa tidak ditemukan!")