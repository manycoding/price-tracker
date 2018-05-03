# price_tracker
  A service to fetch price changes of specified items. Update frequency specified in *settings.py*, currently it's daily at 23:00
  
  Dev server:
  
  https://is29q06ry7.execute-api.ap-northeast-1.amazonaws.com/dev
  
## Supported Shops
  * aliexpress.com

## In Short
    python3 manage.py runserver
    rabbitmq-server
    celery worker -A price_tracker -l info --beat -b amqp://user:pass@localhost:port/host
