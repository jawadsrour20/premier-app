import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("tokens.json", scope)
client = gspread.authorize(creds)
excel = client.open("system_manager")
sheet = excel.get_worksheet(0)
login = excel.get_worksheet(1)
trans = excel.get_worksheet(2)
trans_admin = excel.get_worksheet(3)
summary = excel.get_worksheet(4)
premier = excel.get_worksheet(6)
managers = excel.get_worksheet(7)

def get_data():
    return sheet.get_all_records()


def login_data():
    return login.get_all_records()


def trans_data():
    return trans.get_all_records()


def summary_data():
    return summary.get_all_records()


def get_premier_data():
    return premier.get_all_records()

def get_users():
    return managers.get_all_records()

def insert_data(insertRow):
    trans.append_row(insertRow)


def insert_data_summary(insertRow):
    summary.append_row(insertRow)


def insert_data_admin(insertRow):
    trans_admin.append_row(insertRow)



# print(insert_data(["12",234]))