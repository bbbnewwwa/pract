import os
import shutil
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / 'db.sqlite3'
BACKUP_DIR = BASE_DIR / 'backups'

BACKUP_DIR.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"db_backup_{timestamp}.sqlite3"
backup_path = BACKUP_DIR / backup_filename

shutil.copy(DB_PATH, backup_path)
print(f"Резервная копия создана: {backup_path}")