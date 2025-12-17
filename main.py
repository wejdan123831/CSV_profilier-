import json
import csv
from pathlib import Path

# تأكد أن هذا هو المكان الذي وضعت فيه الملف الموجود في الصورة
CSV_PATH = Path(r"C:\Users\w\Documents\AI camp\saudi_shopping_with_missing.csv")

def get_data_type(value):
    val = value.strip()
    if not val: return None
    try:
        # محاولة التحويل لرقم
        float(val)
        return "number"
    except ValueError:
        return "string"

def is_missing(value: str | None) -> bool:
    if value is None: return True
    val = value.strip().lower()
    blacklist = ["", "na", "n/a", "null", "none", "nan"]
    return val in blacklist

def generate_profile():
    # 1. التحقق من وجود الملف
    if not CSV_PATH.exists():
        print(f"❌ خطأ: الملف غير موجود في {CSV_PATH}")
        return

    report = {"rows": 0, "columns": {}}

    with open(CSV_PATH, mode='r', encoding='utf-8') as file:
        # 2. فحص أول سطر للتأكد أنه ليس تقرير Markdown
        first_line = file.readline()
        if first_line.startswith("# Project"):
            print("🛑 تنبيه خطير: الملف الذي تحاول قراءته هو ملف تقرير وليس ملف بيانات CSV!")
            print("يبدو أنك قمت بحفظ التقرير داخل ملف البيانات الأصلي بالخطأ.")
            return
        
        # العودة لبداية الملف للقراءة بـ DictReader
        file.seek(0)
        reader = csv.DictReader(file)
        headers = reader.fieldnames 

        if not headers:
            print("❌ خطأ: لا توجد رؤوس أعمدة في الملف.")
            return

        for h in headers:
            report["columns"][h] = {"missing": 0, "type": "number", "_temp_types": set()} 

        for row in reader:
            report["rows"] += 1
            for h in headers:  
                val = row[h]
                if is_missing(val):
                    report["columns"][h]["missing"] += 1
                else: 
                    # نسجل كل الأنواع التي تظهر في العمود
                    dtype = get_data_type(val)
                    if dtype:
                        report["columns"][h]["_temp_types"].add(dtype)

    # تحديد النوع النهائي لكل عمود
    for h in headers:
        types = report["columns"][h].pop("_temp_types")
        if "string" in types:
            report["columns"][h]["type"] = "string"
        elif "number" in types:
            report["columns"][h]["type"] = "number"
        else:
            report["columns"][h]["type"] = "unknown"

    # 3. حفظ النتائج بأسماء واضحة جداً بعيداً عن ملف البيانات
    with open("final_data_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    with open("final_data_report.md", "w", encoding="utf-8") as f:
        f.write("# Project Data Profile Report\n\n")
        f.write(f"**Total Rows:** {report['rows']}\n\n")
        f.write("| Column Name | Missing Values | Data Type |\n")
        f.write("| :--- | :--- | :--- |\n")
        for col, info in report["columns"].items():
            f.write(f"| {col} | {info['missing']} | {info['type']} |\n")

    print(f"✅ تم بنجاح! الملفات الناتجة: final_data_report.json و final_data_report.md")

if __name__ == "__main__":
    generate_profile()