import bardapi
import os
from keys import *

# set your __Secure-1PSID value to key
token = BARD_KEY

# set your input text
input_text = "Create a House MD episode with this problem: Patient presented with autism. Write it as a script"

# Send an API request and get a response.
response = bardapi.core.Bard(token).get_answer(input_text)

print(response["content"])
