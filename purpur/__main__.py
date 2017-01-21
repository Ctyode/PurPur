import tornado.ioloop
import tornado.web
import os


class Handler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        images = []

        for i in range(4):
            path = os.path.join('/static/images/', '{}.png'.format(i))
            images.append(path)

        self.render('index.html', images=images)


def make_app():
    here = os.path.dirname(os.path.abspath(__file__))
    application = tornado.web.Application([
        ('/', Handler),
        ('/static/(.*)', tornado.web.StaticFileHandler, {'path': os.path.join(here, 'static')})],
        debug=True, template_path=os.path.join(here, 'templates'))

    return application

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
