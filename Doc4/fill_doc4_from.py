from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
import datetime
import os

# === กำหนดพาธต่าง ๆ ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "font"))
input_pdf_path = os.path.join(BASE_DIR, "Doc4.pdf")
output_pdf_path = os.path.join(BASE_DIR, "output.pdf")
c = canvas.Canvas("output.pdf")

# === ค่าคงที่ ===
max_height = 790
checkmark = "✔"

def draw_text(can, text, x, y, font="THSarabun", size=16):
    can.setFont(font, size)
    can.drawString(x, y, text)

def fill_doc4_form(input_pdf_path, output_pdf_path):
    # โหลดฟอนต์
    try:
        pdfmetrics.registerFont(TTFont('THSarabun', os.path.join(FONT_DIR, 'THSarabunNew.ttf')))
        pdfmetrics.registerFont(TTFont('seguisym', os.path.join(FONT_DIR, 'seguisym.ttf')))
    except Exception as e:
        print("ไม่สามารถโหลดฟอนต์ได้:", e)
        print(f"ตรวจสอบว่าไฟล์ .ttf อยู่ในโฟลเดอร์: {FONT_DIR}")
        return

    # === สร้างหน้า overlay สำหรับหน้าแรก ===
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)

    # วันที่ (แบบไทย)
    

    # วาดข้อความเฉพาะหน้าแรก
    draw_text(can, "บ้านพักเด็กและครอบครัว", 435, max_height-32) # เขียนที่
    draw_text(can, "12", 420, max_height-50) # วัน
    draw_text(can, "พฤศจิกายน", 450, max_height-50) # เดือน
    draw_text(can, "2566", 520, max_height-50) # ปี
    draw_text(can, "นายสมชาย ใจดี", 250, max_height-69) # ชื่อผู้รับบริการ
    draw_text(can, "35", 520, max_height-69) # อายุ
    draw_text(can, "ไทย", 75, max_height-88) # สัญชาติ
    draw_text(can, "ไทย", 160, max_height-88) # เชื้อชาติ
    draw_text(can, "พุทธ", 250, max_height-88) # ศาสนา
    draw_text(can, "ค้าขาย", 350, max_height-88) # อาชีพ
    draw_text(can, "10,000", 450, max_height-88) # รายได้
    draw_text(can, "120", 135, max_height-106) # บ้านเลขที่
    draw_text(can, "1", 200, max_height-106) # หมู่ที่
    draw_text(can, "ตำบลบ้านใหม่", 300, max_height-106) # ตำบล
    draw_text(can, "อำเภอเมือง", 480, max_height-106) # อำเภอ
    draw_text(can, "จังหวัดนนทบุรี", 75, max_height-125) # จังหวัด
    draw_text(can, "11110", 250, max_height-125) # รหัสไปรษณีย์
    draw_text(can, "064-1234567", 390, max_height-125) # เบอร์โทรศัพท์
    draw_text(can, "1102131231", 250, max_height-144) # เลขบัตรประชาชน
    draw_text(can, "1234567890123", 450, max_height-144) # เลขที่ใบเสร็จ
    draw_text(can, "สำนักงานอำเภอ", 75, max_height-162) # สถานที่ออกบัตรประชาชน
    draw_text(can, "12", 300, max_height-162) # วันออกบัตรประชาชน
    draw_text(can, "พฤศจิกายน", 370, max_height-162) # เดือนออกบัตรประชาชน
    draw_text(can, "2566", 470, max_height-162) # ปีออกบัตรประชาชน
    draw_text(can, "พ่อ", 75, max_height-181) # เกี่ยวข้องเป็น
    draw_text(can, "เด็กชายสมหมาย ใจดี", 300, max_height-181) # ชื่อเด็ก
    draw_text(can, "เด็กชายสมหมาย ใจดี", 250, max_height-200) # ชื่อคนที่2
    draw_text(can, "25", 520, max_height-200) # อายุคนที่2
    draw_text(can, "ไทย",75 ,  max_height -219) # สัญชาติคนที่2
    draw_text(can, "ไทย", 160, max_height-219) # เชื้อชาติคนที่2
    draw_text(can, "พุทธ", 250, max_height-219) # ศาสนา2
    draw_text(can, "ค้าขาย", 350, max_height-219) # อาชีพคนที่2
    draw_text(can, "10,000", 450, max_height-219) # รายได้คนที่2
    draw_text(can, "13", 130, max_height-237) # บ้านเลขที่คนที่2
    draw_text(can, "2", 200, max_height-237) # หมู่ที่คนที่2
    draw_text(can, "ตำบลบ้านใหม่", 300, max_height-237) # ตำบลคนที่2
    draw_text(can, "อำเภอเมือง", 480, max_height-237) # อำเภอคนที่2
    draw_text(can, "จังหวัดนนทบุรี", 75, max_height-255) # จังหวัดคนที่2
    draw_text(can, "11110", 250, max_height-255) # รหัสไปรษณีย์คนที่2
    draw_text(can, "064-1234567", 390, max_height-255) # เบอร์โทรศัพท์คนที่2
    draw_text(can, "1102131231", 265, max_height-274) # เลขบัตรประชาชนคนที่2
    draw_text(can, "1234567890123", 450, max_height-274) # เลขที่ใบเสร็จคนที่2
    draw_text(can, "สำนักงานอำเภอ", 80, max_height-293) # สถานที่ออกบัตรประชาชนคนที่2
    draw_text(can, "12", 300, max_height-293) # วันออกบัตรประชาชนคนที่2
    draw_text(can, "พฤศจิกายน", 370, max_height-293) # เดือนออกบัตรประชาชนคนที่2
    draw_text(can, "2566", 470, max_height-293) # ปีออกบัตรประชาชนคนที่2
    draw_text(can, "พ่อ", 75, max_height-312) # เกี่ยวข้องเป็นคนที่2
    draw_text(can, "เด็กชายสมหมาย ใจดี", 300, max_height-312) # ชื่อเด็กคนที่2
    draw_text(can, "เด็กชายสมหมาย ใจดี", 55, max_height -349) # เจ้าหน้าที่รับตัวเด็ก
    draw_text(can, "นายสมชาย ใจดี", 250, max_height-386) # มอบให้แก่ชื่อของผู้รับบริการ
    draw_text(can, "นายสมชาย ใจดี", 250, max_height-408) # มอบให้แก่ชื่อของผู้รับบริการคนที่2
    draw_text(can, "นายสมชาย ใจดี", 300, max_height-429) # มอบให้แก่ชื่อของผู้รับบริการคนที่3
    draw_text(can, "นายสมชาย ใจดี", 300, max_height-451) # มอบให้แก่ชื่อของผู้รับบริการคนที่4
    draw_text(can, "นายสมชาย ใจดี", 325, max_height-473) # มอบให้แก่ชื่อของผู้รับบริการคนที่5
    draw_text(can, "นายสมชาย ใจดี", 300, max_height-494) # มอบให้แก่ชื่อของผู้รับบริการคนที่6
    draw_text(can, "✔", 110, max_height-408, font="seguisym", size=16) # เช็คถูกคนที่2
    draw_text(can, "✔", 110, max_height-429, font="seguisym", size=16) # เช็คถูกคนที่3
    draw_text(can, "✔", 110, max_height-451, font="seguisym", size=16) # เช็คถูกคนที่4
    draw_text(can, "✔", 110, max_height-473, font="seguisym", size=16) # เช็คถูกคนที่5
    draw_text(can, "✔", 110, max_height-494, font="seguisym", size=16) # เช็คถูกคนที่6
    draw_text(can, "บ้านพักเด็ก", 460, max_height-512) # ออกบ้านพัก
    draw_text(can, "เด็กชายสมหมาย ใจดี", 70, max_height-605) # ลายเซ้นบิดาผู้มอบเด็ก
    draw_text(can, "เด็กชายสมหมาย ใจดี", 85, max_height-624) # ลายเซ้นมารดาผู้มอบเด็ก
    draw_text(can, "เด็กชายสมหมาย ใจดี", 70, max_height-642) # ลายเซ้นผู้มอบเด็กคนที่2
    draw_text(can, "เด็กชายสมหมาย ใจดี", 85, max_height-661) # ลายเซ้นผู้มอบเด็กคนที่3
    draw_text(can, "เด็กชายสมหมาย ใจดี", 70, max_height-680) # ลายเซ้นผู้มอบเด็กคนที่4
    draw_text(can, "เด็กชายสมหมาย ใจดี", 85, max_height-699) # ลายเซ้นผู้มอบเด็กคนที่5
    draw_text(can, "เด็กชายสมหมาย ใจดี", 70, max_height-717) # ลายเซ้นผู้มอบเด็กคนที่6
    draw_text(can, "เด็กชายสมหมาย ใจดี", 85, max_height-736) # ลายเซ้นผู้มอบเด็กคนที่7
    draw_text(can, "เด็กชายสมหมาย ใจดี", 390, max_height-605) # ลายเซ้นผู้มอบเด็กคนที่8
    draw_text(can, "เด็กชายสมหมาย ใจดี", 405, max_height-624) # ลายเซ้นผู้มอบเด็กคนที่9
    draw_text(can, "เด็กชายสมหมาย ใจดี", 390, max_height-680) # ลายเซ้นผู้มอบเด็กคนที่12
    draw_text(can, "เด็กชายสมหมาย ใจดี", 405, max_height-699) # ลายเซ้นผู้มอบเด็กคนที่13
    draw_text(can, "เด็กชายสมหมาย ใจดี", 390, max_height-717) # ลายเซ้นผู้มอบเด็กคนที่14
    draw_text(can, "เด็กชายสมหมาย ใจดี", 405, max_height-736) # ลายเซ้นผู้มอบเด็กคนที่15
                            
    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)

    # === เปิด PDF ต้นฉบับ ===
    try:
        existing_pdf = PdfReader(input_pdf_path)
    except FileNotFoundError:
        print(f"ไม่พบไฟล์ PDF ต้นฉบับ: {input_pdf_path}")
        return

    output = PdfWriter()

    # === ผสาน overlay กับหน้าแรก ===
    first_page = existing_pdf.pages[0]
    first_page.merge_page(new_pdf.pages[0])
    output.add_page(first_page)

    # === เพิ่มหน้าที่เหลือ ===
    for i in range(1, len(existing_pdf.pages)):
        output.add_page(existing_pdf.pages[i])

    # === เขียนออกเป็น PDF ใหม่ ===
    try:
        with open(output_pdf_path, "wb") as f:
            output.write(f)
        print(f"รีเซ็ตไฟล์ PDF แล้ว: {output_pdf_path}"),
        print (A4)
    except Exception as e:
        print("ไม่สามารถเขียนไฟล์ผลลัพธ์ได้:", e)

# === เรียกใช้ฟังก์ชัน ===
fill_doc4_form(input_pdf_path, output_pdf_path)
# === จบ ===