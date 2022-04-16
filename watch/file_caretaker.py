import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from path import path_dir


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(event.event_type, event.src_path)

    def on_created(self, event):
        print("создание", event.src_path)

    def on_deleted(self, event):
        print("удаление", event.src_path)

    def on_modified(self, event):
        print("модификация", event.src_path)

    def on_moved(self, event):
        print("перемещение", event.src_path)


path = path_dir
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()