'''
Doc for our example file
'''

import asyncio

async def greeting(name):
    return f'Hello {name}'

if __name__ == '__main__':
    async def main():
        names = ['Guido', 'Dave', 'Paula']
        for name in names:
            g = await greeting(name)
            print(g)
    
    asyncio.run(main())
