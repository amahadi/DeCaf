from utils import TextProcessor
import pandas as pd

textProcessor = TextProcessor()

text = "For the code changes: the current akka osgi module has the import for the org apache aries marked as optional so theres no runtime dependency preventing this from working in a plain OSGi environment but I can obviously separate that into a new module as well if you prefer And I can obviously make the changes to the public methods as well"

text2 = textProcessor.replaceMispelledWords(text)

print(text2)