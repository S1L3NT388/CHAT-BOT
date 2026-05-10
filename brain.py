import google.generativeai as genai
from config import GEMINI_KEY

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=(
        "Ти — експерт ритм-гри Project Sekai. Твоя роль: допомагати гравцям. "
        "Якщо пишуть назву пісні — дай рівні Expert/Master та поради по проходженню. "
        "Спілкуйся природно, як бро, українською. Уникай символів * та #."
    )
)

async def get_ai_answer(user_text: str):
    try:
        # Формуємо запит з контекстом (Етап 1: Правило мікро-ніші)
        prompt = f"Запит гравця про Project Sekai: {user_text}"
        response = await model.generate_content_async(prompt)
        
        # Очищення тексту (Етап 2: Data Flow)
        return response.text.replace("*", "").replace("#", "")
    except Exception as e:
        return f"Бро, виникла помилка в системі ШІ: {e}"