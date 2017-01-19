import gtk
from localisation import config

class Alignment(gtk.VBox):

	def __init__(self):
		super(Alignment, self).__init__()
		
		bStop = gtk.Button( config.LOC["align_bStop"] )      
		
		self.pack_start(bStop, True, True, 10)
