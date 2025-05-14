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
input_pdf_path = os.path.join(BASE_DIR, "บันทึกข้อความ.pdf")
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

    # กำหนดพิกัดสูงสุดของหน้า
    max_height = 790
    

    # วาดข้อความเฉพาะหน้าแรก
    draw_text(can, "กองกลาง สำนักงานอธิการบดี", 140, max_height-60) # ชื่อสำนักงาน
    draw_text(can, "๐๖๔ ๓๑๙๙๘๔/ ๑๔๒๐๐", 280, max_height-60) # เบอร์สำนักงาน
    draw_text(can, "ศธ ๐๕๘๔/๑๖", 100, max_height-86)# ที่
    draw_text(can, "๔ กรฏาคม ๒๕๕๗", 320, max_height-86) # วันที่
    draw_text(can, "แจ้งตัดกระแสไฟฟ้สชั่วคราว", 100, max_height-113) # เรื่อง
    draw_text(can, "เรียน หัวหน้าหน่วยงานในสังกัดวิทยาลัยเทคโนโลยีราชมงคลศรีวิชัย", 75, max_height-137) # เนื้อความ
    draw_text(can, "ด้วย สำนักงานการไฟฟ้าส่วนภูมิภาค เขต ๓ (ภาคใต้) จังหวัดยะลา จะดำเนินการบำรุงรักษาระบบ", 112, max_height-161) # เนื้อความ
    draw_text(can, "ไฟฟ้าแรงสูง โดยการตัดกระแสไฟฟ้าชั่วคราว เพื่อป้องกันอันตรายจากการทำงาน", 75, max_height-185) # เนื้อความ
    draw_text(can, "กองกลาง จึงขอเรียนให้ทราบว่า การไฟฟ้าส่วนภูมิภาคฯ จะดำเนินการตัดกระแสไฟฟ้าชั่วคราว ใน", 112, max_height-209) # เนื้อความ
    draw_text(can, "ระหว่างวันที่ ๗-๑๐ กรกฎาคม ๒๕๕๗ เวลา ๐๘.๓๐-๑๖.๓๐ น.", 75, max_height-232)
    draw_text(can, "จึงขอให้หน่วยงานของท่านดำเนินการแจ้งผู้ที่เกี่ยวข้องทราบโดยทั่วกัน ตามรายละเอียดดังแนบ", 75, max_height-256) # เนื้อความ
    # draw_text(can, "ผู้ช่วยศาสตราจารย์ปิยวิทย์ สุวรรณ", 330, max_height-375) #ลายเซ้น
    # draw_text(can, "รักษาราชการแทน ผู้อำนวยการกองกลาง", 320, max_height-399) #ลายเซ้น

                            
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