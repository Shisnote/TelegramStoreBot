import logging, signal, sys

# Логирование программы
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s : %(name)s : %(message)s",  # Добавляем отметку времени
    datefmt="%Y-%m-%d %H:%M:%S"  # Формат времени
)
logger = logging.getLogger(__name__)


# Замена вывода о прекращении программы
def signal_handler(sig, frame):  # noqa
    print("KeyboardInterrupt")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)  # Обработка прерывания
