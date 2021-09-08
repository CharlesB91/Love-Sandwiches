import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

def get_sales_data():
    """
    Get Sales Figures  from the user
    """

    print("Please enter sales data from the last marker")
    print("Data shold be six numbers, seperated by commas")
    print("Example: 10,20,30,40,50")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raised ValueError of string cannot be converted into int, 
    or if there arent exactly 6 values.
    """
    try:
        [int(value) for value in values] 
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    

get_sales_data()