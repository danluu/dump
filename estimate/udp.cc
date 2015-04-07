#include <errno.h>
#include <netdb.h>
#include <netinet/in.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/uio.h>
#include <unistd.h>

#include <iostream>
#include <vector>

#define BUFFER_SZ 1024*1024*128
#define PAYLOAD_SZ 1024
#define NUM_SENDS 1000000

int main() {
  const char* hostname=0; // localhost. TODO: change this.
  const char* portname="daytime";
  struct addrinfo hints;
  memset(&hints,0,sizeof(hints));
  hints.ai_family=AF_UNSPEC;
  hints.ai_socktype=SOCK_DGRAM;
  hints.ai_protocol=0;
  hints.ai_flags=AI_ADDRCONFIG;
  struct addrinfo* res=0;
  int err = getaddrinfo(hostname,portname,&hints,&res);
  if (err != 0) {
    std::cout << "failed to resolve remote socket address: " << err << std::endl;
    return 1;
  }

  int fd=socket(res->ai_family, res->ai_socktype, res->ai_protocol);
  if (fd == -1) {
    std::cout << strerror(errno) << std::endl;
    return 1;
  }

  std::vector<char> content(BUFFER_SZ,0);  
  struct iovec iov[1];
  iov[0].iov_len=sizeof(PAYLOAD_SZ);
  
  struct msghdr message;
  message.msg_name=res->ai_addr;
  message.msg_namelen=res->ai_addrlen;
  message.msg_iov=iov;
  message.msg_iovlen=1;
  message.msg_control=0;
  message.msg_controllen=0;


  int idx = 0;
  for (int i = 0; i < NUM_SENDS; ++i) {
    iov[0].iov_base=static_cast<void*>(&content[idx]);
    
    if (sendmsg(fd,&message,0) == -1) {
      std::cout << strerror(errno) << std::endl;
      return 1;
    }
    idx = (idx + PAYLOAD_SZ) % BUFFER_SZ;
  }
  
  return 0;
}
