# QA Automation Framework

This project demonstrates a complete QA automation workflow using **Selenium WebDriver, PyTest, and Postman**.  
It includes **UI automation tests, API testing, manual test cases, and bug reporting** to simulate a real QA process.

---

## Project Overview

The framework automates testing for a sample e-commerce application using:

- Selenium WebDriver for UI automation
- PyTest for test execution
- Page Object Model (POM) design pattern
- PyTest fixtures for driver management
- pytest-html for test reporting
- Python requests for API automation
- Postman for API testing
- Manual test case documentation
- JIRA-style bug reporting

---

## Project Structure


qa-automation-framework
│
├── pages
│ ├── login_page.py
│ └── inventory_page.py
│
├── tests
│ ├── ui_tests
│ │ ├── test_login.py
│ │ ├── test_invalid_login.py
│ │ └── test_add_to_cart.py
│ │
│ └── api_tests
│ └── test_products_api.py
│
├── postman_collections
│ └── products_api_collection.json
│
├── testcases
│ └── login_test_cases.xlsx
│
├── bug_reports
│ └── login_error_bug.md
│
├── reports
│ └── report.html
│
├── conftest.py
├── requirements.txt
└── README.md


---

## Test Scenarios Implemented

### UI Automation Tests
- Valid Login Test
- Invalid Login Validation
- Add Product to Cart

### API Tests
- Fetch Products API
- Validate response status
- Validate response structure

### Manual Test Cases
- Login functionality
- Cart workflow
- API verification

---

## Technologies Used

| Tool | Purpose |
|-----|--------|
| Python | Programming language |
| Selenium | UI automation |
| PyTest | Test framework |
| Page Object Model | Design pattern |
| pytest-html | Test reporting |
| Python requests | API automation |
| Postman | API manual testing |
| Git & GitHub | Version control |

---

## How to Run the Tests

### 1. Clone the Repository


git clone <your-repo-url>


---

### 2. Create Virtual Environment


python -m venv venv


Activate environment:


venv\Scripts\activate


---

### 3. Install Dependencies


pip install -r requirements.txt


---

### 4. Run Tests


pytest --html=reports/report.html


---

## Sample Test Report

The framework generates HTML reports using pytest-html.

Example output:


5 Passed
0 Failed
0 Errors


---

## QA Workflow Demonstrated

This project simulates a real QA workflow:


Test Case Design
↓
UI Automation (Selenium)
↓
API Testing (Postman + Python)
↓
Bug Reporting
↓
Test Execution Reports


---

## Author

Mrunmai Kumbhar