# -*- coding: utf-8 -*-
# Copyright (c) 2015, New Indictrans Technologies PVT LTD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Voucher(Document):
	def validate(self):
		total=0
		for raw in self.get("itemised_expenses"):
			total+=raw.cost
		self.gross_amount=total
		self.amount_payable=self.gross_amount-self.advance_amount-self.prepaid_amount
		# self.approved_amount=self.amount_payable

def get_manager_list(doctype, txt, searchfield, start, page_len, filters):
	data = frappe.db.sql("""select  parent from `tabUserRole` where role='Manager' """)
	return data

def get_accounts_officer_list(doctype, txt, searchfield, start, page_len, filters):
	data = frappe.db.sql("""select parent from `tabUserRole` where role='Accounts Officer' """)
	return data

