from starlite import Request, Response

from exceptions.exceptions import DataAlreadyExistsException, InvalidCredentialsException, NoSuchDataException


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

def handle_invalid_credentials_exception(_: Request, exc: Exception) -> Response:
    return Response(
        status_code=401,
        content={"message": str(exc)},
    )


exception_handler_map = {
    DataAlreadyExistsException: handle_data_already_exists_exception,
    NoSuchDataException: handle_no_such_data_exception,
    InvalidCredentialsException: handle_invalid_credentials_exception,
}
