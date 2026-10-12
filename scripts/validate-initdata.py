"""Validate raw initData locally. Usage: python validate-initdata.py <BOT_TOKEN> "<RAW_INITDATA>" """
import sys, hmac, hashlib, time
from urllib.parse import parse_qsl
def validate(raw: str, token: str, max_age: int = 86400):
    pairs = dict(parse_qsl(raw, keep_blank_values=True))
    h = pairs.pop("hash", None)
    assert h, "no hash — pass window.Telegram.WebApp.initData as-is"
    s = "\n".join(f"{k}={v}" for k, v in sorted(pairs.items()))
    secret = hmac.new(b"WebAppData", token.encode(), hashlib.sha256).digest()
    calc = hmac.new(secret, s.encode(), hashlib.sha256).hexdigest()
    assert hmac.compare_digest(calc, h), "BAD SIGNATURE — do not trust"
    age = time.time() - int(pairs.get("auth_date", 0))
    print(f"age: {age:.0f}s")
    assert age < max_age, "EXPIRED"
    print("OK — signature valid. user =", pairs.get("user", "")[:120])
if __name__ == "__main__":
    if len(sys.argv) < 3: print(__doc__); sys.exit(2)
    validate(sys.argv[2], sys.argv[1])
