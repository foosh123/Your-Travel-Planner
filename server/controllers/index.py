from starlite import Controller, get

class TestController(Controller):
    path = "/test"

    @get()
    async def index(self) -> str:
        return "This message is from the backend, if you see this then all's good."
