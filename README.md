# price_tracker
  A service to write price changes of specified items.
  
  Dev server:
  
  https://rocky-lowlands-69345.herokuapp.com
  
## Supported shops
  * aliexpress.com
  * hanchor.com

## In Short
    python3 manage.py runserver
    rabbitmq-server
    celery worker -A price_tracker -l info --beat -b amqp://user:pass@localhost:port/host
