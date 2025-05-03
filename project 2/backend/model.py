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

        # We check the presence of the file, if not, we create an empty list
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=4)

        # Adding data to a JSON file
        try:
            with open(self.data_file, 'r+', encoding='utf-8') as f:
                try:
                    file_data = json.load(f)
                except json.JSONDecodeError:
                    # If the file is empty or damaged, we start with an empty list
                    file_data = []
                file_data.append(data)
                f.seek(0)
                json.dump(file_data, f, ensure_ascii=False, indent=4)
                f.truncate()  # We truncate the file if the new data is shorter than the old data
        except Exception as e:
            print(f"Ошибка при работе с файлом: {e}")
            return False

        # Git logic:
        branch_name = f"user-{uuid.uuid4().hex[:8]}"  # Short unique identifier
        try:
            # Create and switch to a new branch
            subprocess.run(["git", "checkout", "-b", branch_name], check=True)

            # Adding changes
            subprocess.run(["git", "add", self.data_file], check=True)

            # Let's make a commit
            commit_message = f"User data added: {user_data.get('email', 'unknown')}"
            subprocess.run(["git", "commit", "-m", commit_message], check=True)

            # Sending changes to the remote repository
            subprocess.run(["git", "push", "-u", "origin", branch_name], check=True)

        except subprocess.CalledProcessError as e:
            print(f"Error while working with Git: {e}")

        finally:
            # Switch back to the main branch
            try:
                subprocess.run(["git", "checkout", "main"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error when switching to main branch: {e}")

        return True