import sys
from homeassistant.helpers import selector
print("Attributes in selector:")
for x in sorted(dir(selector)):
    if "Selector" in x:
        print(f" - {x}")
