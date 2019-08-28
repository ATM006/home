//server.c

#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<sys/socket.h>
#include<sys/wait.h>
#include<unistd.h>
#include <arpa/inet.h>


int main()
{
	struct sockaddr_in address,client;
	bzero(&address,sizeof(address));
	
	address.sin_family = AF_INET;
	address.sin_port = htons(8088);
	//address.sin_addr.s_addr = inet_addr("127.0.0.1");
	address.sin_addr.s_addr = INADDR_ANY;
	
	int sockfd = socket(AF_INET,SOCK_STREAM,0);

	int ret = bind(sockfd,(struct sockaddr*)&address,sizeof(address));

	ret = listen(sockfd,5);

	socklen_t len = sizeof(address);
	int connfd = accept(sockfd,(struct sockaddr*)&address,&len);		

	char buff[128] = {0};
	while(1)
	{
		memset(buff,'\0',sizeof(buff));
		recv(connfd,buff,sizeof(buff)-1,0);
		printf("-> %s\n",buff);

		send(connfd,buff,sizeof(buff)-1,0);

	}
	
	close(sockfd);
	return 0;
}
