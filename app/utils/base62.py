import string
import uuid
from typing import Final


class Base62:
    BASE: Final[str] = string.ascii_letters + string.digits
    BASE_LEN: Final[int] = len(BASE)
    print(BASE_LEN)

    @classmethod
    def encode(cls, num: int) -> str:
        if num < 0:
            raise ValueError(f"{cls}.encode() need positive integer but you passed: {num}")

        if num == 0:
            return cls.BASE[0]

        result = []
        while num:
            num, remainder = divmod(num, cls.BASE_LEN)
            result.append(cls.BASE[remainder])
        return "".join(result)


print(uuid.uuid4().int)
