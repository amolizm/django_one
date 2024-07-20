import uvicorn
from learning.asgi import application

def main():
    uvicorn.run(app=application,
                host="127.0.0.1", 
                port=8000, 
                log_level="info")

if __name__ == "__main__":
    main()