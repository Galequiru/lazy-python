from typing import Callable

type Lazy[T] = Callable[[], T]