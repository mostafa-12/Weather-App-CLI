import os
import json
import time
class Cache:
    CACHE_FILE = "cache.json"
    EXPIRATION_TIME = 3600
    
    @classmethod
    def loadCache(cls):

        if os.path.exists(cls.CACHE_FILE):
        
            with open(cls.CACHE_FILE) as file:
        
                return json.load(file)
        return {}
    
    @classmethod
    def save(cls, data):
        
        with open(cls.CACHE_FILE,"w") as file:
            json.dump(data, file, indent=2, sort_keys= True)

    @classmethod
    def check(cls,paramter):
        cache = cls.loadCache()

        if paramter in cache.keys():

            timeStamp = time.time() - cache[paramter]["timestamp"]
            
            if timeStamp >= cls.EXPIRATION_TIME:

                del cache[paramter]
            
            else :
                return cache[paramter]["data"]
            
        return {}

    @classmethod
    def update(cls, key, data):
        
        loaded_cache = cls.loadCache()

        loaded_cache[key] = {

            "data" : data,
            "timestamp" : time.time()
        }
        cls.save(loaded_cache)
        
    @classmethod
    def clearCache(cls):
        if os.path.exists(cls.CACHE_FILE):
            os.remove(cls.CACHE_FILE)