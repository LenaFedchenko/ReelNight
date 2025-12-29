from modules import app, main_window
# from utils.api_requests import test_movie

# test_movie()
def main():
    try:
        main_window.show()
        app.exec()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()