import requests, json, os

class DataGetter:
    def __init__(self):
        pass
    def request_url(self, apiUrl):
        response = requests.get(apiUrl)
        if response.status_code == 200:
            jsonData = json.dumps(response.json(), indent= 4, ensure_ascii= False)
            with open("test.json", "w+", encoding= "utf-8") as js:
                js.write(jsonData)
                  
        else: 
            print(f"請求失敗，狀態碼為{response.status_code}")

class CaseOne:
    def __init__(self, apiName):
        self.apiName = apiName
        self.get_target_api()
        self.get_target_data()
    def get_target_api(self):
        with open("test.json", "r", encoding="utf-8") as js:
            js = json.load(js)
            data = json.dumps(js, indent=4, ensure_ascii= False) # 打印用的
            for tag in js["tags"]:
                if tag["description"] == self.apiName:
                    self.targetApi = f"https://www.ris.gov.tw//rs-opendata/api/v1/datastore/{tag['name']}"
    def get_target_data(self):
        if not os.path.isdir("./case_one"):
            os.mkdir("./case_one")
        response = requests.get(self.targetApi)
        jsonData = response.json()
        if response.status_code == 200:
            for page in range(1, int(jsonData["totalPage"])+1):
                response = requests.get(f"{self.targetApi}/?page={page}")
                if response.status_code == 200:
                    js = json.dumps(response.json(), indent= 4, ensure_ascii= False)
                    with open("./case_one/case_one.json", "w+", encoding= "utf-8") as data:
                        data.write(js)
                        if page != int(jsonData["totalPage"]):
                            data.write("\n,\n")
                  
        else: 
            print(f"請求失敗，狀態碼為{response.status_code}")

class CaseTwo: 
    def __init__(self, apiName, year):
        self.apiName = apiName
        self.year = year
        self.get_target_api()
        self.get_target_data()
    def get_target_api(self):
        with open("test.json", "r", encoding="utf-8") as js:
            js = json.load(js)
            data = json.dumps(js, indent=4, ensure_ascii= False) # 打印用的
            for tag in js["tags"]:
                if tag["description"] == self.apiName:
                    self.targetApi = f"https://www.ris.gov.tw//rs-opendata/api/v1/datastore/{tag['name']}/{self.year}"
    def get_target_data(self):
        response = requests.get(self.targetApi)
        jsonData = response.json()
        if response.status_code == 200:
            if not os.path.isdir("./case_two"):
                os.mkdir("./case_two")
            for page in range(1, int(jsonData["totalPage"])+1):
                response = requests.get(f"{self.targetApi}/?page={page}")
                if response.status_code == 200:
                    js = json.dumps(response.json(), indent= 4, ensure_ascii= False)
                    with open(f"./case_two/case_two-{page}.json", "w+", encoding= "utf-8") as data:
                        data.write(js)
        else: 
            print(f"請求失敗，狀態碼為{response.status_code}")

class CaseThree:
    def __init__(self, motherAge):
        self.MotherAge = motherAge
        self.get_data()
    def get_data(self):
        if not os.path.isdir("./case_three"):
            os.mkdir("./case_three")
        for i in range(len(os.listdir("./case_two"))):
            result = []
            with open(f"./case_two/case_two-{i+1}.json", "r", encoding="utf-8") as data:
                data = json.load(data)
                for j in range(len(data["responseData"])):
                    if data["responseData"][j]["mother_age"] < f"{self.MotherAge}歲":
                        result.append(data["responseData"][j])
                data["responseData"] = result
                # print(data)
            with open(f"./case_three/case_three-{i+1}.json", "w+", encoding="utf-8") as file:
                file.write(json.dumps(data, indent= 4, ensure_ascii= False))
