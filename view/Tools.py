import gtk
from Index import Index
from Alignment import Alignment
from localisation import config

class Tools(gtk.Notebook):
	
	def __init__(self):
		super(Tools, self).__init__()
		
		vboxIndex = gtk.VBox(False, 5)
		aIndex = gtk.Alignment(0.5,0.25, 0, 0)
		aIndex.add( Index() )

		vboxAlign = gtk.VBox(False, 5)
		aAlign = gtk.Alignment(0.5,0.25, 0, 0)
		aAlign.add( Alignment() )

		vboxIndex.pack_start( aIndex )
		vboxAlign.pack_start( aAlign )
		
		self.set_tab_pos(gtk.POS_TOP)        		
		self.append_page(vboxIndex)
		self.set_tab_label_text(vboxIndex, config.LOC["tools_index"])
		self.append_page(vboxAlign)
		self.set_tab_label_text(vboxAlign, config.LOC["tools_align"])
