from asyncio import create_task, Lock, get_event_loop
from random import randint
import logging

log = logging.getLogger(__name__)

from common.constants import VERSION, SUB_VERSION, LOCALE
from net.client.client_socket import ClientSocket
from net.packets.crypto import MapleCryptograph, MapleIV
from net.packets.packet import Packet

class ClientBase:
    def __init__(self, parent, socket):
        self.m_riv = None
        self.m_siv = None
        self.m_socket = socket
        
        self._parent = parent
        self.logged_in = False
        self._port = None

        self._server_id = None
        self._channel_id = None

    async def initialize(self):
        if isinstance(self._parent.__crypto__, MapleCryptograph):

            self.m_siv = MapleIV(randint(0, 2**31-1))
            self.m_riv = MapleIV(randint(0, 2**31-1))

            packet = Packet(op_code=0X0E)
            packet.encode_short(VERSION)
            packet.encode_string(SUB_VERSION)
            packet.encode_int(self.m_siv)
            packet.encode_int(self.m_riv)
            packet.encode_byte(LOCALE)

            await self.m_socket.send_packet_raw(packet)

        await self.recieve()

    async def recieve(self):
        m_recvBuffer = await self.sock_recv()

        if self.m_riv:
            m_recvBuffer = self.manipulate_buffer(m_recvBuffer, self.m_riv)

        self.dispatch(Packet(m_recvBuffer, op_codes=self._parent.__opcodes__))

    def dispatch(self, packet):
        self._parent._dispatcher.push(self, packet)

    async def sock_recv(self):
        return await self.m_socket.sock_recv()

    async def send_packet(self, packet):
        buffer = packet.to_array()
        opcode = packet.opcode

        await self.m_socket.send_packet(packet)

    async def send_packet_raw(self, packet):
        print(f"Sent : [{packet.op_code}] [{packet.to_string()}]")
        await self.m_socket.send_packet_raw(packet)

    def manipulate_buffer(self, buffer, iv):
        return self._parent.__crypto__.transform(buffer, iv)

    @property
    def server_id(self):
        return self._server_id
    
    @server_id.setter
    def server_id(self, value):
        self._server_id = value
    
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value