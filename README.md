# crayon.py
A reverse engineered wrapper over the craiyon backend.

# Examples
```py
craiyon = Craiyon()
asyncio.run(craiyon.generate(count=3, output_str="{}.jpg".format(uuid.uuid4()), text="Rock the Casbah"))
```
