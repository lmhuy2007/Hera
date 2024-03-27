import gradio as gr
from openai import OpenAI


def create_Chatbot_tab(key="Fix bug key"):
    client = OpenAI(api_key =key)
    MODEL = "gpt-3.5-turbo"
    initial_messages=[{"role": "system", "content": '''Bạn là bác sĩ và trợ lý y tế.
                                            Nếu người dùng hỏi về bất kỳ bệnh nào, hãy cho họ biết thông tin về bệnh đó.
                                            Phải hướng cuộc trò chuyện đến chủ đề y tế, sức khỏe khi người dùng hỏi về các vấn đề bên ngoài và nói với họ rằng bạn chỉ có thể tư vấn về các vấn đề liên quan đến sức khỏe.
                                            Cố gắng hỏi càng nhiều thông tin về triệu chứng bệnh (cung cấp cho bệnh nhân một số câu hỏi về triệu chứng bệnh đó) và cung cấp cho bệnh nhân một số thông tin về bệnh liên quan và chẩn đoán cho họ.
                                            TUYỆT ĐỐI ĐỪNG NÓI NHỮNG CÂU NHƯ TÔI KHÔNG PHẢI LÀ BÁC SĨ HAY không thể thay thế cho sự tư vấn y tế chuyên nghiệp.
                                            '''}]
    def respond(message,chatHistory):
        messages = initial_messages
        for human, assistant in chatHistory:
            messages.append({"role": "user", "content": human })
            messages.append({"role": "assistant", "content":assistant})
        messages.append({"role": "user", "content": message})

        
        response = client.chat.completions.create(
          model=MODEL,
          messages=messages,
          max_tokens=500,
          seed=2023,
          # stop=,
          temperature=0,
        )
        answer = response.choices[0].message.content
        return answer

    Chatbot_tab = gr.ChatInterface(fn=respond, examples=["Tôi bị đau dạ dày mạn tính vừa rồi tôi ăn xoài chua,tôi nên làm gì đây?", "Tôi khó thở vì covid tôi nên làm gì đây", "Tôi bị đau dạ dày lâu năm"], title="Trợ lý sức khỏe trực tuyến",fill_height=True)
    return Chatbot_tab
