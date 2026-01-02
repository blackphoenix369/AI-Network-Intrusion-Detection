#include <pcap.h>
#include <iostream>
#include <fstream>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <netinet/udp.h>
#include <netinet/ip_icmp.h>
#include <netinet/ether.h>
#include <arpa/inet.h>
#include <unordered_map>

std::ofstream csv("traffic_data.csv", std::ios::app);

void write_header() {
    csv << "timestamp,src_ip,dst_ip,src_port,dst_port,protocol,"
        << "packet_len,tcp_flags,flow_id\n";
}

std::string get_tcp_flags(u_char flags) {
    std::string f;

    if (flags & TH_SYN)  f += "SYN|";
    if (flags & TH_ACK)  f += "ACK|";
    if (flags & TH_FIN)  f += "FIN|";
    if (flags & TH_RST)  f += "RST|";
    if (flags & TH_PUSH) f += "PSH|";
    if (flags & TH_URG)  f += "URG|";

    if (!f.empty())
        f.pop_back();   
    else
        f = "NONE";

    return f;
}


void packet_handler(u_char *, const struct pcap_pkthdr *header, const u_char *packet) {
    struct ether_header *eth = (struct ether_header *)packet;
    if (ntohs(eth->ether_type) != ETHERTYPE_IP) return;

    struct ip *ip_hdr = (struct ip *)(packet + sizeof(struct ether_header));

    char src_ip[INET_ADDRSTRLEN], dst_ip[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &ip_hdr->ip_src, src_ip, sizeof(src_ip));
    inet_ntop(AF_INET, &ip_hdr->ip_dst, dst_ip, sizeof(dst_ip));

    std::string protocol = "OTHER";
    int src_port = 0, dst_port = 0;
    std::string flags = "NONE";

    if (ip_hdr->ip_p == IPPROTO_TCP) {
        protocol = "TCP";
        struct tcphdr *tcp = (struct tcphdr *)
            ((u_char *)ip_hdr + ip_hdr->ip_hl * 4);

        src_port = ntohs(tcp->th_sport);
        dst_port = ntohs(tcp->th_dport);
        flags = get_tcp_flags(tcp->th_flags);
    }
    else if (ip_hdr->ip_p == IPPROTO_UDP) {
        protocol = "UDP";
        struct udphdr *udp = (struct udphdr *)
            ((u_char *)ip_hdr + ip_hdr->ip_hl * 4);

        src_port = ntohs(udp->uh_sport);
        dst_port = ntohs(udp->uh_dport);
    }
    else if (ip_hdr->ip_p == IPPROTO_ICMP) {
        protocol = "ICMP";
    }

    char timebuf[64];
    std::snprintf(timebuf, sizeof(timebuf), "%ld.%06ld",
                  header->ts.tv_sec, header->ts.tv_usec);

    std::string flow_id =
        std::string(src_ip) + ":" + std::to_string(src_port) +
        "->" +
        std::string(dst_ip) + ":" + std::to_string(dst_port);

    csv << timebuf << ","
        << src_ip << ","
        << dst_ip << ","
        << src_port << ","
        << dst_port << ","
        << protocol << ","
        << header->len << ","
        << flags << ","
        << flow_id << "\n";

    csv.flush();
}


int main() {
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_if_t *devs;

    if (pcap_findalldevs(&devs, errbuf) == -1) {
        std::cerr << errbuf << std::endl;
        return 1;
    }

    pcap_t *handle = pcap_open_live(
        devs->name, BUFSIZ, 1, 1000, errbuf);

    if (!handle) {
        std::cerr << errbuf << std::endl;
        return 1;
    }

    write_header();
    std::cout << "[+] Capturing packets on: " << devs->name << std::endl;

    pcap_loop(handle, 0, packet_handler, nullptr);

    pcap_close(handle);
    return 0;
}
