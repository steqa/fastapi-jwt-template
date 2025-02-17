from api.redis import redis_client


def add_token_to_blacklist(jti: str, expire_at: str):
    redis_client.set(jti, "blocked")
    redis_client.expireat(jti, expire_at)


def is_token_blacklisted(jti: str) -> bool:
    return redis_client.get(jti) is not None
