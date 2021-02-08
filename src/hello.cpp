#include <iostream>

#include "Poco/MD5Engine.h"
#include "Poco/DigestStream.h"

#include "hello.h"


void hello() {
    #ifdef NDEBUG
    std::cout << "Hello World Release!" <<std::endl;
    #else
    std::cout << "Hello World Debug!" <<std::endl;
    #endif


    Poco::MD5Engine md5;
    
	Poco::DigestOutputStream ds(md5);
    ds << "abcdefghijklmnopqrstuvwxyz";
    ds.close();
	
	
	std::string strMD5 = Poco::DigestEngine::digestToHex(md5.digest());	
    std::cout << "MD5 of string `abcdefghijklmnopqrstuvwxyz`" << strMD5 << std::endl;
	
    return;

}
