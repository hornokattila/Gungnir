import settings
from gungnir import urls
from gungnir import wsdl

if __name__ == "__main__":
    wsdl.Flask(__name__).run(prints_config=settings.settings["config"], prints_prefix=urls.prints_prefix, prints_system=settings.settings["system"], prints=urls.prints, **settings.settings["server"])
