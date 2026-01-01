#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    ofstream file("traffic_data.csv");

    file << "packet_size,flow_duration,protocol_type,src_bytes,dst_bytes,packet_rate\n";

    srand(time(0));

    for (int i = 0; i < 200; i++) {
        int packet_size = rand() % 1460 + 40;
        int flow_duration = rand() % 10000 + 1;
        int protocol_type = rand() % 3;  // 0-TCP, 1-UDP, 2-ICMP
        int src_bytes = rand() % 5000;
        int dst_bytes = rand() % 5000;
        float packet_rate = (rand() % 1000) / 10.0;

        file << packet_size << ","
             << flow_duration << ","
             << protocol_type << ","
             << src_bytes << ","
             << dst_bytes << ","
             << packet_rate << "\n";
    }

    file.close();
    cout << "[+] traffic_data.csv generated successfully\n";
    return 0;
}
