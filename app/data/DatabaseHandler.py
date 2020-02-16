import logging
from util.Util import util as Util
import sqlite3 as SQLiteDatabase
from model.Contact import *

print('Successfully calling the Util class ' + Util.DATABASE_NAME)

class DatabaseHandler:
    
    def __init__(self):
        self.database = SQLiteDatabase.connect('Contact Manager DB')
        self.db_drop = "DROP TABLE IF EXISTS "
        # super(Util.DATABASE_NAME,Util.DATABASE_VERSION)

    def __str__(self):
        return 'Database Handler class'
    
    # @Override
    # def onCreate(self,SQLiteDatabase): 
    def onCreate(self):
        'create table _name(id,name,phone_number) '

        try:
            CREATE_CONTACT_TABLE = "CREATE TABLE "+ Util.TABLE_NAME +"("+ Util.KEY_ID +" INTEGER PRIMARY KEY,"+ Util.KEY_NAME +" TEXT,"+ Util.KEY_PHONE_NUMBER +" TEXT"+")"
            self.database.execute(CREATE_CONTACT_TABLE) # Creating the table
        except Exception as e:
            print(e)

    # @Override
    def onUpgrade(self,i=1,i1=0):
        DROP_TABLE = self.db_drop
        # SQLiteDatabase.execSQL(DROP_TABLE, new String[]{Util.DATABASE_NAME})
        # onCreate(self.database) # create the table again

    ' CRUD ' 

    def addContact(self,Contact):
        
        # db = SQLiteDatabase.getWritableDatabase() 
        # just like a hashmap or arraylist for databases
##        values = SQLiteDatabase.ContentValues() 
##        values.put(Util.KEY_NAME,contact.getName()) 
##        values.put(Util.KEY_PHONE_NUMBER,contact.getPhoneNumber()) 

        # Insert to row
#        db.insert(Util.TABLE_NAME,None,values) 
        print("DB handler", "addContact: " + "item added") 
        # Need to close table once writing is complete
        self.database.close() 

    # Get a contact
    def getContact(self,Contact):
        
        contact = Contact.getContact(uid)
        db = SQLiteDatabase.getReadableDatabase()
        
        cursor = SQLiteDatabase.cursor()
        
        # cursor is used to iterate through db table elements
        cursor = db.query(Util.TABLE_NAME,list((Util.KEY_ID,Util.KEY_NAME, Util.KEY_PHONE_NUMBER)),Util.KEY_ID +"=?", list(String.valueOf(id)),None,None,None) 

        if cursor != None:
            cursor.moveToFirst() 

        contact = Contact() 
        contact.setId(Integer.parseInt(cursor.getString(0))) 
        contact.setName(cursor.getString(1)) 
        contact.setPhoneNumber(cursor.getString(2)) 

        cursor.close() 

        return contact 

    
    # Get all Contacts
    # public List<Contact>
    def getAllContacts(self):
        contactList = list([Contact])
        # List<Contact> contactList = new ArrayList<>()
        
        # db = SQLiteDatabase.getReadableDatabase() 

        # Select all contacts from the database table
        selectAll = "SELECT * FROM " + Util.TABLE_NAME 
        Cursor cursor = self.database.rawQuery(selectAll,None)

        # loop through the data
        if cursor.moveToFirst():
            ' Was originally a java do{ while { } } loop ' 
            # do:
            while cursor.moveToNext():
                contact = Contact() 
                contact.setId(Integer.parseInt(cursor.getString(0))) 
                contact.setName(cursor.getString(1)) 
                contact.setPhoneNumber(cursor.getString(2))
                
                # add contact objects to our list
                contactList.add(contact)
            # while cursor.moveToNext():
            
        cursor.close() 
        return contactList
    
    # Update contact
    def updateContact(Contact):
        db = SQLiteDatabase.getWritableDatabase()
        
        values = SQLiteDatabase.ContentValues() 
        values.put(Util.KEY_NAME,contact.getName()) 
        values.put(Util.KEY_PHONE_NUMBER, contact.getPhoneNumber())
        
        ' Update the row -- update(table_name,values,where id = 43) '
        return  db.update(Util.TABLE_NAME,values,Util.KEY_ID + "=?",list((String.valueOf(contact.getId()))))

    # Delete a contact
    def deleteContact(Contact):
        
        db = SQLiteDatabase.getWritableDatabase() 
        db.delete(Util.TABLE_NAME,Util.KEY_ID + "=?",list((String.valueOf(contact.getId()))))
        
        db.close() 

    # Contact count
    def getCount():
        countQuery = "SELECT * FROM " + Util.TABLE_NAME 
        db = SQLiteDatabase.getReadableDatabase() 
        cursor = db.rawQuery(countQuery,null) 

        return cursor.getCount()

tg = DatabaseHandler()
print("database handler instantiated:\n",tg)
' testing methods '
tg.onCreate()
tg.onUpgrade()
tg.addContact("Contact")
# tg.getContact(1)
tg.getAllContacts()
tg.updateContact()
tg.deleteContact()
tg.getContact()
