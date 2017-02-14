from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory
import marisa_trie
from kivy.uix.label import Label
from kivy.factory import Factory
import copy
import sys
import random
import struct
import json
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
c=0
ce=[0]
lister=list()
global keys
global values
global old
old=""
global all_details
global trie2
global newvalues
global all_detailin
all_detailin={'first':'last'}

class TestRoot(BoxLayout):


	def add_name(self):
		global ce
		ce=random.randint(0,1000)
		global fmt
		fmt="<H"
		keys= list()
		values= list()
		newvalues=list()
		key_value=list()
		trie=marisa_trie.RecordTrie(fmt, zip(keys,values))
		#with open('my_trie_copy.marisa','w') as f:
		#	trie.write(f)
		trie.load('my_trie_copy.marisa')
		newvalues=trie.items()
		for i in range(len(newvalues)):

			newvalues[i]=list(newvalues[i])

		key_value.append(self.add_input.text)
		key_value.append((ce,))
		newvalues.append(key_value)
		keys=[]
		values=[]
		for x in newvalues:
			keys.append(x[0])
			values.append(x[1])
		trie=marisa_trie.RecordTrie(fmt, zip(keys,values))
		global details
		with open('my_dict.json','w') as f:
			json.dump(all_detailin,f)
		f.close()
		with open('my_dict.json') as f:
			all_details = json.load(f)
		f.close()		
		details={"name":'','number':'','emailid':'','facebook':''}
		details['name']= self.add_input.text
		details['number']= self.add_number.text
		details['emailid']= self.add_email.text
		details['facebook']= self.add_facebook.text
		all_details[ce]=details
		with open('my_dict.json','w') as f:
			json.dump(all_details,f)
		f.close()
		trie.save('my_trie_copy.marisa')


	def search_page(self):
		self.clear_widgets()
		new_page=Factory.Searchresults()
		self.add_widget(new_page)


class Listitems(ListItemButton):
	    pass


class Searchresults(BoxLayout):


	def search_name(self):
		global fmt
		fmt="<H"
		keys= list()
		values= list()
		global trie2
		trie2=marisa_trie.RecordTrie(fmt, zip(keys,values))		
		trie2.load('my_trie_copy.marisa')
		old=""
		liste=[]
		liste=trie2.keys(self.search_resulti.text)
		for x in liste:
			self.test.text=x
		data=liste
		self.search_output.item_strings=liste
		del self.search_output.adapter.data[:]
	def display(self):
		valv=trie2[self.test.text]
		valvi=valv[0][0]
		with open('my_dict.json') as f:
			my_dict = json.load(f)

		dictionary=my_dict[str(valvi)]
		self.name.text=dictionary["name"]
		self.phone.text=dictionary["number"]
		self.mail.text=dictionary["emailid"]
		self.fb.text=dictionary["facebook"]
	def search_pa(self):
		self.clear_widgets()
		new_=Factory.TestRoot()
		self.add_widget(new_)

class TestApp(App):
    pass	

if __name__ == '__main__':	
	TestApp().run()