class TestBuMen:
    def wanmei(self, name, code):
        json = {"name": name,
                "code": code,
                "manager": "1",
                "introduce": "菜鸟部",
                "pid": "1260120712836886528"}
        return json

    def que_name(self, code):
        json = {
            "code": code,
            "manager": "1",
            "introduce": "菜鸟部",
            "pid": "1260120712836886528"}
        return json

    def que_code(self, name):
        json = {"name": name,
                "manager": "1",
                "introduce": "菜鸟部",
                "pid": "1260120712836886528"}
        return json
