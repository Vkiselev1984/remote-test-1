from flask import render_template

class UserView:
    @staticmethod
    def form():
        return render_template('index.html')

    @staticmethod
    def success():
        return "<h3>Данные успешно отправлены!</h3>"