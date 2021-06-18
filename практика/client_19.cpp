#define NOMINMAX
#include <SDKDDKVer.h>
#pragma comment(lib, "ws2_32.lib")
#include <winsock2.h>
#include <iostream>
#include <string>
#include <math.h>
#include <fstream>
#include <string>
#define _WINSOCK_DEPRECATED_NO_WARNINGS
#pragma warning(disable: 4996)
SOCKET Connection;
std::string message = " ";
char mode = ' ';
enum Packet
{
	Chat,
	P_Test,
};
bool ProcessPacket(Packet packettype)
{
	switch (packettype)
	{
	case Chat:
	{
		int msg_size;
		recv(Connection, (char*)&msg_size, sizeof(int), NULL);
		char* msg = new char[msg_size + 1];
		msg[msg_size] = '\0';
		recv(Connection, msg, msg_size, NULL);
		message = msg;
		std::cout << msg << std::endl;
		delete[] msg;
		break;
	}
	case P_Test:
		std::cout << "Test packet :3.\n";
		break;
	default:
		std::cout << "Unrecognized packet >~<: " << packettype << std::endl;
		break;
	}
	return true;
}

void ClientHandler()
{
	Packet packettype;
	while (true)
	{
		recv(Connection, (char*)&packettype, sizeof(Packet), NULL);

		if (!ProcessPacket(packettype))
		{
			break;
		}
	}
	closesocket(Connection);
}
float timer;
int main(int argc, char* argv[])
{
	WSAData wsaData;
	WORD DLLVersion = MAKEWORD(2, 1);
	system("color 0a");
	std::string name = " ";
	if (WSAStartup(DLLVersion, &wsaData) != 0)
	{
		std::cout << "Error" << std::endl;
		exit(1);
	}
	char ip[256];
	int port;
	std::cout << "///////////" << std::endl;
	std::cout << "ENTER IP: ";
	std::cin >> ip;
	std::cout << "\n///////////" << std::endl;
	std::cout << "ENTER PORT: ";
	std::cin >> port;
	std::cout << "\n///////////" << std::endl;
	std::cout << "ENTER NAME: ";
	std::cin >> name;
	SOCKADDR_IN addr;
	int sizeofaddr = sizeof(addr);
	addr.sin_addr.s_addr = inet_addr(ip);
	addr.sin_port = htons(port);
	addr.sin_family = AF_INET;
	Connection = socket(AF_INET, SOCK_STREAM, NULL);
	if (connect(Connection, (SOCKADDR*)&addr, sizeof(addr)) != 0)
	{
		std::cout << "Error: failed connect to server >~<.\n";
		return 1;
	}
	std::cout << "Connected!\n";
	CreateThread(NULL, NULL, (LPTHREAD_START_ROUTINE)ClientHandler, NULL, NULL, NULL);
	std::string msg1;
	while (true)
	{
		std::cin >> msg1;
		msg1 = name + ": " + msg1;
		int msg_size = msg1.size();
		Packet packettype = Chat;
		send(Connection, (char*)&packettype, sizeof(Packet), NULL);
		send(Connection, (char*)&msg_size, sizeof(int), NULL);
		send(Connection, msg1.c_str(), msg_size, NULL);
	}
	system("pause");
	return 0;
}