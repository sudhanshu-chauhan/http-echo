import json
import logging

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler


class EchoHTTPHandler(RequestHandler):
    def initialize(self) -> None:
        self.set_header("Content-Type", "application/json")

    def get(self: RequestHandler) -> None:
        echo_res = {}
        try:
            echo_res["query_params"] = {}
            for key, val in self.request.query_arguments.items():
                echo_res["query_params"][key] = [
                    unoval.decode("utf-8") for unoval in val]

            self.set_status(200)
            self.write(json.dumps(echo_res))
        except Exception as err:
            logging.error(err)
            self.set_status(500)
            self.write(json.dumps({"error": "unexpected application error"}))

    def post(self: RequestHandler) -> None:
        echo_res = {}
        try:
            echo_res["query_params"] = {}
            for key, val in self.request.query_arguments.items():
                echo_res["query_params"][key] = [
                    unoval.decode("utf-8") for unoval in val]
            echo_res["body"] = self.request.body.decode("utf-8")
            self.set_status(200)
            self.write(json.dumps(echo_res))
        except Exception as err:
            logging.error(err)
            self.set_status(500)
            self.write(json.dumps({"error": "unexpected application error"}))

    def put(self: RequestHandler) -> None:
        echo_res = {}
        try:
            echo_res["query_params"] = {}
            for key, val in self.request.query_arguments.items():
                echo_res["query_params"][key] = [
                    unoval.decode("utf-8") for unoval in val]
            echo_res["body"] = self.request.body.decode("utf-8")
            self.set_status(200)
            self.write(json.dumps(echo_res))
        except Exception as err:
            logging.error(err)
            self.set_status(500)
            self.write(json.dumps({"error": "unexpected application error"}))


class EchoApplication(Application):
    def __init__(self):
        handlers = [
            (r"/echo", EchoHTTPHandler)
        ]
        Application.__init__(self, handlers)


def main():
    try:
        host, port = "localhost", 8001
        app_instance = EchoApplication()
        logging.info("starting echo server at {}:{}".format(host, port))
        app_instance.listen(port, address=host)
        IOLoop.instance().start()
    except Exception as err:
        logging.error(err)


if __name__ == '__main__':
    main()
