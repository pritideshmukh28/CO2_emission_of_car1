import pickle
import json
import numpy as np
import config


class CO2emission():
    def __init__(self,Car,Model,Volume,Weight):
        print("****** INIT Function *********")
        self.Car = Car
        self.Model = Model
        self.Volume = Volume
        self.Weight = Weight
    
    def __load_saved_data(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)


    def get_predicted_emission(self):
        self.__load_saved_data()
    
    #Car = 20
    #volume =1400
    #weight =929
        Car = self.json_data['Car'][self.Car]
        Model = self.json_data['Model'][self.Model]
        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = Car
        test_array[0,1] = Model
        test_array[0,2] = self.Volume
        test_array[0,3] = self.Weight

        CO2emission = np.around(self.model.predict(test_array)[0],3)
        return CO2emission


    