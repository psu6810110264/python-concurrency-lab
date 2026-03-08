# Python Concurrency Lab

## Project Description / คำอธิบายโปรเจกต์

โปรแกรมนี้เป็น Python program ขนาดเล็กที่สร้างขึ้นเพื่อสาธิตการใช้ **Concurrency ใน Python**

โดยใช้เทคนิคหลัก 3 แบบ ได้แก่

- **Thread**
- **Process Pool**
- **Asyncio**

โปรแกรมนี้มีหน้าที่หลักคือ
1. อ่านไฟล์ `.txt` หลายไฟล์และนับจำนวนบรรทัด
2. ทำการคำนวณที่ใช้ CPU สูง
3. รัน asynchronous tasks หลายงานพร้อมกัน

โปรเจกต์นี้ช่วยแสดงให้เห็นว่าแต่ละเทคนิคเหมาะกับงานประเภทต่างกัน

---

# Features / ความสามารถของโปรแกรม

โปรแกรมสามารถทำงานดังนี้

- อ่านไฟล์ `.txt` หลายไฟล์พร้อมกัน
- นับจำนวนบรรทัดของไฟล์
- คำนวณค่าทางคณิตศาสตร์ที่ใช้ CPU
- รัน asynchronous tasks หลายงานพร้อมกัน
- แสดงตัวอย่างการใช้ concurrency ใน Python

---

# Technologies Used / เทคโนโลยีที่ใช้

- Python 3
- asyncio
- concurrent.futures

โดยใช้

- **ThreadPoolExecutor**
- **ProcessPoolExecutor**

---

# Project Structure / โครงสร้างโปรเจกต์
