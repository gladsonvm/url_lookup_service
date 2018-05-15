# url lookup service
A URL scanner which responds to get requests to check a given url is vulnerable or not.

#### Setup
 - Clone this repository
    - git clone https://github.com/gladsonvm/url_lookup_service.git
 - Create a Virtual environment
    - mkvirtualenv <env_name>
 - Activate virual env
   - workon <env_name>
 - Install all requirements with `pip install requirements.txt`
 - run with `python app.py` by default app will be using port 8080
 
##### sending requests
  Send http GET requests in the format 
  
  http://<server:port>/1/<hostname_to_be_scanned:port>/original/path&<query_string=value>
  
  eg request: 
      
      GET http://localhost:8080/1/hostname_8000/path/to&qs=1
  response
  
      {
        "original_path": "hostname:port/origina/path&qs=1", 
        "meta": {"timestamp": "2018-05-15 12:45:29.748930", 
        "resource_uri": "/1/hostname:port/origina/path&qs=1"}, 
        "hostname": "hostname", 
        "port": "8000"
        }
##### how it works
  All required data is extracted from url and url to be scanned will be constructed from same. After that 
url to be scanned will be checked for vulnerability and results are returned as a json.