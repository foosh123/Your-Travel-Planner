from starlite import Request, Response

from exceptions.exceptions import DataAlreadyExistsException, EmailNotSentException, InvalidInputException, NoSuchDataException


def handle_data_already_exists_exception(_: Request, exc: Exception) -> Response:
    return Response(
        status_code=409,
        content={"message": str(exc)},
    )

def handle_no_such_data_exception(_: Request, exc: Exception) -> Response:
    return Response(
        status_code=404,
        content={"message": str(exc)},
    )

def handle_invalid_input_exception(_: Request, exc: Exception) -> Response:
    return Response(
        status_code=400,
        content={"message": str(exc)},
    )

def handle_email_not_sent_exception(_: Request, exc: Exception) -> Response:
    return Response(
        status_code=500,
        content={"message": str(exc)},
    )

exception_handler_map = {
    DataAlreadyExistsException: handle_data_already_exists_exception,
    NoSuchDataException: handle_no_such_data_exception,
    InvalidInputException: handle_invalid_input_exception,
    EmailNotSentException: handle_email_not_sent_exception,
}
