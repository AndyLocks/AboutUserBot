import pickle
from .members import Members

class Basa:


    async def updateMember(id: int, member: Members) -> None:
        """Rewrites the file found by id to the received user."""


        with open(f"members/member{id}.pickle", "wb") as f:
            pickle.dump(member, f)


    async def makeNewMember(id: int) -> None:
        """Creates a Pickle file following the pattern: Member<user_id> (Member123456789). Folder: members"""


        with open(f"members/member{id}.pickle", "wb") as f:
            member = Members()
            pickle.dump(member, f)


    async def isMemberInBasa(id: int) -> bool:
        """Returns true if the user is in the database, otherwise false"""

        
        try:
            open(f"members/member{id}.pickle", "rb")

        except FileNotFoundError:
            return False
        
        return True
    
    
    async def getMember(id: int) -> Members:
        """Returns the user found by id. If the file was empty, a new user object will be returned."""


        with open(f"members/member{id}.pickle", 'rb') as f:
            
            try: return pickle.load(f)
            except EOFError: return Members()