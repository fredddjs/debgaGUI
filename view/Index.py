import gtk
from localisation import config

class Index(gtk.VBox):

	def __init__(self):
		super(Index, self).__init__()
		
		lInput = gtk.Label( config.LOC["index_lInput"] )
		eInput = gtk.Entry()
		lOutput = gtk.Label( config.LOC["index_lOutput"] )
		eOutput = gtk.Entry()
		bRun = gtk.Button( config.LOC["index_bRun"] )
        
		self.pack_start(lInput, True, True, 10)
		self.pack_start(eInput, True, True, 10)
		self.pack_start(lOutput, True, True, 10)
		self.pack_start(eOutput, True, True, 10)   
		self.pack_start(bRun, True, True, 10)
