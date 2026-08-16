from langchain_ollama import ChatOllama

# Test your local model
llm = ChatOllama(model="qwen2.5-coder:14b")
response = llm.invoke("Say 'Hello, I am working!' in Python code")
print(response.content)