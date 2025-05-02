import json
import os
import subprocess
import uuid
from datetime import datetime

class UserModel:
    def __init__(self, config):
        self.data_file = config['data_file']

    def save_user(self, user_data):
        data = {
            "user": user_data,
            "timestamp": datetime.now().isoformat()
        }

        # Проверяем наличие файла, если нет — создаем пустой список
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=4)

        # Добавляем данные в JSON-файл
        with open(self.data_file, 'r+', encoding='utf-8') as f:
            file_data = json.load(f)
            file_data.append(data)
            f.seek(0)
            json.dump(file_data, f, ensure_ascii=False, indent=4)

        # Git логика:
        branch_name = f"user-{uuid.uuid4().hex[:8]}"  # Короткий уникальный идентификатор
        try:
            # Создаем и переключаемся на новую ветку
            subprocess.run(["git", "checkout", "-b", branch_name], check=True)

            # Добавляем изменения
            subprocess.run(["git", "add", self.data_file], check=True)

            # Делаем коммит
            commit_message = f"Добавлены данные пользователя: {user_data['email']}"
            subprocess.run(["git", "commit", "-m", commit_message], check=True)

            # Отправляем изменения в удаленный репозиторий
            subprocess.run(["git", "push", "-u", "origin", branch_name], check=True)

        except subprocess.CalledProcessError as e:
            print(f"Ошибка при работе с Git: {e}")

        finally:
            # Переключаемся обратно на main ветку
            subprocess.run(["git", "checkout", "main"], check=True)