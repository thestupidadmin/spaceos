print("You might have to do pip3 install aiohttp and asyncio and aiofiles so this script can work")

import os
import aiohttp      
import asyncio  
os.system("pip install aiofiles >/dev/null 2>/dev/null")
os.system("pip3 install aiofiles >/dev/null 2>/dev/null")
import aiofiles


async def t():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://github.com/thestupidadmin/spaceos/raw/refs/heads/main/testing-repo/pythonvps.sh") as resp:
            if resp.status == 200:
                f = await aiofiles.open('./pythonvps.sh', mode='wb')
                await f.write(await resp.read())
                await f.close()

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(t())
    loop.close()
    os.system("bash pythonvps.sh")

if __name__ == '__main__':
    main()
