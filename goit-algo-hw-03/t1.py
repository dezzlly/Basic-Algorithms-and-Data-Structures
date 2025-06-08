# модуль для парсинга аргументов из командной строки
import argparse
# класс для работы с путями как объектами
from pathlib import Path
# модуль для работы с файлами и копирования
import shutil


# Создаётся объект парсера. Аргумент description — это описание, которое выводится при запуске с флагом --help
parser = argparse.ArgumentParser(description="Копирует файлы по расширениям в целевую папку.")
# Первый обязательный аргумент, help — пояснение, которое также отображается в справке
parser.add_argument("source", help="Путь к исходной директории")
# Второй необязательный аргумент, если он не передан — будет использовано значение default="dist"
parser.add_argument("destination", nargs="?", default="dist", help="Путь к целевой директории (по умолчанию: dist)")

# Считываются аргументы, переданные при запуске скрипта, и сохраняются в объект args
# python script.py ./input ./output
# args.source      # './input'
# args.destination # './output'
args = parser.parse_args()

# Эти строки превращают строки в объекты Path, с которыми можно удобно работать: проверять, создавать, соединять пути
source_dir = Path(args.source)
destination_dir = Path(args.destination)


def bypass_directory(path: Path):
    try:
        # path.iterdir() возвращает все элементы (файлы и папки) внутри директории path
        for element in path.iterdir():
            if element.is_dir():
                bypass_directory(element)
            if element.is_file():
                copy_file(element)
    
    except Exception as e:
        print(f"Ошибка при доступе к {path}: {e}")


def copy_file(file: Path):
    # file.suffix возвращает расширение (например, .txt). [1:] убирает точку → будет просто txt
    ext = file.suffix[1:]
    if not ext:
        # Если файл без расширения, присваивается no_extension
        ext = "no_extension"

    # Создаётся путь к целевой подпапке, например: dist/txt
    target_folder = destination_dir / ext
    # Создаёт эту папку (и родительские, если надо). Не вызывает ошибку, если она уже существует
    target_folder.mkdir(parents=True, exist_ok=True)

    # Копирует файл в эту папку, сохраняя метаданные (дату создания и т.п.)
    shutil.copy2(file, target_folder / file.name)


bypass_directory(source_dir)