
import unittest

from model import *

class ModelTest(unittest.TestCase):

    def test_01_train(self):

        model_train(os.path.join("cs-train"),test=True)
        saved_model = os.path.join("solution_guidance/models","sl-netherlands-0_1.joblib")
        self.assertTrue(os.path.exists(saved_model))

    def test_02_load(self):

        data_dir = os.path.join("cs-train")
        all_data, all_models = model_load(data_dir = data_dir)
        model = all_models['netherlands']
        
        self.assertTrue('predict' in dir(model))
        self.assertTrue('fit' in dir(model))

       
    def test_03_predict(self):

        data_dir = os.path.join("cs-train")
        ## ensure that a list can be passed        
        result = model_predict('netherlands','2018','08','01',test=True,  data_dir = data_dir)
        y_pred = result['y_pred']
        self.assertTrue(y_pred >= 0.0)

          

if __name__ == '__main__':
    unittest.main()
