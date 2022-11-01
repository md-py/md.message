import typing


# Meta
__author__ = 'https://md.land/md'
__version__ = '0.2.0'
__all__ = (
    # Meta
    '__author__',
    '__version__',
    # Contract
    'MessageInterface',
    'SendInterface',
    'ReceiveInterface',
    'HandleInterface',
    # Implementation
    'ReceiveApplication',
)


# Contract
class MessageInterface:
    def get_payload(self) -> typing.Any:
        raise NotImplementedError


class SendInterface:
    def send(self, message: MessageInterface) -> None:
        """ Thread-safe method to send message """
        raise NotImplementedError


class ReceiveInterface:
    def receive(self) -> typing.Iterable[MessageInterface]:
        """ Thread-safe method to return queue message """
        raise NotImplementedError

    def accept(self, message: MessageInterface) -> None:  # ack
        """ Thread-safe method to return accept message """
        raise NotImplementedError

    def reject(self, message: MessageInterface) -> None:  # nack
        """ Thread-safe method to return reject message """
        raise NotImplementedError


class HandleInterface:
    def handle(self, message: MessageInterface) -> None:
        raise NotImplementedError


# Implementation
class ReceiveApplication:
    def __init__(
        self,
        receive_message: ReceiveInterface,
        handle_message: HandleInterface,
        retry_exception: typing.Union[Exception, type, typing.Tuple[typing.Union[Exception, type]]] = None,
    ) -> None:
        self._receive_message = receive_message
        self._handle_message = handle_message
        self._retry_exception = retry_exception or tuple()

    def run(self) -> None:
        for message in self._receive_message.receive():
            try:
                self._handle_message.handle(message=message)
                self._receive_message.accept(message=message)
            except self._retry_exception:
                self._receive_message.reject(message=message)
