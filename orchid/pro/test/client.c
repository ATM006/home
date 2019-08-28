//client.c

#include<stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>


int main()
{
	struct sockaddr_in address;

	bzero(&address,sizeof(address));
	address.sin_family = AF_INET;
	address.sin_port = htons(8088);
	//address.sin_addr.s_addr = INADDR_ANY;
	address.sin_addr.s_addr = inet_addr("127.0.0.1");
	
	int sockfd = socket(AF_INET,SOCK_STREAM,0);

	int ret = connect(sockfd,(struct sockaddr*)&address,sizeof(address));

	char buff[128] = {0};
	while(1)
	{
		scanf("%s",buff);
		if(strcmp(buff,"exit") == 0 )
			break;
		send(sockfd,buff,sizeof(buff)-1,0);

		bzero(&buff,sizeof(buff));
		recv(sockfd,buff,sizeof(buff)-1,0);
		printf("->%s\n",buff);

	}

	close(sockfd);
	return 0;
}
