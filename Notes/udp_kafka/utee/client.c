#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>

#define MESSAGE_SIZE 2048 

typedef enum {
    true = (1 == 1),
    false = (1 == 0)
}bool;

//improve fgets
char* imp_fgets(char* buf, int num, FILE* fp, bool ignore)
{
    char* find = 0;
    if (!fgets(buf, num, fp)){
        return NULL;
    }

    if ((find = strrchr(buf, '\n'))){
        *find = '\0';
    }
    else if (ignore){
        char ch;
        while (((ch = fgetc(fp)) != EOF) && (ch != '\n'));
    }
    return buf;
}

int main(int argc, char *argv[])
{
    int sockfd = 0;
    int num = 0, r = 0;
    struct sockaddr_in dest;
    char message[MESSAGE_SIZE ];
    char destIP[128] = "127.0.0.1";
    int port = 19820;
    int sendmsg = 0;
    int lines_read;
    int offset = 0;

    memset(message, 0, sizeof(message));
    fprintf(stdout,"STDIN_FILENO : %d\n",STDIN_FILENO);
    fprintf(stdout,"UDP Tee\n");
    if ( argc < 3 ) {
      fprintf(stdout,"UDP Tee <IP> <Port> <Message>\n");
      exit(1);
    }
    strcpy(destIP,argv[1]);
    port = atoi(argv[2]);
    if ( argc >= 4) {
      strcpy(message, argv[3]);
      sendmsg = 1;
    }

    fprintf(stdout,"stdin :%p, stdout:%p, stderr:%p\n", stdin, stdout, stderr);
    /* create socket */
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    /* initialize value in dest */
    bzero(&dest, sizeof(dest));
    dest.sin_family = AF_INET;
    dest.sin_port = htons(port);
    inet_pton(AF_INET, destIP, &dest.sin_addr);

    if ( sendmsg ) {
      fprintf(stdout,"send message %s to server[%s:%d]\n", message,destIP,port);
      sendto(sockfd,message,strlen(message),0,&dest,sizeof(dest));
    } else {
        memset(message,0,MESSAGE_SIZE );
      do {
        //lines_read = fgets(message,MESSAGE_SIZE,stdin);
        lines_read = imp_fgets(message,MESSAGE_SIZE,stdin,false);
        sendto(sockfd,message,strlen(message),0,&dest,sizeof(dest));
        memset(message,0,MESSAGE_SIZE );

      }while(lines_read != 0);
    }
    close(sockfd);
    fprintf(stdout,"close socket\n");
    
	return 0;
}

