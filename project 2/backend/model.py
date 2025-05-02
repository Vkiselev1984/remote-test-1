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

        # Проверяем наличие файла, если нет — создаём пустой список
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=4)

        # Добавляем данные в JSON-файл
        try:
            with open(self.data_file, 'r+', encoding='utf-8') as f:
                try:
                    file_data = json.load(f)
                except json.JSONDecodeError:
                    # Если файл пустой или повреждён — начинаем с пустого списка
                    file_data = []
                file_data.append(data)
                f.seek(0)
                json.dump(file_data, f, ensure_ascii=False, indent=4)
                f.truncate()  # Обрезаем файл, если новые данные короче старых
        except Exception as e:
            print(f"Ошибка при работе с файлом: {e}")
            return False

        # Git-логика:
        branch_name = f"user-{uuid.uuid4().hex[:8]}"  # Короткий уникальный идентификатор
        try:
            # Создаём и переключаемся на новую ветку
            subprocess.run(["git", "checkout", "-b", branch_name], check=True)

            # Добавляем изменения
            subprocess.run(["git", "add", self.data_file], check=True)

            # Делаем коммит
            commit_message = f"Добавлены данные пользователя: {user_data.get('email', 'unknown')}"
            subprocess.run(["git", "commit", "-m", commit_message], check=True)

            # Отправляем изменения в удалённый репозиторий
            subprocess.run(["git", "push", "-u", "origin", branch_name], check=True)

        except subprocess.CalledProcessError as e:
            print(f"Ошибка при работе с Git: {e}")

        finally:
            # Переключаемся обратно на ветку main
            try:
                subprocess.run(["git", "checkout", "main"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Ошибка при переключении на ветку main: {e}")

        return True