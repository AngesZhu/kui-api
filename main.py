from waitress import serve
from setting import start_app, settings

__all__ = ["app"]
app = start_app()


if __name__ == '__main__':
    serve(app, listen=f'*:{settings.PROJECT.PORT}')
