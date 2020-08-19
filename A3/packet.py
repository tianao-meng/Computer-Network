import socket
class packet:

    def __init__(self, message_type, router_id, data):
        
        self.message_type = message_type
        self.router_id = router_id
        self.data = data
    
    def get_init_udp_data(self):
        array = bytearray()
        array.extend(self.message_type.to_bytes(length=4, byteorder="big"))
        array.extend(self.router_id.to_bytes(length=4, byteorder="big"))
        
        array.extend(self.data.encode())
        return array
    
    def get_lsa_udp_data(self):
        array = bytearray()
        array.extend(self.message_type.to_bytes(length=4, byteorder="big"))
        array.extend(self.router_id.to_bytes(length=4, byteorder="big"))
        
        for i in range(len(self.data)):
            array.extend(self.data[i].to_bytes(length=4, byteorder="big"))
        
        return array

    @staticmethod
    def create_init(router_id):
        return packet(1, router_id, "")
    
    @staticmethod
    def create_lsa(sender_id, data):
        return packet(3, sender_id, data)
    
    @staticmethod
    def parse_init_reply_data(UDPdata):
        message_type = int.from_bytes(UDPdata[0:4], byteorder="big") #4
        num_links = int.from_bytes(UDPdata[4:8], byteorder="big")
        link_dic = {}
        for i in range(num_links):
            link_id = int.from_bytes(UDPdata[(8+ (8 * i)): ((8+ (8 * i)) + 4 )], byteorder="big")
            link_cost = int.from_bytes(UDPdata[(8+ (8 * i) + 4) : ((8+ (8 * i)) + 8)], byteorder="big")
            link_dic[link_id] = link_cost

        return message_type, num_links, link_dic

    @staticmethod
    def parse_lsa(UDPdata):
        message_type = int.from_bytes(UDPdata[0:4], byteorder="big")
        sender_id = int.from_bytes(UDPdata[4:8], byteorder="big")
        sender_link_id = int.from_bytes(UDPdata[8:12], byteorder="big")
        router_id = int.from_bytes(UDPdata[12:16], byteorder="big")
        router_link_id = int.from_bytes(UDPdata[16:20], byteorder="big")
        router_link_cost = int.from_bytes(UDPdata[20:24], byteorder="big")

        lsa_res = [message_type, sender_id, sender_link_id, router_id, router_link_id, router_link_cost]
        return lsa_res


