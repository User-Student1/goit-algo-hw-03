import argparse
import os
import shutil
import sys
import tkinter as tk
from tkinter import filedialog

def recursive_copy(scr_dir, dst_dir):
    """
    Рекурсивна функція, яка ходить по всіх папках і файлах.
    Якщо знаходить файл - копіює його у відповідну папку за розширенням
    """

    try:
        items = os.listdir(scr_dir)
    except PermissionError:
        print(f"Немає доступу до {scr_dir}")
        return
    except FileNotFoundError:
        print(f"Папку не знайдена: {scr_dir}")
        return
    
    for item in items:
        full_item_path = os.path.join(scr_dir, item)

        if os.path.isdir(full_item_path):
            recursive_copy(full_item_path, dst_dir)
        
        else:
            file_ext = os.path.splitext(item)[1][1:].lower()
            if file_ext == "":
                file_ext = "no_extension"

            target_dir = os.path.join(dst_dir, file_ext)
            os.makedirs(target_dir, exist_ok=True)


            target_file_path = os.path.join(target_dir, item)

            try:
                shutil.copy2(full_item_path, target_file_path)
                print(f"Скопійовано: {full_item_path} -> {target_file_path}")
            except Exception as e:
                print(f"Помилка копіювання {item}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів")
    parser.add_argument("source", nargs="?", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії прихначення (за замовчуванням dist)")
    args = parser.parse_args()

    if args.source is None:
        root = tk.Tk()
        root.withdraw()
        scr = filedialog.askdirectory(title="Виберіть папку для сортування")
        if not scr:
            print("Папка не вибрана. Вихід з програми.")
            sys.exit(0)

    else:
        scr = args.source

    if not os.path.exists(scr) or not os.path.isdir(scr):
        print(f"Помилка: директорія '{scr}' не існує або це не папка.")
        sys.exit(0)
    
    dst = args.destination
    os.makedirs(dst,exist_ok=True)

    recursive_copy(scr, dst)

if __name__ == "__main__":
    main()