# Database Handler

class Util:

    def __init__(self):
        # Database realted items
        self.DATABASE_VERSION = 1
        self.DATABASE_NAME = "contact_db"
        self.TABLE_NAME = "contacts"
        # Contacts column names
        self.KEY_ID = "id"
        self.KEY_NAME = "name"
        self.KEY_PHONE_NUMBER = "phone_number"


util = Util()

##def main():
##    util = Util()
##    return util

if __name__ == '__main__':
    util = Util()
