from socket import *
import sys
from packet import packet
import threading
import copy

def Dijkstra(vr_router_id):
    N = [vr_router_id]
    distance_matrix_new = copy.deepcopy(distance_matrix)
    num_routers = len(distance_matrix_new)


    for i in range(len(distance_matrix_new)):
        for j in range(len(distance_matrix_new)):
            distance_matrix_new[i][j] = [distance_matrix_new[i][j], float("inf")]
    #change source node in distance matrix element to [cost, predecessor]
    for i in range(len(distance_matrix_new[vr_router_id - 1])):
        if (distance_matrix_new[vr_router_id - 1][i][0] != float("inf")):
            distance_matrix_new[vr_router_id - 1][i][1] = vr_router_id

    while (len(N) < num_routers):
        min_cost = float("inf")
        w = 0
        for router in range(num_routers):
            if (router + 1) not in N:
                if (distance_matrix_new[vr_router_id - 1][router][0] < min_cost):
                    w = router + 1
                    min_cost = distance_matrix_new[vr_router_id - 1][router][0]
        N.append(w)

        for dest in range(num_routers):
            if (dest + 1) not in N:
                if ((distance_matrix_new[w-1][dest][0] + distance_matrix_new[vr_router_id - 1][w-1][0]) < distance_matrix_new[vr_router_id - 1][dest][0]):
                    distance_matrix_new[vr_router_id - 1][dest][0] = distance_matrix_new[w-1][dest][0] + distance_matrix_new[vr_router_id - 1][w-1][0]
                    distance_matrix_new[vr_router_id - 1][dest][1] = w


    path_dict = {}
    for i in range(num_routers):
        path_dict[i + 1] = []

    for i in range(num_routers):
        if(distance_matrix_new[vr_router_id - 1][i][0] != float("inf")):
            last_router = distance_matrix_new[vr_router_id - 1][i][1]
            path_dict[i + 1].append(last_router)
            while (last_router != vr_router_id):
                last_router = distance_matrix_new[vr_router_id - 1][last_router-1][1]
                path_dict[i + 1].append(last_router)
            path_dict[i + 1].reverse()
            path_dict[i + 1].append(i + 1)
    return path_dict, distance_matrix_new

