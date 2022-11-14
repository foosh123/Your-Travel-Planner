from starlite import Controller, get

class TestController(Controller):
    path = "/test"

    @get(exclude_from_auth=True)
    async def index(self) -> str:
        return "This message is from the backend, if you see this then all's good."
