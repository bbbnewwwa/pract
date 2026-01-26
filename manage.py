"""Django's command-line utility for administrative tasks."""
import os
import sys
import os
from pathlib import Path

LOGS_DIR = Path(__file__).resolve().parent / 'beauty_studio' / 'logs'
LOGS_DIR.mkdir(exist_ok=True)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beauty_studio.mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django." 
            "Вы уверены, что он установлен и доступен в переменной окружения PYTHONPATH?" 
            "Может быть, вы забыли активировать виртуальное окружение?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
