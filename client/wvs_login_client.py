from .client_base import ClientBase

class WvsLoginClient(ClientBase):
    """LoginClient

    Parameters
    ----------

    parent: `ServerBase`
        Parent server client is connecting to
    socket: `socket`
        Socket holding client - server connection
    name: str
        Name identifying type of client
    """

    def __init__(self, parent, socket):
        super().__init__(parent, socket)

        self.account = None
        self.server_id = None
        self.channel_id = None
        self.logged_in = False
    
    async def login(self, username, password):
        ret = await self._parent.login(self, username, password)

        if ret == 0:
            self.logged_in = True
        
        return ret

    @property
    def account_id(self):
        return self.account.id if getattr(self.account, 'id') else -1