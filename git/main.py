import openai
import os
import sys

openai.api_key = os.environ['OPENAI_API_KEY']
if openai.api_key == "":
  sys.stderr.write("""
  You haven't set up your API key yet.
  
  If you don't have an API key yet, visit:
  
  https://platform.openai.com/signup

  1. Make an account or sign in
  2. Click "View API Keys" from the top right menu.
  3. Click "Create new secret key"

  Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
  """)
  exit(1)


topic = input("What topic would you like to learn about?\n> ".strip())

messages = [{"role": "system", "content": f"I want to do some interactiveinstruction. I want you to start explaining the concept of {topic} to me for tourism recommendation."}]

first = False
while True:  
  if first:
    question = input("> ")
    messages.append({"role": "user", "content": question})

  first = True

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )

  content = response ['choices'] [0]['message']['content'].strip()

  print(f"{content}")
  messages.append({"role": "system", "content": content})

  


response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "system",
        "content": "You are a helpful assistant."
    }, {
        "role": "user",
        "content": "Who won the world series in 2020?"
    }, {
        "role":
        "assistant",
        "content":
        "The Los Angeles Dodgers won the World Series in 2020."
    }, {
        "role": "user",
        "content": "Where was it played?"
    }])

print(response)
