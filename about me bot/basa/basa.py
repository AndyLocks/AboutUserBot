import pickle
from .members import Members

class Basa:


    async def updateMember(id: int, member: Members) -> None:


        with open(f"members/member{id}.pickle", "wb") as f:
            pickle.dump(member, f)


    async def makeNewMember(id: int):


        with open(f"members/member{id}.pickle", "wb") as f:
            member = Members()
            pickle.dump(member, f)


    async def isMemberInBasa(id: int) -> bool:

        
        try:
            open(f"members/member{id}.pickle", "rb")

        except FileNotFoundError:
            return False
        
        return True
    
    
    async def getMember(id: int) -> Members:
        with open(f"members/member{id}.pickle", 'rb') as f:
            try: return pickle.load(f)
            except EOFError: return Members()
        

if __name__ == "__main__":
    import asyncio

    async def main():
        pass
        

    asyncio.run(main())