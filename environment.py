from dotenv import load_dotenv

import os
load_dotenv()

env = {
    "MONGO_URI": os.environ["MONGO_URI"]
}