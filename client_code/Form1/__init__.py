from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def buttonSubmit_click(self, **event_args):
    text_value = self.text_box_1.text
    anvil.server.call('say_hello', text_value)    
