from fastapi import FastAPI, HTTPException
from models import PromptRequest
from gemini_ai import gemini_ai_client
from open_ai import open_ai_client

app = FastAPI()
gemini_ai_client()
open_ai_client()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/ask-gemini")
async def ask(body: PromptRequest):
    try:
      model = gemini_ai_client().GenerativeModel("gemini-1.5-flash")
      response = model.generate_content(body.prompt)
      print(response.text)
      ai_message = response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": ai_message}

@app.post("/ask-openai")
async def ask(body: PromptRequest):
    client = open_ai_client()
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": body.prompt
        }
      ]
    )
    ai_message = response.choices[0].message.content
    return {"message": ai_message}
