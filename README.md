# Customer Management App

A simple console-based Python application to manage customer data — including adding, updating, and validating emails and phone numbers.

## Project Structure

customer_app/
├── main.py              # Program entry point  
├── customer_ops.py      # Core logic: add/update/delete/search  
├── validation.py        # Input validation: email, phone, date  
├── ui.py                # Display and menu input  
├── data.py              # Holds sample customer data  
├── requirements.txt     # External libraries used  
└── tests/
    └── test_app.py      # Unit tests

## Installation

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt

## How to Run

To start the application, run:

```bash
python customer_app/main.py

---

### **Running Unit Tests**
```markdown
## Running Tests

To run unit tests:

```bash
python -m unittest discover customer_app/tests

---

### 👤 **(Optional) Author Section**
```markdown
## Author

Albert Cyriac  
Level 5 Digital & Technology Solutions Degree Apprentice  
