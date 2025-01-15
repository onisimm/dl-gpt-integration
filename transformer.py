from langchain_openai import ChatOpenAI

class TransformerModel:
    def __init__(self, api_key):
        self.model = ChatOpenAI(
            model="gpt-4o",  # or "gpt-4o" for GPT-4o
            temperature=1,
            max_retries=2,
            api_key=api_key 
        )

    def generate_response(self, chat_history: list) -> str:
        messages = [(msg["role"], msg["content"]) for msg in chat_history]

        ai_msg = self.model.invoke(messages)
        
        return ai_msg.content
\