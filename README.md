# Greeting with ChatGPT - WINDOWS

This is a small project that adds generative AI messages to defined places.

## Configuration on Windows

Follow these steps to set up and run the project on a Windows machine:

1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    venv\Scripts\activate
    ```

3. Install project dependencies from requirements.txt:
    ```bash
    python3 -m pip install -r requirements.txt
    ```

4. Start the web application using Uvicorn with auto-reload:
    ```bash
    uvicorn main:app --reload
    ```

5. In another terminal window, run the ETL script (etl.py):
    ```bash
    python3 etl.py
    ```

---------------------------------------------------------------------------------------------------------

# Greeting with ChatGPT - LINUX

This is a small project that adds generative AI messages to defined places.

## Configuration on Linux

Follow these steps to set up and run the project on a Linux machine:


1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

3. Install project dependencies from requirements.txt:
    ```bash
    python3 -m pip install -r requirements.txt
    ```

4. Start the web application using Uvicorn with auto-reload:
    ```bash
    uvicorn main:app --reload
    ```

5. In another terminal window, run the ETL script (etl.py):
    ```bash
    python3 etl.py
    ```
