# SplitAndMergeMP3
`splitandmergemp3.py` is a Python script designed to split and merge MP3 files using FFMPEG.

## Language

[زبان فارسی](#فهرست-مطالب)
<br>
[English Language](#split-and-merge-mp3-1)






# Split and Merge MP3

## فهرست مطالب
1. [معرفی پروژه](#معرفی-پروژه)
2. [ویژگی‌ها](#ویژگیها)
3. [پیش‌نیازها](#پیشنیازها)
4. [نصب و راه‌اندازی](#نصب-و-راهاندازی)
5. [نحوه استفاده](#نحوه-استفاده)
    - [تقسیم یک فایل MP3](#1-تقسیم-یک-فایل-mp3)
    - [ادغام فایل‌های MP3 بر اساس نام فایل‌ها](#ادغام-فایل‌های-mp3-بر-اساس-نام-فایل‌ها)
    - [ادغام فایل‌های MP3 بر اساس نام پوشه](#ادغام-فایل‌های-mp3-بر-اساس-نام-پوشه)
6. [ساختار فایل‌ها](#ساختار-فایلها)
7. [جزئیات اسکریپت](#جزئیات-اسکریپت)
8. [موارد قابل بهبود](#موارد-قابل-بهبود)
9. [لایسنس](#لایسنس)

## معرفی پروژه

`splitandmergemp3.py` یک اسکریپت پایتون است که برای تقسیم و ادغام فایل‌های MP3 با استفاده از FFMPEG طراحی شده است. این اسکریپت می‌تواند یک فایل MP3 را به قطعات کوچکتر تقسیم کند یا فایل‌های MP3 موجود در یک پوشه را به یک فایل واحد ترکیب کند.



### **برنامه Python برای تقسیم و ادغام فایل‌های MP3**

`splitandmergemp3.py` یک اسکریپت پایتون است که برای تقسیم و ادغام فایل‌های MP3 با استفاده از FFMPEG طراحی شده است. این اسکریپت می‌تواند یک فایل MP3 را به قطعات کوچکتر تقسیم کند یا فایل‌های MP3 موجود در یک پوشه را به یک فایل واحد ترکیب کند.

---

### **ویژگی‌ها**

- **تقسیم فایل‌های MP3:** تقسیم یک فایل MP3 به قطعات کوچکتر براساس زمان‌های مشخص شده.
- **ادغام فایل‌های MP3 بر اساس نام پوشه:** ترکیب تمامی فایل‌های MP3 در یک پوشه به یک فایل با نام پوشه.
- **ادغام فایل‌های MP3 بر اساس پیشوند مشترک:** ترکیب فایل‌های MP3 با پیشوند نام مشترک به یک فایل واحد.

---

### **پیش‌نیازها**

1. **پایتون نسخه 3.6 یا بالاتر**
   - دانلود و نصب از [Python.org](https://www.python.org)
2. **FFMPEG**
   - ابزار خط فرمان برای پردازش داده‌های چندرسانه‌ای.
   - دانلود و نصب از [FFMPEG.org](https://ffmpeg.org/)
   - اطمینان حاصل کنید که پوشه `bin` مربوط به FFMPEG به متغیر محیطی `PATH` اضافه شده باشد.
   
---

### **نصب و راه‌اندازی**

1. **کلون کردن مخزن:**
   ```bash
   git clone https://github.com/mohammad021/SplitAndMergeMP3.git
   cd SplitAndMergeMP3
   ```

2. **تایید مسیرهای FFMPEG:**
   - اطمینان حاصل کنید که `ffmpeg.exe` و `ffprobe.exe` در مسیر `C:\ffmpeg\bin` قرار دارند یا مسیر صحیح را در هنگام اجرای اسکریپت وارد کنید.

---

### **نحوه استفاده**

#### **1. تقسیم یک فایل MP3:**

   استفاده از دستور `split` به همراه نام فایل و بازه‌های زمانی:
   ```bash
   python splitandmergemp3.py split input.mp3 1:00 2:00
   ```
   - **مثال:** این دستور فایل `input.mp3` را به قطعات 1 دقیقه و 2 دقیقه تقسیم می‌کند.

#### **2. ادغام فایل‌های MP3 بر اساس نام فایل‌ها:**

   استفاده از دستور `mergefiles` برای ادغام فایل‌های MP3 بر اساس پیشوند مشترک نام‌ها در دایرکتوری جاری:
   ```bash
   python splitandmergemp3.py mergefiles
   ```

#### **3. ادغام فایل‌های MP3 بر اساس نام پوشه:**

   استفاده از دستور `mergefolder` برای ادغام تمامی فایل‌های MP3 در پوشه جاری:
   ```bash
   python splitandmergemp3.py mergefolder
   ```

---

### **ساختار فایل‌ها**

اطمینان حاصل کنید که فایل‌های MP3 شما به شکل زیر سازماندهی شده‌اند (فرض می‌کنیم که شما بر اساس نام پوشه ادغام می‌کنید):

```
FolderName/
├── part1.mp3
├── part2.mp3
├── part3.mp3
```

- فایل‌های MP3 در پوشه باید نام‌هایی داشته باشند که با استراتژی ادغام همخوانی داشته باشند (یا پیشوند مشترک یا بر اساس نام پوشه).

---

### **جزئیات اسکریپت**

1. **get_ffmpeg_paths:**
   - از کاربر مسیر نصب FFMPEG را در صورت عدم وجود مسیر پیش‌فرض درخواست می‌کند.

2. **check_ffmpeg_paths:**
   - بررسی می‌کند که آیا مسیرهای پیش‌فرض برای `ffmpeg.exe` و `ffprobe.exe` وجود دارند یا خیر.

3. **time_to_seconds:**
   - تبدیل فرمت زمانی (دقیقه:ثانیه) به ثانیه.

4. **split_mp3:**
   - تقسیم یک فایل MP3 به قطعات زمانی مشخص شده و ذخیره آن‌ها در یک پوشه با نام فایل ورودی.

5. **concatenate_mp3_folder:**
   - ادغام تمامی فایل‌های MP3 در یک پوشه به یک فایل با نام پوشه.

6. **concatenate_mp3_files:**
   - ادغام فایل‌های MP3 با پیشوند مشترک در نام‌ها به یک فایل واحد.

---

### **موارد قابل بهبود**

- **پشتیبانی از فرمت‌های اضافی:** اضافه کردن پشتیبانی از فرمت‌های دیگر مانند `.wav` یا `.flac` با تغییرات جزئی.
- **آرگومان‌های خط فرمان برای مسیرها:** امکان تنظیم مسیرهای ورودی و خروجی از طریق آرگومان‌های خط فرمان.
- **گزارش خطا:** پیاده‌سازی لاگ‌ها برای ذخیره خطاها در یک فایل جداگانه برای رفع اشکال آسان‌تر.

---

### **لایسنس**

این پروژه تحت لایسنس MIT منتشر می‌شود.

---


# Split and Merge MP3

## Table of Contents
1. [Project Introduction](#project-introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation and Setup](#installation-and-setup)
5. [Usage](#usage)
    - [Splitting an MP3 File](#splitting-an-mp3-file)
    - [Merging MP3 Files by File Names](#merging-mp3-files-by-file-names)
    - [Merging MP3 Files by Folder Name](#merging-mp3-files-by-folder-name)
6. [File Structure](#file-structure)
7. [Script Details](#script-details)
8. [Possible Improvements](#possible-improvements)
9. [License](#license)

## Project Introduction

`splitandmergemp3.py` is a Python script designed to split and merge MP3 files using FFMPEG. This script can either split a single MP3 file into smaller segments or merge multiple MP3 files within a folder into one consolidated file.



### **Split and Merge MP3: A Python Script for Audio File Manipulation**

`splitandmergemp3.py` is a Python script designed to split and merge MP3 files using FFMPEG. This script can either split a single MP3 file into smaller segments or merge multiple MP3 files within a folder into one consolidated file.

---

### **Features**

- **Split MP3 Files:** Divide an MP3 file into smaller segments based on specified time intervals.
- **Merge MP3 Files by Folder Name:** Combine all MP3 files within a folder into a single file named after the folder.
- **Merge MP3 Files by Common Prefix:** Combine MP3 files with common prefix names into a single file.

---

### **Prerequisites**

1. **Python 3.6 or higher**
   - Download and install from [Python.org](https://www.python.org)
2. **FFMPEG**
   - Command-line tool for handling multimedia data.
   - Download and install from [FFMPEG.org](https://ffmpeg.org/)
   - Ensure the `bin` directory of FFMPEG is added to your `PATH` environment variable.
   
---

### **Installation and Setup**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mohammad021/SplitAndMergeMP3.git
   cd SplitAndMergeMP3
   ```

2. **Verify FFMPEG Paths:**
   - Ensure that `ffmpeg.exe` and `ffprobe.exe` are located in the `C:\ffmpeg\bin` directory, or provide the correct path during the script execution.

---

### **Usage**

#### **1. Splitting an MP3 File:**

   Use the `split` command followed by the file name and time intervals:
   ```bash
   python splitandmergemp3.py split input.mp3 1:00 2:00
   ```
   - **Example:** This command will split `input.mp3` into segments of 1 minute and 2 minutes respectively.

#### **2. Merging MP3 Files by File Names:**

   Use the `mergefiles` command to merge MP3 files based on their common prefix names in the current directory:
   ```bash
   python splitandmergemp3.py mergefiles
   ```

#### **3. Merging MP3 Files by Folder Name:**

   Use the `mergefolder` command to merge all MP3 files within the current folder:
   ```bash
   python splitandmergemp3.py mergefolder
   ```

---

### **File Structure**

Ensure your MP3 files are organized in the following structure (assuming you are merging by folder name):

```
FolderName/
├── part1.mp3
├── part2.mp3
├── part3.mp3
```

- MP3 files within the folder should have names that align with the merging strategy (either common prefix or by folder name).

---

### **Script Details**

1. **get_ffmpeg_paths:**
   - Prompts the user for the FFMPEG installation path if the default path is not valid.

2. **check_ffmpeg_paths:**
   - Checks if the default paths for `ffmpeg.exe` and `ffprobe.exe` exist.

3. **time_to_seconds:**
   - Converts a time format (`minutes:seconds`) into seconds.

4. **split_mp3:**
   - Splits an MP3 file into specified time segments and saves them in a folder named after the input file.

5. **concatenate_mp3_folder:**
   - Merges all MP3 files within a specified folder into one file named after the folder.

6. **concatenate_mp3_files:**
   - Merges MP3 files with a common prefix in their names into a single file.

---

### **Possible Improvements**

- **Additional Format Support:** Add support for other audio formats like `.wav` or `.flac` with minor modifications.
- **Command-line Arguments for Paths:** Allow setting input and output paths via command-line arguments.
- **Error Logging:** Implement logging to save errors in a separate file for easier debugging.

---

### **License**

This project is released under the MIT License.

---


