import logging
import logging.config

entry=input("Enter Full Name:")
entry_message=input("Enter a message:")
msg_type=input("Enter the type of message i(info)/e(error)/w(warning)")

FORMAT = '%(asctime)s %(created)f  %(levelname)s  %(message)s'
logging.basicConfig(format=FORMAT)
    

if( msg_type=='i'):
    
    print(logging.info)

elif(msg_type=='e'):
    
    print(logging.error)

elif(msg_type=='w'):
    
    print(logging.warning)
else:
    pass






logging.info('This is an info message')
logging.error('This is an error message')
logging.warning('This is a warning message')


	


