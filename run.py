import argparse
from app.app import app


parser = argparse.ArgumentParser(description='Gorgeous App')
parser.add_argument('--port', "-p", type=int, default=8000,
                    help='port number')

args = parser.parse_args()


if __name__ == "__main__":
    app.run(host='localhost', port=args.port, debug=True)
