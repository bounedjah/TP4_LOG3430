import os

GOOD_COMMIT = os.getenv("GOOD_COMMIT", "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
BAD_COMMIT  = os.getenv("BAD_COMMIT",  "c1a4be04b972b6c17db242fc37752ad517c29402")

os.system(f"git bisect start {BAD_COMMIT} {GOOD_COMMIT}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")
