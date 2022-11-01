# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2022-10-31
### Change

- `md.message.ReceiveApplication` constructor parameter 
  `retry_message_exception` type generalized 
  from `typing.Tuple[typing.Union[Exception, type]]` to `typing.Union[Exception, type, typing.Tuple[typing.Union[Exception, type]]]`

#### Backward compatibility breaking change

- `md.message.ReceiveApplication` constructor parameter `retry_message_exception` renamed 
   to `retry_exception`

## [0.1.0] - 2022-10-26

- Implementation initialization

[0.2.0]: https://github.com/md-py/md.message/releases/tag/0.2.0
[0.1.0]: https://github.com/md-py/md.message/releases/tag/0.1.0
