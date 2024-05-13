import pika
#phương thức kết nối
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
#cấu hình và nội dung gửi tin nhắn
channel.basic_publish(exchange='', 
                      routing_key='hello', 
                      body='chao ban')
print(" [x] Sent 'Gửi tin nhắn thành công!!'")
connection.close()