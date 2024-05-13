#!/usr/bin/env python
import pika, sys, os
#Phương thức kết nối 
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
#Hàm nhận tin nhắn 
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
#cấu hình và chạy lại hàm callback
    channel.basic_consume(queue='hello', 
                          on_message_callback=callback, 
                          auto_ack=True)

    print(' [*] Đang chờ tin nhắn. Nhấn CTRL + C để thoát.')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Kết thúc!!!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)