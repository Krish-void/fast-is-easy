import uvicorn
def main():
    print("Hello from crash-course-1!")


if __name__ == "__main__":
    main()

    uvicorn.run("src.app:app", host="0.0.0.0",port=8000, reload=True)
