import pika
import json
from api.models import Idea


IDEA_STATE_CREATE = 'CREATE'
IDEA_STATE_UPDATE = 'UPDATE'
IDEA_STATE_DELETE = 'DELETE'


class MessageController:
    def __init__(self) -> None:
        self.uri = None
        self.conn = None

    def connect(self, uri) -> None:
        self.uri = uri
        self.conn = pika.BlockingConnection(
            pika.URLParameters(uri))

    def disconnect(self):
        self.conn.close()
        self.uri = None
        self.conn = None

    def publish_idea_creation(self, idea: Idea):
        channel = self.conn.channel()
        #self._notify_index_create_idea(channel, idea)
        self._notify_user_relation_operation(channel, idea, IDEA_STATE_CREATE)
        channel.close()

    def publish_idea_modification(self, idea: Idea):
        channel = self.conn.channel()
        # Id will be
        #self._notify_index_update_idea(channel, idea)
        self._notify_user_relation_operation(channel, idea, IDEA_STATE_UPDATE)
        channel.close()

    def publish_idea_deletion(self, idea: Idea):
        channel = self.conn.channel()
        #self._notify_index_delete_idea(channel, idea)
        self._notify_user_relation_operation(channel, idea, IDEA_STATE_DELETE)
        channel.close()

    def _notify_user_relation_operation(self, channel, idea, operation):
        self._publish_on_exchange(channel,
                                  'idea',
                                  'idea.operation',
                                  {'id': idea.id,
                                   'idea_name': idea.name,
                                   'state': operation})

    def _notify_index_delete_idea(self, channel, idea: Idea):
        self._publish_on_exchange(channel,
                                  'idea',
                                  'idea.index',
                                  {'id': idea.id,
                                   'idea_name': idea.name,
                                   'state': IDEA_STATE_DELETE})

    def _notify_index_update_idea(self, channel, idea: Idea):
        self._publish_on_exchange(channel,
                                  'idea',
                                  'idea.index',
                                  {'id': idea.id,
                                   'idea_name': idea.name,
                                   'state': IDEA_STATE_UPDATE})

    def _notify_index_create_idea(self, channel, idea: Idea):
        self._publish_on_exchange(channel,
                                  'idea',
                                  'idea.index',
                                  {'id': idea.id,
                                   'idea_name': idea.name,
                                   'state': IDEA_STATE_CREATE})

    def _publish_on_exchange(self, channel, exchange, routing_key, body):
        channel.exchange_declare(
            exchange=exchange,
            exchange_type='direct'
        )
        channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(body))


MsgCtrl = MessageController()