# type 1 is initial message
def router (nfe_ip, nfe_port, vr_router_id):

    topology = "{}_{}{}{}".format('topology', vr_router_id, '.', 'out')
    topology_file = open(topology, 'w')

    routingtable = "{}_{}{}{}".format('routingtable', vr_router_id, '.', 'out')
    routingtable_file = open(routingtable, 'w')

    # create new file not append, everytime open router, we create a empty file
    topology_file.close()

    routingtable_file.close()

    router_Socket = socket(AF_INET, SOCK_DGRAM)

    init_packet = packet.create_init(vr_router_id)

    router_Socket.sendto(init_packet.get_init_udp_data(), (nfe_ip, nfe_port))

    init_reply_packet, clientAddress = router_Socket.recvfrom(2048)
    # link_dic -> key is linkid, value is linkcost
    message_type, num_links, link_dic = packet.parse_init_reply_data(init_reply_packet)

    linkid_cost = []
    for key, value in link_dic.items():
        have_knowns_ele = [vr_router_id, key, value]
        have_knowns.append(have_knowns_ele)
        link_ids.append(key)

        linkid_cost.append([key, value])
    router_link_cost_dic[vr_router_id] = linkid_cost

    # The initial LSA being emitted to all the neighbours
    for have_known in have_knowns:
        for sender_link_id in link_ids:
            # have_known[0] is router_id, because it is initial lsa, router_id is itself
            # sender_id is always itself
            # data [sender_link_id, router_id, router_link_id, router_link_cost]
            data = [sender_link_id, have_known[0], have_known[1], have_known[2]]
            init_lsa_packet = packet.create_lsa(vr_router_id, data)
            # send initial lsa to all the neighbors
            print("Sending(E):SID(%d),SLID(%d),RID(%d),RLID(%d),LC(%d)" % (vr_router_id, sender_link_id, have_known[0], have_known[1], have_known[2]))
            router_Socket.sendto(init_lsa_packet.get_lsa_udp_data(), (nfe_ip, nfe_port))

    while True:
        topology = "{}_{}{}{}".format('topology', vr_router_id, '.', 'out')
        topology_file = open(topology, 'a')

        routingtable = "{}_{}{}{}".format('routingtable', vr_router_id, '.', 'out')
        routingtable_file = open(routingtable, 'a')


        lsa_packet, clientAddress = router_Socket.recvfrom(2048)
        lsa_message = packet.parse_lsa(lsa_packet)
        useful_message = [lsa_message[3],lsa_message[4], lsa_message[5]]

        sender_id = lsa_message[1]
        original_sender_link_id = lsa_message[2]

        print("Received:SID(%d),SLID(%d),RID(%d),RLID(%d),LC(%d)" % (lsa_message[1], lsa_message[2], lsa_message[3],lsa_message[4], lsa_message[5]))
        if (useful_message in have_knowns):
            print("Dropping:SID(%d),SLID(%d),RID(%d),RLID(%d),LC(%d)" % (lsa_message[1], lsa_message[2], lsa_message[3], lsa_message[4], lsa_message[5]))
            continue
        if (useful_message not in have_knowns):
            have_knowns.append(useful_message)

            router_id = useful_message[0]
            router_link_id = useful_message[1]
            router_link_cost = useful_message[2]
            
            #update distance matrix
            num_routers = len(distance_matrix)
            num_routers_add = router_id - num_routers
            if (router_id > num_routers):

                for i in (range(num_routers_add)):
                    distance_matrix.append([])

                for i in (range(num_routers)):
                    for j in (range(num_routers_add)):
                        distance_matrix[i].append(float("inf"))

                for i in (range(num_routers_add)):
                    for j in (range(router_id)):
                        distance_matrix[num_routers + i].append(float("inf"))
                # check if two routers have the same link between them then update the distance matrix
                for key in router_link_cost_dic.keys():

                    if ([router_link_id, router_link_cost] in router_link_cost_dic [key]):
                        src = key
                        dest = router_id

                        distance_matrix[src - 1][dest - 1] = router_link_cost
                        distance_matrix[dest - 1][src - 1] = router_link_cost
                        TOPOLOGY.append([src, dest, router_link_id, router_link_cost])

                        str_to_write = "{}{}".format("TOPOLOGY", '\n')
                        topology_file.write(str_to_write)
                        for i in TOPOLOGY:
                            str_to_write = "{}{}{}{}{}{}{}{}{}{}{}{}{}" \
                                .format('router', ':', i[0], ',router', ':', i[1], ',linkid', ':', i[2], ',cost', ':', i[3], '\n')
                            topology_file.write(str_to_write)

                            str_to_write = "{}{}{}{}{}{}{}{}{}{}{}{}{}" \
                                .format('router', ':', i[1], ',router', ':', i[0], ',linkid', ':', i[2], ',cost', ':', i[3], '\n')
                            topology_file.write(str_to_write)
                        topology_file.write('\n')
                        # routing table
                        path_dict, distance_matrix_new = Dijkstra(vr_router_id)
                        str_to_write = "{}{}".format("ROUTING", '\n')
                        routingtable_file.write(str_to_write)
                        for key in path_dict.keys():

                            if (key != vr_router_id) and (path_dict[key] != []):
                                str_to_write = "{}{}{}{}{}{}" \
                                    .format(path_dict[key][-1], ':', path_dict[key][1], ',',
                                            distance_matrix_new[vr_router_id - 1][key - 1][0], '\n')
                                routingtable_file.write(str_to_write)
                        routingtable_file.write('\n')

                        topology_file.close()

                        routingtable_file.close()
                        break

            else:
                for key in router_link_cost_dic.keys():
                    if ([router_link_id, router_link_cost] in router_link_cost_dic [key]):
                        src = key
                        dest = router_id
                        distance_matrix[src - 1][dest - 1] = router_link_cost
                        distance_matrix[dest - 1][src - 1] = router_link_cost
                        TOPOLOGY.append([src, dest, router_link_id, router_link_cost])

                        str_to_write = "{}{}".format("TOPOLOGY", '\n')
                        topology_file.write(str_to_write)
                        for i in TOPOLOGY:
                            str_to_write = "{}{}{}{}{}{}{}{}{}{}{}{}{}"\
                                .format('router', ':', i[0], ',router', ':', i[1],',linkid', ':', i[2],',cost', ':', i[3],'\n')
                            topology_file.write(str_to_write)

                            str_to_write = "{}{}{}{}{}{}{}{}{}{}{}{}{}"\
                                .format('router', ':', i[1], ',router', ':', i[0],',linkid', ':', i[2],',cost', ':', i[3],'\n')
                            topology_file.write(str_to_write)
                        topology_file.write('\n')

                        # routing table
                        path_dict, distance_matrix_new = Dijkstra(vr_router_id)
                        str_to_write = "{}{}".format("ROUTING", '\n')
                        routingtable_file.write(str_to_write)
                        for key in path_dict.keys():

                            if (key != vr_router_id) and (path_dict[key] != []):
                                str_to_write = "{}{}{}{}{}{}" \
                                    .format(path_dict[key][-1], ':', path_dict[key][1], ',',
                                            distance_matrix_new[vr_router_id - 1][key - 1][0], '\n')
                                routingtable_file.write(str_to_write)
                        routingtable_file.write('\n')

                        topology_file.close()

                        routingtable_file.close()
                        break

            #update roter_link_cost_dict
            if (router_id in router_link_cost_dic.keys()):

                router_link_cost_dic[router_id].append([router_link_id, router_link_cost])

            if not (router_id in router_link_cost_dic.keys()):
                router_link_cost_dic[router_id] = []
                router_link_cost_dic[router_id].append([router_link_id, router_link_cost])



            # send this useful message to neighbors
            for sender_link_id in link_ids:
                if (sender_link_id == original_sender_link_id):
                    continue
                # have_known[0] is router_id, because it is initial lsa, router_id is itself
                # sender_id is always itself
                # data [sender_link_id, router_id, router_link_id, router_link_cost]
                data = [sender_link_id, router_id, router_link_id, router_link_cost]
                print("Sending(F):SID(%d),SLID(%d),RID(%d),RLID(%d),LC(%d)" % (vr_router_id, sender_link_id, router_id, router_link_id, router_link_cost))
                lsa_packet = packet.create_lsa(vr_router_id, data)
                # send initial lsa to the neighbors
                router_Socket.sendto(lsa_packet.get_lsa_udp_data(), (nfe_ip, nfe_port))


if __name__ == "__main__":

    nfe_ip = sys.argv[1]
    nfe_port = int(sys.argv[2])
    router_id = int(sys.argv[3])

    have_knowns = []
    link_ids = []
    distance_matrix = []
    for i in range(router_id):
        distance_matrix.append([])
        for j in range(router_id):
            distance_matrix[i].append(float("inf"))
    # key is router id, value is [linkid, link_cost]
    router_link_cost_dic = {}
    # TOPOLOGY = [src, dest, linkid, link_cost]
    TOPOLOGY = []

    router(nfe_ip, nfe_port, router_id)
    topology_file.close()
    routingtable_file.close()
    exit(0)

