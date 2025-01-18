from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_websocket(group: str, data: dict):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group,
        {
            "type": "send_notification",
            "data": data,
        }
    )