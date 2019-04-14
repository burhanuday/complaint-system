from tkinter import *
from tkinter.ttk import *
from db import DBConnect
import sqlite3

class ListComp:
	def __init__(self):
		self._dbconnect = DBConnect()
		self._dbconnect.row_factory = sqlite3.Row
		self._root = Tk()
		self._root.geometry('800x800')
		self._root.title('List of Complaints')
		self.tree = Treeview(self._root)
		self.fillTable()
		
	
	def OnDoubleClick(self, event):
		item = self.tree.selection()
		print('item:', item)
		#print('event:', event)
		item = self.tree.selection()[0]
		curItem = self.tree.focus()
		print(self.tree.item(curItem)["values"][8])

		toggle = 1

		if self.tree.item(curItem)["values"][8] == "Case Closed":
			toggle = 0

		row = self.tree.item(item,"text")
		cursor = self._dbconnect.UpdateRow(toggle, int(row))
		self.fillTable()

	def fillTable(self):
		tv = self.tree
		tv.delete(*tv.get_children())
		tv.bind("<<TreeviewSelect>>", self.OnDoubleClick)
		tv.pack()
		tv.heading('#0', text='ID')
		tv.configure(column=('#PoliceStation', '#Subject', '#ComplaintType', '#Name', '#Gender', '#Address', '#Phone', '#Comment', '#Closed'))
		
		colwidth=80
		
		tv.heading('#PoliceStation',text='Police')
		tv.heading('#Subject',text='Subject')
		tv.heading('#ComplaintType',text='ComplaintType')		
		tv.heading('#Name', text='Name')
		tv.heading('#Gender', text='Gender')
		tv.heading('#Address', text='Address')
		tv.heading('#Phone', text='Phone')				
		tv.heading('#Comment', text='Comment')
		tv.heading('#Closed', text='Case Closed')
		cursor = self._dbconnect.ListRequest()
		
		tv.column("#0", width=50 )
		tv.column("#PoliceStation", width=colwidth )
		tv.column("#Subject", width=colwidth )
		tv.column("#ComplaintType", width=colwidth )
		tv.column("#Name", width=colwidth )
		tv.column("#Gender", width=colwidth )
		tv.column("#Address", width=colwidth )
		tv.column("#Phone", width=colwidth )
		tv.column("#Comment", width=colwidth )
		tv.column("#Closed", width=colwidth )
		
		for row in cursor:
			tv.insert('', 'end', '#{}'.format(row['ID']),text=row['ID'])
			tv.set('#{}'.format(row['ID']),'#PoliceStation',row['Police'])
			tv.set('#{}'.format(row['ID']),'#Subject',row['Subject'])
			tv.set('#{}'.format(row['ID']),'#ComplaintType',row['ComplaintType'])			
			tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
			tv.set('#{}'.format(row['ID']),'#Gender',row['Gender'])
			tv.set('#{}'.format(row['ID']),'#Address',row['Address'])
			tv.set('#{}'.format(row['ID']),'#Phone',row['Phone'])			
			tv.set('#{}'.format(row['ID']),'#Comment',row['Comment'])
			closed = "Investigation ongoing"
			if row['Closed'] == 1:
				closed = "Case Closed"
			tv.set('#{}'.format(row['ID']),'#Closed',closed)
			
