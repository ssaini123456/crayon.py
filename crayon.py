#
# author: Sutinder S. Saini
#
# github: https://github.com/sa111n111
#
#
import random
import io
import aiohttp
import asyncio
import json
import uuid
import urllib.parse

class CraiyonNoValueError(ValueError):
    pass

class CraiyonWantedSizeTooBigError(ValueError):
    pass

class CraiyonNoOutputProvidedError(ValueError):
    pass

class Craiyon:

    def __init__(self):
        # HTTP stuff for Crayon.
        # Achieved through RE'ing the backend.
        self.crayon_url = "https://backend.craiyon.com/generate"
        
        self.headers = {}
        self.headers["Content-Type"] = "application/json"

    async def generate(self, count: int = 1, output_str: str = None, *, text: str = None):
        if count > 6:
            raise CraiyonWantedSizeTooBigError("Your wanted size must not exceed 6.")

        if output_str == None:
            raise CraiyonNoOutputProvidedError("You must provide an output name!")

        # build our request 
        IR = {
            'prompt': text
        }

        data = json.dumps(IR)

        to_json = None
        async with aiohttp.ClientSession() as session:
            async with session.post(self.crayon_url, data=data, headers=self.headers) as resp:
                # grab our json response asynchronously
                to_json = await resp.json()

        image_id = uuid.uuid4()
                
        data_url_template = "data:image/jpeg;base64,"
        
        # form our data-url
        for i in range(count):
            url_fmt = "{}{}".format(data_url_template, to_json["images"][i+1])
            
            # Prepare image download. we simply use urlopen to open our data URI
            # and write its contents to an image.jpg file.
            response = urllib.request.urlopen(url_fmt)
            with open('{}'.format(output_str), 'wb') as f:
                f.write(response.file.read())

#craiyon = Craiyon()
#uuid_tag = uuid.uuid4()
#asyncio.run(craiyon.generate(count=3, output_str=f"{uuid_tag}_img.jpg", text="Rock the Casbah"))
