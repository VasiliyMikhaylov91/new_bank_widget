import os
from typing import Any

from src.decorators import log


def test_log(capsys: Any) -> None:
    """
    Тестирование декоратора log:
    - С успешно выполняемой функцией
    - С функцией вызывающей исключение
    - С указанным лог файлом
    """

    @log()
    def empty_function() -> None:
        pass

    @log()
    def err_function() -> None:
        raise Exception("Что-то пошло не так")

    @log("my_log.txt")
    def empty_file_function() -> None:
        pass

    empty_function()
    captured = capsys.readouterr()
    assert captured.out == "empty_function ok\n\n"

    err_function()
    captured = capsys.readouterr()
    assert captured.out == "err_function error: Что-то пошло не так. Inputs:(), {}\n\n"

    empty_file_function()
    with open("my_log.txt", "r") as file:
        assert file.read() == "empty_file_function ok\n"
    os.remove("my_log.txt")
