# 🎹 Sekai Coach AI

**Sekai Coach AI** — це розумний Telegram-бот для гравців ритм-гри *Project Sekai: Colorful Stage!*. Він працює як персональний ШІ-коуч, допомагаючи гравцям аналізувати треки та готуватися до проходження на рівнях складності Expert та Master.

---

## 🚀 Проблема та концепція (System Idea)

Гравці часто витрачають час на рутинний пошук характеристик пісень та гайдів. 
- **Рішення:** Використання LLM для миттєвої генерації технічних порад та аналітики.
- **Мікро-ніша:** Ритм-геймінг та автоматизація ігрового досвіду.

## 🛠 Технологічний стек

- **Language:** Python 3.10+
- **Framework:** [Aiogram 3.x](https://docs.aiogram.dev/) (Asynchronous Telegram API)
- **AI Engine:** [Google Gemini 2.5 Flash Lite](https://aistudio.google.com/)
- **Configuration:** Python-dotenv

## 🏗 Архітектура (System Design)

Проєкт побудований за принципом **модульності**, що дозволяє легко масштабувати систему:

1.  **Main Module (`main.py`):** Обробка вхідних повідомлень (Handlers) та управління станом (FSM).
2.  **AI Engine (`brain.py`):** Логіка взаємодії з API Gemini, налаштування системного промпту та обробка відповідей.
3.  **Config (`config.py`):** Безпечне управління ключами доступу та конфігураціями середовища.

---

## ⚙️ Встановлення та запуск

1.    ```bash
   git clone [https://github.com/your-username/sekai-coach-ai.git](https://github.com/your-username/sekai-coach-ai.git)
   cd sekai-coach-ai
   Встановіть залежності:

2. pip install aiogram google-generativeai python-dotenv
3. Створіть файл `.env` у корені проєкту:
   ```env
   BOT_TOKEN=ваш_токен_від_BotFather
   GEMINI_KEY=ваш_api_key_від_Google_AI
   ADMIN_ID=ваш_telegram_id
4. Запустіть бота py main.py

---

## 🕹 Функціонал

- ✅ **Аналіз пісень:** Просто напишіть назву треку, і ШІ видасть рівні складності та поради по механікам (фліки, спам нот, зажимки).
- ✅ **Натуральний діалог:** Бот спілкується українською мовою у дружньому стилі.
- ✅ **Admin Stop:** Функція безпечного вимкнення бота безпосередньо з Telegram (команда `/stop`).

   
