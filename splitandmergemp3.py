import os
import sys
import subprocess

# مسیر پیش‌فرض FFmpeg و FFprobe
DEFAULT_FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"
DEFAULT_FFPROBE_PATH = r"C:\ffmpeg\bin\ffprobe.exe"

def get_ffmpeg_paths():
    """درخواست مسیر FFmpeg از کاربر در صورت عدم وجود در مسیر پیش‌فرض"""
    ffmpeg_path = input("لطفاً مسیر پوشه روت FFmpeg را وارد کنید (مثال: C:\\ffmpeg): ").strip()
    ffmpeg_exe = os.path.join(ffmpeg_path, "bin", "ffmpeg.exe")
    ffprobe_exe = os.path.join(ffmpeg_path, "bin", "ffprobe.exe")
    
    if not os.path.exists(ffmpeg_exe) or not os.path.exists(ffprobe_exe):
        print("مسیرهای FFmpeg اشتباه هستند یا فایل‌ها یافت نشدند.")
        sys.exit(1)
    
    return ffmpeg_exe, ffprobe_exe

def check_ffmpeg_paths():
    """بررسی مسیرهای FFmpeg"""
    if not os.path.exists(DEFAULT_FFMPEG_PATH) or not os.path.exists(DEFAULT_FFPROBE_PATH):
        return False
    return True

def time_to_seconds(time_str):
    """تبدیل فرمت زمانی (مثل '1:00') به ثانیه"""
    try:
        time_parts = time_str.split(':')
        minutes = int(time_parts[0])
        seconds = int(time_parts[1])
        return minutes * 60 + seconds
    except:
        print(f"خطا در فرمت زمانی {time_str}")
        sys.exit(1)

def split_mp3(ffmpeg_path, ffprobe_path, input_file, time_segments):
    """تقسیم فایل MP3 به قطعات مشخص شده با استفاده از FFmpeg"""
    try:
        # ایجاد پوشه با نام فایل
        folder_name = os.path.splitext(os.path.basename(input_file))[0]
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        # تبدیل زمان‌ها به ثانیه
        segments_seconds = [time_to_seconds(t) for t in time_segments]
        
        # دریافت مدت زمان کل فایل
        duration_cmd = [ffprobe_path, '-i', input_file, '-show_entries', 
                       'format=duration', '-v', 'quiet', '-of', 'csv=p=0']
        total_duration = float(subprocess.check_output(duration_cmd).decode().strip())
        
        # محاسبه زمان باقی‌مانده
        total_segments_time = sum(segments_seconds)
        remaining_time = total_duration - total_segments_time
        
        if remaining_time > 0:
            segments_seconds.append(remaining_time)
            print(f"زمان باقی‌مانده: {remaining_time:.2f} ثانیه")
        
        # برش و ذخیره قطعات
        current_position = 0
        for i, duration in enumerate(segments_seconds, 1):
            print(f"در حال پردازش قطعه {i}...")
            output_path = os.path.join(folder_name, f"part_{i}.mp3")
            
            cmd = [
                ffmpeg_path,
                '-i', input_file,
                '-ss', str(current_position),
                '-t', str(duration),
                '-acodec', 'copy',
                '-y',
                output_path
            ]
            
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"قطعه {i} ذخیره شد: {output_path}")
            current_position += duration
            
    except Exception as e:
        print(f"خطا در پردازش فایل: {str(e)}")
        sys.exit(1)

def concatenate_mp3_folder(ffmpeg_path, folder_path):
    """ترکیب فایل‌های MP3 در یک پوشه به یک فایل واحد با نام پوشه"""
    try:
        # یافتن تمامی فایل‌های MP3 در پوشه
        mp3_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]
        
        if not mp3_files:
            print("هیچ فایل MP3 در پوشه موجود نیست.")
            return
        
        # استخراج نام پوشه به عنوان نام فایل خروجی
        folder_name = os.path.basename(folder_path)
        output_file = os.path.join(folder_path, f"{folder_name}.mp3")
        
        # ایجاد فایل متنی شامل مسیر فایل‌های ورودی
        with open("file_list.txt", "w") as file_list:
            for file in mp3_files:
                file_list.write(f"file '{os.path.join(folder_path, file)}'\n")
        
        # اجرای فرمان FFmpeg برای چسباندن فایل‌ها
        cmd = [
            ffmpeg_path,
            '-f', 'concat',
            '-safe', '0',
            '-i', 'file_list.txt',
            '-c', 'copy',
            output_file
        ]
        
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"فایل‌ها با موفقیت ترکیب شدند: {output_file}")
        
    except Exception as e:
        print(f"خطا در ترکیب فایل‌ها: {str(e)}")

def concatenate_mp3_files(ffmpeg_path, folder_path):
    """ترکیب فایل‌های MP3 در یک پوشه به یک فایل واحد با نام دلخواه"""
    try:
        # یافتن تمامی فایل‌های MP3 در پوشه
        mp3_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]
        
        if not mp3_files:
            print("هیچ فایل MP3 در پوشه موجود نیست.")
            return
        
        # استخراج قسمت مشترک نام فایل‌ها
        common_prefix = os.path.commonprefix(mp3_files)
        common_prefix = common_prefix.rstrip('0123456789_')  # حذف اعداد و آندرلاین در انتهای پیشوند مشترک
        output_file = os.path.join(folder_path, f"{common_prefix}.mp3")
        
        # ایجاد فایل متنی شامل مسیر فایل‌های ورودی
        with open("file_list.txt", "w") as file_list:
            for file in mp3_files:
                file_list.write(f"file '{os.path.join(folder_path, file)}'\n")
        
        # اجرای فرمان FFmpeg برای چسباندن فایل‌ها
        cmd = [
            ffmpeg_path,
            '-f', 'concat',
            '-safe', '0',
            '-i', 'file_list.txt',
            '-c', 'copy',
            output_file
        ]
        
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"فایل‌ها با موفقیت ترکیب شدند: {output_file}")
        
    except Exception as e:
        print(f"خطا در ترکیب فایل‌ها: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("استفاده:")
        print("چند تکه کردن فایل mp3:")
        print("python splitandmergemp3.py split input.mp3 1:00 2:00")
        print("یکی کردن بر اساس نام فایل های داخل پوشه mp3:")
        print("python splitandmergemp3.py mergefiles")
        print("یکی کردن بر اساس نام پوشه محتوی فایل mp3:")
        print("python splitandmergemp3.py mergefolder")
        sys.exit(1)
    
    ffmpeg_path, ffprobe_path = (DEFAULT_FFMPEG_PATH, DEFAULT_FFPROBE_PATH) if check_ffmpeg_paths() else get_ffmpeg_paths()
    
    command = sys.argv[1].lower()
    
    if command == 'split':
        input_file = sys.argv[2]
        time_segments = sys.argv[3:]
        if not os.path.exists(input_file):
            print(f"فایل {input_file} یافت نشد!")
            sys.exit(1)
        split_mp3(ffmpeg_path, ffprobe_path, input_file, time_segments)
    elif command == 'mergefiles':
        folder_path = os.getcwd()
        concatenate_mp3_files(ffmpeg_path, folder_path)
    elif command == 'mergefolder':
        folder_path = os.getcwd()
        concatenate_mp3_folder(ffmpeg_path, folder_path)
    else:
        print(f"دستور ناشناخته: {command}")
        print("دستورات موجود: split, mergefiles, mergefolder")
        sys.exit(1)
