from tortoise import fields


class BaseModel:
    id = fields.BigIntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)


# MySQL : primary key 를 정할때 주의해야 되는 점
# MySQL version 8 이상 부터라면 (5.7 부터도 쓰긴 함.)
# innodb 가 default engine (옛날 MyISAM)

# innodb 의 특징 중 하나 -> clustering index
# primary key 를 기준으로
# primary key 값이 비슷한 row 들 끼리 disk 에서도 실제로 모여있음

# HDD
# 랜덤 IO 가 느리고 , 순차 IO 가 빠릅니다.

# 그냥 Int 가 아니라, 비즈니스 적 의미가 있고,
# 계속해서 증가 하는 어떤 값으로
# 굉장히 빠르게 읽을 수 있습니다.
# 1 10 20 30 100 ...~
