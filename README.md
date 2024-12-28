# Shelf Library Catalog

## Overview
Shelf is a web-based library catalog system designed to help users manage their book collections and keep track of their reading progress. It offers user authentication, book management, and user-specific tracking functionalities. Built with Python and Flask, it uses an SQLite database for data persistence.

## Features

*   **User Authentication:**
    *   Secure user registration.
    *   User login functionality with password hashing.
    *   User logout.
*   **Book Management:**
    *   Add new books with titles and authors.
    *   View a list of all available books.
    *   View detailed information about a book.
*   **User Book Tracking:**
    *   Users can track the books they've read.
    *   View a list of recorded books.
*   **Responsive Design:** Basic responsive layout for a good viewing experience.
*   **Styling:** Styled with a vintage aesthetic and a color palette.
*   **Animations:** Implemented subtle transitions and animations

## Technologies Used

*   **Python:**  Programming language
*   **Flask:** Web framework
*   **Flask-SQLAlchemy:**  SQL toolkit and ORM
*   **Flask-Login:**  User authentication
*   **Flask-WTF:** Form handling
*   **SQLite:** Database
*   **HTML/CSS/JavaScript:**  Front-end technologies.

## Setup Instructions

Follow these steps to get the "Shelf" application running on your local machine.

### Prerequisites
*   Python 3.7 or higher
*   pip (Python package manager)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/toqaezzatly/Shelf_library_catalog/
   
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Create an `requirements.txt` file:** make sure to create a `requirements.txt` file by listing all the dependencies of the project, you can generate it by running the command: `pip freeze > requirements.txt`

6.  **Run the application:**
    ```bash
    python app.py
    ```

7.  **Open in browser:** Navigate to `http://127.0.0.1:5000/` in your web browser.

## Directory Structure
