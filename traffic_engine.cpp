#include <pcap.h>
#include <iostream>
#include <fstream>
#include <ctime>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>

std::ofstream csv("traffic_data.csv", std::ios::app);

void write_header() {
    csv << "timestamp,src_ip,dst_ip,src_port,dst_port,protocol,packet_len,tcp_flags\n";
}

void packet_handler(u_char *, const struct pcap_pkthdr *header, const u_char *packet) {
    struct ip *ip_hdr = (struct ip *)(packet + 14);

    if (ip_hdr->ip_p != IPPROTO_TCP) return;

    struct tcphdr *tcp_hdr = (struct tcphdr *)(packet + 14 + ip_hdr->ip_hl * 4);

    char timebuf[64];
    std::time_t now = std::time(nullptr);
    std::strftime(timebuf, sizeof(timebuf), "%H:%M:%S", std::localtime(&now));

    csv << timebuf << ","
        << inet_ntoa(ip_hdr->ip_src) << ","
        << inet_ntoa(ip_hdr->ip_dst) << ","
        << ntohs(tcp_hdr->th_sport) << ","
        << ntohs(tcp_hdr->th_dport) << ","
        << "TCP" << ","
        << header->len << ",";

    if (tcp_hdr->th_flags & TH_SYN) csv << "SYN";
    if (tcp_hdr->th_flags & TH_ACK) csv << "ACK";
    if (tcp_hdr->th_flags & TH_FIN) csv << "FIN";

    csv << "\n";
    csv.flush();
}

int main() {
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_if_t *devices;

    if (pcap_findalldevs(&devices, errbuf) == -1) {
        std::cerr << errbuf << std::endl;
        return 1;
    }

    pcap_t *handle = pcap_open_live(devices->name, BUFSIZ, 1, 1000, errbuf);
    if (!handle) {
        std::cerr << errbuf << std::endl;
        return 1;
    }

    write_header();
    pcap_loop(handle, 0, packet_handler, nullptr);

    pcap_close(handle);
    return 0;
}
