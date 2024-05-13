#!/usr/bin/env python
import pika, sys, os,time

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        ch.basic_ack(delivery_tag = method.delivery_tag)
        
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', 
                          on_message_callback=callback, 
                         )

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