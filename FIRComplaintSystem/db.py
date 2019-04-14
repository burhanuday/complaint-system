#!/usr/bin/python3
import sqlite3

class DBConnect:
	def __init__(self):
		self._db = sqlite3.connect('information.db')
		self._db.row_factory = sqlite3.Row

	def Add(self, police, subject, type, name, gender, address, phone, comment, closed):
		self._db.execute('''insert into Comp (Police, Subject, ComplaintType, Name, Gender, Address, Phone, Comment, Closed) values (?,?,?,?,?,?,?,?,?)''',(police,subject,type,name,gender,address,phone,comment,closed))
		self._db.commit()
		return 'Your complaint has been submitted.'

	def ListRequest(self):
		cursor = self._db.execute('select * from Comp')
		return cursor

	def UpdateRow(self, row, val):
		#print('update Comp set Closed = {} where ID = {}'.format(row, val))
		self._db.execute('update Comp set Closed = {} where ID = {}'.format(row, val))
		self._db.commit()
