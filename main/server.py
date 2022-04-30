import sys
import time
import logging
import random
from flask import Flask

if len(sys.argv) > 1:
    HOST = "127.0.0.1"
    print("HOST: " + HOST)
    PORT = int(sys.argv[1])
    print("PORT: " + str(PORT))

    logger = logging.getLogger(__name__)
    api = Flask(__name__)

    @api.route("/tiempo")
    def tiempo():
        t1 = time.time()
        time.sleep(random.randint(1, 5))
        t2 = time.time()
        return {"t1": t1, "t2": t2}

    api.run(host=HOST, port=PORT)
else:
    print("Usage: python3 server.py <port>")