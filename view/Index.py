import gtk
from localisation import config

class Index(gtk.HBox):

	def __init__(self):
		super(Index, self).__init__()

                #Main variables
		lInput = gtk.Label( config.LOC["index_lInput"] )
		eInput = gtk.Entry()
		lOutput = gtk.Label( config.LOC["index_lOutput"] )
		eOutput = gtk.Entry()

                bRun = gtk.Button( config.LOC["index_bRun"] )

                image_entry_button_input = gtk.Image()
                image_entry_button_input.set_from_stock(gtk.STOCK_GO_DOWN, 2)
                bInput = gtk.Button()
                bInput.set_image(image_entry_button_input)

                image_entry_button_output = gtk.Image()
                image_entry_button_output.set_from_stock(gtk.STOCK_GO_DOWN, 2)    
                bOutput = gtk.Button()
                bOutput.set_image(image_entry_button_output)


                image_arrow = gtk.Image()
                image_arrow.set_from_stock(gtk.STOCK_GO_FORWARD, 10)
                bArrow = gtk.Button()
                bArrow.set_image(image_arrow)

                image_load = gtk.Image()
                image_load.set_from_stock(gtk.STOCK_YES, 10)
                bRed = gtk.Button()
                bRed.set_image(image_load)

                
                separator = gtk.VSeparator()

                # Option variables
                lOption = gtk.Label( config.LOC["index_lOption"] )
                lLength = gtk.Label( config.LOC["index_lLength"] )
                eLength = gtk.Entry()
                separator_option = gtk.HSeparator()
                

                #Build the boxes
                process = gtk.VBox(False, 0)
                process.add(bArrow)
                process.add(bRed)

                run = gtk.HBox(False, 0)
                run.add(bRun)
                run.add(process)

                input_entry = gtk.HBox(False, 0)
                input_entry.add(eInput)
                input_entry.add(bInput)

                output_entry = gtk.HBox(False, 0)
                output_entry.add(eOutput)
                output_entry.add(bOutput)

                
                main = gtk.VBox(False, 0)
                main.add(lInput)
                main.add(input_entry)
                main.add(lOutput)
                main.add(output_entry)
                main.add(run)
                

                option = gtk.VBox(False, 0)
                option.add(lOption)
                option.add(separator_option)
                option.add(lLength)
                option.add(eLength)
                
                #Add boxes to the Index box
                self.pack_start(main, True, True, 10)
                self.pack_start(process, True, True, 10)
                self.pack_start(run, True, True, 10) 
                self.add(separator)
                self.pack_start(option, True, True, 10)
                
                
