from utils.data_capture import DataCapture


def run():
    data_capture = DataCapture()
    data_capture.add_number(3)
    data_capture.add_number(9)
    data_capture.add_number(3)
    data_capture.add_number(4)
    data_capture.add_number(6)

    stats = data_capture.build_stats()

    print(stats.less(4))
    print(stats.greater(4))
    print(stats.between(3, 6))


if __name__ == "__main__":
    run()
