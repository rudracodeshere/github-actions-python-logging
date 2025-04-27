import logging

# Setup logging to a file
logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    logging.info("Script started.")

    try:
        x = 10 / 0   # This will cause a ZeroDivisionError
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
